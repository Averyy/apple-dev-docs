# BNNSDataLayout8DFirstMajor

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 8D first-major tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var BNNSDataLayout8DFirstMajor: BNNSDataLayout { get }
```

#### Discussion

The value `(i, j, k, l, m, n, o, p)` is at index:

`p * stride[0] + o * stride[1] + n * stride[2] + m * stride[3] +`

`l * stride[4] + k * stride[5] + j * stride[6] + i * stride[7]`

- `size[0]` is the size of the first dimension (`i`).
- `size[1]` is the size of the second dimension (`j`).
- `size[2]` is the size of the third dimension (`k`).
- `size[3]` is the size of the fourth dimension (`l`).
- `size[4]` is the size of the fifth dimension (`m`).
- `size[5]` is the size of the sixth dimension (`n`).
- `size[6]` is the size of the seventh dimension (`o`).
- `size[7]` is the size of the eighth  dimension (`p`).

## See Also

- [var BNNSDataLayout8DLastMajor: BNNSDataLayout](bnnsdatalayout8dlastmajor.md)
  A constant that represents a 8D last-major tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayout8dfirstmajor)*