# BNNSDataLayout5DLastMajor

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 5D last-major tensor.

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
var BNNSDataLayout5DLastMajor: BNNSDataLayout { get }
```

#### Discussion

The value `(i, j, k, l, m)` is at index:

`i * stride[0] + j * stride[1] + k * stride[2] + l * stride[3] + m * stride[4]`.

- `size[0]` is the size of the first dimension (`i`).
- `size[1]` is the size of the second dimension (`j`).
- `size[2]` is the size of the third dimension (`k`).
- `size[3]` is the size of the fourth dimension (`l`).
- `size[4]` is the size of the fifth dimension (`m`).

## See Also

- [var BNNSDataLayout5DFirstMajor: BNNSDataLayout](bnnsdatalayout5dfirstmajor.md)
  A constant that represents a 5D first-major tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayout5dlastmajor)*