# BNNS.Shape.vector(_:stride:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

A constant that represents a shape with a 1D vector data layout.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
case vector(Int, stride: Int = 0)
```

## See Also

### Shape Constants
- [case matrixColumnMajor(Int, Int, stride: (Int, Int))](./matrixcolumnmajor%28_,_,stride%29.md)
  A constant that represents a shape with a 2D column-major data layout.
- [case matrixRowMajor(Int, Int, stride: (Int, Int))](./matrixrowmajor%28_,_,stride%29.md)
  A constant that represents a shape with a 2D row-major data layout.
- [case matrixFirstMajor(Int, Int, stride: (Int, Int))](./matrixfirstmajor%28_,_,stride%29.md)
  A constant that represents a shape with a 2D first-major data layout.
- [case matrixLastMajor(Int, Int, stride: (Int, Int))](./matrixlastmajor%28_,_,stride%29.md)
  A constant that represents a shape with a 2D last-major data layout.
- [case imageCHW(Int, Int, Int, stride: (Int, Int, Int))](./imagechw%28_,_,_,stride%29.md)
  A constant that represents a shape with a 3D image stack data layout.
- [case tensor3DFirstMajor(Int, Int, Int, stride: (Int, Int, Int))](./tensor3dfirstmajor%28_,_,_,stride%29.md)
  A constant that represents a shape with a 3D first-major data layout.
- [case tensor3DLastMajor(Int, Int, Int, stride: (Int, Int, Int))](./tensor3dlastmajor%28_,_,_,stride%29.md)
  A constant that represents a shape with a 3D last-major data layout.
- [case tensor3DNSE(Int, Int, Int, stride: (Int, Int, Int))](./tensor3dnse%28_,_,_,stride%29.md)
  A constant that represents a shape with the size elements embedding dimension, sequence length, and batch size.
- [case tensor3DSNE(Int, Int, Int, stride: (Int, Int, Int))](./tensor3dsne%28_,_,_,stride%29.md)
  A constant that represents a shape with the size elements embedding dimension, batch size, and sequence length.
- [case convolutionWeightsOIHW(Int, Int, Int, Int, stride: (Int, Int, Int, Int))](./convolutionweightsoihw%28_,_,_,_,stride%29.md)
  A constant that represents a shape with a 4D array of convolution weights data layout.
- [case tensor4DFirstMajor(Int, Int, Int, Int, stride: (Int, Int, Int, Int))](./tensor4dfirstmajor%28_,_,_,_,stride%29.md)
  A constant that represents a shape with a 4D first-major data layout.
- [case tensor4DLastMajor(Int, Int, Int, Int, stride: (Int, Int, Int, Int))](./tensor4dlastmajor%28_,_,_,_,stride%29.md)
  A constant that represents a shape with a 4D last-major data layout.
- [case tensor5DFirstMajor(Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int))](./tensor5dfirstmajor%28_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 5D first-major data layout.
- [case tensor5DLastMajor(Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int))](./tensor5dlastmajor%28_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 5D last-major data layout.
- [case tensor6DFirstMajor(Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int))](./tensor6dfirstmajor%28_,_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 6D first-major data layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/shape/vector(_:stride:))*