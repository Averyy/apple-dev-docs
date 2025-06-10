# BNNS.Shape.tensor3DNSE(_:_:_:stride:)

**Framework**: Accelerate  
**Kind**: case

A constant that represents a shape with the size elements embedding dimension, sequence length, and batch size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
case tensor3DNSE(Int, Int, Int, stride: (Int, Int, Int) = (0, 0, 0))
```

## See Also

- [var BNNSDataLayoutNSE: BNNSDataLayout](bnnsdatalayoutnse.md)
  A constant that represents a 3D tensor with the size elements embedding dimension, sequence length, and batch size.
- [case vector(Int, stride: Int)](bnns/shape/vector(_:stride:).md)
  A constant that represents a shape with a 1D vector data layout.
- [case matrixColumnMajor(Int, Int, stride: (Int, Int))](bnns/shape/matrixcolumnmajor(_:_:stride:).md)
  A constant that represents a shape with a 2D column-major data layout.
- [case matrixRowMajor(Int, Int, stride: (Int, Int))](bnns/shape/matrixrowmajor(_:_:stride:).md)
  A constant that represents a shape with a 2D row-major data layout.
- [case matrixFirstMajor(Int, Int, stride: (Int, Int))](bnns/shape/matrixfirstmajor(_:_:stride:).md)
  A constant that represents a shape with a 2D first-major data layout.
- [case matrixLastMajor(Int, Int, stride: (Int, Int))](bnns/shape/matrixlastmajor(_:_:stride:).md)
  A constant that represents a shape with a 2D last-major data layout.
- [case imageCHW(Int, Int, Int, stride: (Int, Int, Int))](bnns/shape/imagechw(_:_:_:stride:).md)
  A constant that represents a shape with a 3D image stack data layout.
- [case tensor3DFirstMajor(Int, Int, Int, stride: (Int, Int, Int))](bnns/shape/tensor3dfirstmajor(_:_:_:stride:).md)
  A constant that represents a shape with a 3D first-major data layout.
- [case tensor3DLastMajor(Int, Int, Int, stride: (Int, Int, Int))](bnns/shape/tensor3dlastmajor(_:_:_:stride:).md)
  A constant that represents a shape with a 3D last-major data layout.
- [case tensor3DSNE(Int, Int, Int, stride: (Int, Int, Int))](bnns/shape/tensor3dsne(_:_:_:stride:).md)
  A constant that represents a shape with the size elements embedding dimension, batch size, and sequence length.
- [case convolutionWeightsOIHW(Int, Int, Int, Int, stride: (Int, Int, Int, Int))](bnns/shape/convolutionweightsoihw(_:_:_:_:stride:).md)
  A constant that represents a shape with a 4D array of convolution weights data layout.
- [case tensor4DFirstMajor(Int, Int, Int, Int, stride: (Int, Int, Int, Int))](bnns/shape/tensor4dfirstmajor(_:_:_:_:stride:).md)
  A constant that represents a shape with a 4D first-major data layout.
- [case tensor4DLastMajor(Int, Int, Int, Int, stride: (Int, Int, Int, Int))](bnns/shape/tensor4dlastmajor(_:_:_:_:stride:).md)
  A constant that represents a shape with a 4D last-major data layout.
- [case tensor5DFirstMajor(Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int))](bnns/shape/tensor5dfirstmajor(_:_:_:_:_:stride:).md)
  A constant that represents a shape with a 5D first-major data layout.
- [case tensor5DLastMajor(Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int))](bnns/shape/tensor5dlastmajor(_:_:_:_:_:stride:).md)
  A constant that represents a shape with a 5D last-major data layout.
- [case tensor6DFirstMajor(Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int))](bnns/shape/tensor6dfirstmajor(_:_:_:_:_:_:stride:).md)
  A constant that represents a shape with a 6D first-major data layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/shape/tensor3dnse(_:_:_:stride:))*