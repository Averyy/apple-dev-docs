# BNNSDataLayoutNSE

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 3D tensor with the size elements embedding dimension, sequence length, and batch size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var BNNSDataLayoutNSE: BNNSDataLayout { get }
```

#### Discussion

The value `(e, s, n)` is at index `e * stride[0] + s * stride[1] + n * stride[2]`.

- `size[0]` is the embedding dimension (`e`).
- `size[1]` is the sequence length (`s`).
- `size[2]` is the batch size (`n`).

## See Also

- [var BNNSDataLayoutImageCHW: BNNSDataLayout](bnnsdatalayoutimagechw.md)
  A constant that represents a 3D image stack.
- [var BNNSDataLayout3DFirstMajor: BNNSDataLayout](bnnsdatalayout3dfirstmajor.md)
  A constant that represents a 3D first-major tensor.
- [var BNNSDataLayout3DLastMajor: BNNSDataLayout](bnnsdatalayout3dlastmajor.md)
  A constant that represents a 3D last-major tensor.
- [var BNNSDataLayoutSNE: BNNSDataLayout](bnnsdatalayoutsne.md)
  A constant that represents a 3D tensor with the size elements embedding dimension, batch size, and sequence length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayoutnse)*