# BNNS.Shape

**Framework**: Accelerate  
**Kind**: enum

Constants that describe the size and data layout of an n-dimensional array descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
enum Shape
```

## Topics

### Creating a Shape
- [init([Int], dataLayout: BNNS.DataLayout?, stride: [Int]?)](bnns/shape/init(_:datalayout:stride:).md)
  Returns a new shape with the specified size, data layout, and stride.
- [init(arrayLiteral: BNNS.Shape.ArrayLiteralElement...)](bnns/shape/init(arrayliteral:).md)
  Returns a new shape with the specified size.
### Specifying the Data Layout of a Shape
- [BNNS.DataLayout](bnns/datalayout.md)
  Constants that describe the data layout of an n-dimensional array descriptor shape.
### Shape Constants
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
- [case tensor3DNSE(Int, Int, Int, stride: (Int, Int, Int))](bnns/shape/tensor3dnse(_:_:_:stride:).md)
  A constant that represents a shape with the size elements embedding dimension, sequence length, and batch size.
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
- [case tensor6DLastMajor(Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int))](bnns/shape/tensor6dlastmajor(_:_:_:_:_:_:stride:).md)
  A constant that represents a shape with a 6D last-major data layout.
- [case tensor7DFirstMajor(Int, Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int, Int))](bnns/shape/tensor7dfirstmajor(_:_:_:_:_:_:_:stride:).md)
  A constant that represents a shape with a 7D first-major data layout.
- [case tensor7DLastMajor(Int, Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int, Int))](bnns/shape/tensor7dlastmajor(_:_:_:_:_:_:_:stride:).md)
  A constant that represents a shape with a 7D last-major data layout.
- [case tensor8DFirstMajor(Int, Int, Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int, Int, Int))](bnns/shape/tensor8dfirstmajor(_:_:_:_:_:_:_:_:stride:).md)
  A constant that represents a shape with a 8D first-major data layout.
- [case tensor8DLastMajor(Int, Int, Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int, Int, Int))](bnns/shape/tensor8dlastmajor(_:_:_:_:_:_:_:_:stride:).md)
  A constant that represents a shape with a 8D last-major data layout.
### Inspecting the Properties of a Shape
- [var batchStride: Int](bnns/shape/batchstride.md)
  The number of elements between each batch of data in the shape.
- [var layout: BNNSDataLayout](bnns/shape/layout.md)
  The data layout of the shape.
- [var rank: Int](bnns/shape/rank.md)
  The number of dimensions of the shape.
- [var size: (Int, Int, Int, Int, Int, Int, Int, Int)](bnns/shape/size.md)
  The size, in elements, of each dimension of the shape.
- [var stride: (Int, Int, Int, Int, Int, Int, Int, Int)](bnns/shape/stride.md)
  The stride, in elements, of each dimension of the shape.
### Default Implementations
- [ExpressibleByArrayLiteral Implementations](bnns/shape/expressiblebyarrayliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)

## See Also

- [struct BNNSLayerData](bnnslayerdata.md)
  A structure containing common layer parameters.
- [struct BNNSDataLayout](bnnsdatalayout.md)
  Constants that describe the data type of an n-dimensional array.
- [struct BNNSDataType](bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSNDArrayDescriptor](bnnsndarraydescriptor.md)
  A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.
- [func BNNSDataLayoutGetRank(BNNSDataLayout) -> Int](bnnsdatalayoutgetrank(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/shape)*