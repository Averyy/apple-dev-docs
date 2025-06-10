# BNNSDataLayout5DFirstMajor

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 5D first-major tensor.

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
var BNNSDataLayout5DFirstMajor: BNNSDataLayout { get }
```

#### Discussion

The value `(i, j, k, l, m)` is at index:

`m * stride[0] + l * stride[1] + k * stride[2] + j * stride[3] + i * stride[4]`.

- `size[0]` is the size of the first dimension (`i`).
- `size[1]` is the size of the second dimension (`j`).
- `size[2]` is the size of the third dimension (`k`).
- `size[3]` is the size of the fourth dimension (`l`).
- `size[4]` is the size of the fifth dimension (`m`).

## See Also

- [var BNNSDataLayout5DLastMajor: BNNSDataLayout](bnnsdatalayout5dlastmajor.md)
  A constant that represents a 5D last-major tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayout5dfirstmajor)*