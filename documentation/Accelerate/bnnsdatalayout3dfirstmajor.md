# BNNSDataLayout3DFirstMajor

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 3D first-major tensor.

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
var BNNSDataLayout3DFirstMajor: BNNSDataLayout { get }
```

#### Discussion

The value `(i, j, k)` is at index `k * stride[0] + j * stride[1] + i * stride[2]`.

- `size[0]` is the size of the first dimension (`i`).
- `size[1]` is the size of the second dimension (`j`).
- `size[2]` is the size of the third dimension (`k`).

## See Also

- [var BNNSDataLayoutImageCHW: BNNSDataLayout](bnnsdatalayoutimagechw.md)
  A constant that represents a 3D image stack.
- [var BNNSDataLayout3DLastMajor: BNNSDataLayout](bnnsdatalayout3dlastmajor.md)
  A constant that represents a 3D last-major tensor.
- [var BNNSDataLayoutSNE: BNNSDataLayout](bnnsdatalayoutsne.md)
  A constant that represents a 3D tensor with the size elements embedding dimension, batch size, and sequence length.
- [var BNNSDataLayoutNSE: BNNSDataLayout](bnnsdatalayoutnse.md)
  A constant that represents a 3D tensor with the size elements embedding dimension, sequence length, and batch size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayout3dfirstmajor)*