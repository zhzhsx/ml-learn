#!/bin/env python3


def d(a):
    b = a[1:]
    b.append(0)
    return [i - j for i, j in zip(a, b)]


def main():
    # 格力
    print(d([154.61, 94.52, 40.15]))
    print(d([154.21, 112.29, 64.02, 31.60]))
    print(d([125.32, 99.53, 57.21, 27.75]))
    print("================")

    # 江西铜业
    print(d([15.81, 8.3, 5.41]))
    print(d([7.88, 9.88, 4.73, 2.01]))


if __name__ == '__main__':
    main()
