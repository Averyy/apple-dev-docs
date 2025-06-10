# BNNSDataLayout

**Framework**: Accelerate  
**Kind**: struct

Constants that describe the data type of an n-dimensional array.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSDataLayout
```

## Topics

### 1D Data Layouts
- [var BNNSDataLayoutVector: BNNSDataLayout](bnnsdatalayoutvector.md)
  A constant that represents a 1D vector.
- [var BNNSDataLayout1DFirstMajor: BNNSDataLayout](bnnsdatalayout1dfirstmajor.md)
  A constant that represents a 1D first-major vector.
- [var BNNSDataLayout1DLastMajor: BNNSDataLayout](bnnsdatalayout1dlastmajor.md)
  A constant that represents a 1D last-major vector.
### 2D Data Layouts
- [var BNNSDataLayoutColumnMajorMatrix: BNNSDataLayout](bnnsdatalayoutcolumnmajormatrix.md)
  A constant that represents a 2D column-major matrix.
- [var BNNSDataLayoutRowMajorMatrix: BNNSDataLayout](bnnsdatalayoutrowmajormatrix.md)
  A constant that represents a 2D row-major matrix.
- [var BNNSDataLayout2DFirstMajor: BNNSDataLayout](bnnsdatalayout2dfirstmajor.md)
  A constant that represents a 2D first-major matrix.
- [var BNNSDataLayout2DLastMajor: BNNSDataLayout](bnnsdatalayout2dlastmajor.md)
  A constant that represents a 2D last-major matrix.
### 3D Data Layouts
- [var BNNSDataLayoutImageCHW: BNNSDataLayout](bnnsdatalayoutimagechw.md)
  A constant that represents a 3D image stack.
- [var BNNSDataLayout3DFirstMajor: BNNSDataLayout](bnnsdatalayout3dfirstmajor.md)
  A constant that represents a 3D first-major tensor.
- [var BNNSDataLayout3DLastMajor: BNNSDataLayout](bnnsdatalayout3dlastmajor.md)
  A constant that represents a 3D last-major tensor.
- [var BNNSDataLayoutSNE: BNNSDataLayout](bnnsdatalayoutsne.md)
  A constant that represents a 3D tensor with the size elements embedding dimension, batch size, and sequence length.
- [var BNNSDataLayoutNSE: BNNSDataLayout](bnnsdatalayoutnse.md)
  A constant that represents a 3D tensor with the size elements embedding dimension, sequence length, and batch size.
### 4D Data Layouts
- [var BNNSDataLayoutConvolutionWeightsOIHW: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihw.md)
  A constant that represents a 4D array of convolution weights.
- [var BNNSDataLayoutConvolutionWeightsIOHrWr: BNNSDataLayout](bnnsdatalayoutconvolutionweightsiohrwr.md)
  A constant that represents a 4D array of rotated convolution weights.
- [var BNNSDataLayoutConvolutionWeightsOIHrWr: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihrwr.md)
  A constant that represents a 4D array of rotated convolution weights.
- [var BNNSDataLayoutConvolutionWeightsOIHW_Pack32: BNNSDataLayout](bnnsdatalayoutconvolutionweightsoihw_pack32.md)
  A constant that represents a 4D array of packed convolution weights with 32-output channel packing and 128-byte array address alignment.
- [var BNNSDataLayout4DFirstMajor: BNNSDataLayout](bnnsdatalayout4dfirstmajor.md)
  A constant that represents a 4D first-major tensor.
- [var BNNSDataLayout4DLastMajor: BNNSDataLayout](bnnsdatalayout4dlastmajor.md)
  A constant that represents a 4D last-major tensor.
### 5D Data Layouts
- [var BNNSDataLayout5DFirstMajor: BNNSDataLayout](bnnsdatalayout5dfirstmajor.md)
  A constant that represents a 5D first-major tensor.
- [var BNNSDataLayout5DLastMajor: BNNSDataLayout](bnnsdatalayout5dlastmajor.md)
  A constant that represents a 5D last-major tensor.
### 6D Data Layouts
- [var BNNSDataLayout6DFirstMajor: BNNSDataLayout](bnnsdatalayout6dfirstmajor.md)
  A constant that represents a 6D first-major tensor.
- [var BNNSDataLayout6DLastMajor: BNNSDataLayout](bnnsdatalayout6dlastmajor.md)
  A constant that represents a 6D last-major tensor.
### 7D Data Layouts
- [var BNNSDataLayout7DFirstMajor: BNNSDataLayout](bnnsdatalayout7dfirstmajor.md)
  A constant that represents a 7D first-major tensor.
- [var BNNSDataLayout7DLastMajor: BNNSDataLayout](bnnsdatalayout7dlastmajor.md)
  A constant that represents a 7D last-major tensor.
### 8D Data Layouts
- [var BNNSDataLayout8DFirstMajor: BNNSDataLayout](bnnsdatalayout8dfirstmajor.md)
  A constant that represents a 8D first-major tensor.
- [var BNNSDataLayout8DLastMajor: BNNSDataLayout](bnnsdatalayout8dlastmajor.md)
  A constant that represents a 8D last-major tensor.
### Other Data Layouts
- [var BNNSDataLayoutFullyConnectedSparse: BNNSDataLayout](bnnsdatalayoutfullyconnectedsparse.md)
- [var BNNSDataLayoutMHA_DHK: BNNSDataLayout](bnnsdatalayoutmha_dhk.md)
### Raw Values
- [init(UInt32)](bnnsdatalayout/init(_:).md)
- [init(rawValue: UInt32)](bnnsdatalayout/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsdatalayout/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct BNNSLayerData](bnnslayerdata.md)
  A structure containing common layer parameters.
- [BNNS.Shape](bnns/shape.md)
  Constants that describe the size and data layout of an n-dimensional array descriptor.
- [struct BNNSDataType](bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSNDArrayDescriptor](bnnsndarraydescriptor.md)
  A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.
- [func BNNSDataLayoutGetRank(BNNSDataLayout) -> Int](bnnsdatalayoutgetrank(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayout)*