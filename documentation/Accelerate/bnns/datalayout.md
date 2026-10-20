# BNNS.DataLayout

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the data layout of an n-dimensional array descriptor shape.

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
enum DataLayout
```

## Topics

### Data Layout Constants
- [BNNS.DataLayout.vector](./datalayout/vector.md)
  A constant that represents a 1D vector.
- [BNNS.DataLayout.matrixColumnMajor](./datalayout/matrixcolumnmajor.md)
  A constant that represents a 2D column-major matrix.
- [BNNS.DataLayout.matrixRowMajor](./datalayout/matrixrowmajor.md)
  A constant that represents a 2D row-major matrix.
- [BNNS.DataLayout.matrixFirstMajor](./datalayout/matrixfirstmajor.md)
  A constant that represents a 2D first-major matrix.
- [BNNS.DataLayout.matrixLastMajor](./datalayout/matrixlastmajor.md)
  A constant that represents a 2D last-major matrix.
- [BNNS.DataLayout.imageCHW](./datalayout/imagechw.md)
  A constant that represents a 3D image stack.
- [BNNS.DataLayout.tensor3DFirstMajor](./datalayout/tensor3dfirstmajor.md)
  A constant that represents a 3D first-major tensor.
- [BNNS.DataLayout.tensor3DLastMajor](./datalayout/tensor3dlastmajor.md)
  A constant that represents a 3D last-major tensor.
- [BNNS.DataLayout.tensor3DNSE](./datalayout/tensor3dnse.md)
  A constant that represents a 3D tensor with size ordered by embedding dimension, sequence length, batch size.
- [BNNS.DataLayout.tensor3DSNE](./datalayout/tensor3dsne.md)
  A constant that represents a 3D tensor with size ordered by embedding dimension, batch size, sequence length.
- [BNNS.DataLayout.convolutionWeightsOIHW](./datalayout/convolutionweightsoihw.md)
  A constant that represents a 4D array of convolution weights.
- [BNNS.DataLayout.tensor4DFirstMajor](./datalayout/tensor4dfirstmajor.md)
  A constant that represents a 4D first-major tensor.
- [BNNS.DataLayout.tensor4DLastMajor](./datalayout/tensor4dlastmajor.md)
  A constant that represents a 4D last-major tensor.
- [BNNS.DataLayout.tensor5DFirstMajor](./datalayout/tensor5dfirstmajor.md)
  A constant that represents a 5D first-major tensor.
- [BNNS.DataLayout.tensor5DLastMajor](./datalayout/tensor5dlastmajor.md)
  A constant that represents a 5D last-major tensor.
- [BNNS.DataLayout.tensor6DFirstMajor](./datalayout/tensor6dfirstmajor.md)
  A constant that represents a 6D first-major tensor.
- [BNNS.DataLayout.tensor6DLastMajor](./datalayout/tensor6dlastmajor.md)
  A constant that represents a 6D last-major tensor.
- [BNNS.DataLayout.tensor7DFirstMajor](./datalayout/tensor7dfirstmajor.md)
  A constant that represents a 7D first-major tensor.
- [BNNS.DataLayout.tensor7DLastMajor](./datalayout/tensor7dlastmajor.md)
  A constant that represents a 7D last-major tensor.
- [BNNS.DataLayout.tensor8DFirstMajor](./datalayout/tensor8dfirstmajor.md)
  A constant that represents a 8D first-major tensor.
- [BNNS.DataLayout.tensor8DLastMajor](./datalayout/tensor8dlastmajor.md)
  A constant that represents a 8D last-major tensor.
### Determining the Number of Dimensions
- [var rank: Int](./datalayout/rank.md)
  The number of dimensions of the data layout.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/datalayout)*