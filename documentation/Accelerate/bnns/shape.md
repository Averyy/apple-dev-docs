# BNNS.Shape

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the size and data layout of an n-dimensional array descriptor.

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
enum Shape
```

## Topics

### Creating a Shape
- [init([Int], dataLayout: BNNS.DataLayout?, stride: [Int]?)](./shape/init%28_,datalayout,stride%29.md)
  Returns a new shape with the specified size, data layout, and stride.
- [init(arrayLiteral: BNNS.Shape.ArrayLiteralElement...)](./shape/init%28arrayliteral%29.md)
  Returns a new shape with the specified size.
### Specifying the Data Layout of a Shape
- [BNNS.DataLayout](./datalayout.md)
  Constants that describe the data layout of an n-dimensional array descriptor shape.
### Shape Constants
- [case vector(Int, stride: Int)](./shape/vector%28_,stride%29.md)
  A constant that represents a shape with a 1D vector data layout.
- [case matrixColumnMajor(Int, Int, stride: (Int, Int))](./shape/matrixcolumnmajor%28_,_,stride%29.md)
  A constant that represents a shape with a 2D column-major data layout.
- [case matrixRowMajor(Int, Int, stride: (Int, Int))](./shape/matrixrowmajor%28_,_,stride%29.md)
  A constant that represents a shape with a 2D row-major data layout.
- [case matrixFirstMajor(Int, Int, stride: (Int, Int))](./shape/matrixfirstmajor%28_,_,stride%29.md)
  A constant that represents a shape with a 2D first-major data layout.
- [case matrixLastMajor(Int, Int, stride: (Int, Int))](./shape/matrixlastmajor%28_,_,stride%29.md)
  A constant that represents a shape with a 2D last-major data layout.
- [case imageCHW(Int, Int, Int, stride: (Int, Int, Int))](./shape/imagechw%28_,_,_,stride%29.md)
  A constant that represents a shape with a 3D image stack data layout.
- [case tensor3DFirstMajor(Int, Int, Int, stride: (Int, Int, Int))](./shape/tensor3dfirstmajor%28_,_,_,stride%29.md)
  A constant that represents a shape with a 3D first-major data layout.
- [case tensor3DLastMajor(Int, Int, Int, stride: (Int, Int, Int))](./shape/tensor3dlastmajor%28_,_,_,stride%29.md)
  A constant that represents a shape with a 3D last-major data layout.
- [case tensor3DNSE(Int, Int, Int, stride: (Int, Int, Int))](./shape/tensor3dnse%28_,_,_,stride%29.md)
  A constant that represents a shape with the size elements embedding dimension, sequence length, and batch size.
- [case tensor3DSNE(Int, Int, Int, stride: (Int, Int, Int))](./shape/tensor3dsne%28_,_,_,stride%29.md)
  A constant that represents a shape with the size elements embedding dimension, batch size, and sequence length.
- [case convolutionWeightsOIHW(Int, Int, Int, Int, stride: (Int, Int, Int, Int))](./shape/convolutionweightsoihw%28_,_,_,_,stride%29.md)
  A constant that represents a shape with a 4D array of convolution weights data layout.
- [case tensor4DFirstMajor(Int, Int, Int, Int, stride: (Int, Int, Int, Int))](./shape/tensor4dfirstmajor%28_,_,_,_,stride%29.md)
  A constant that represents a shape with a 4D first-major data layout.
- [case tensor4DLastMajor(Int, Int, Int, Int, stride: (Int, Int, Int, Int))](./shape/tensor4dlastmajor%28_,_,_,_,stride%29.md)
  A constant that represents a shape with a 4D last-major data layout.
- [case tensor5DFirstMajor(Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int))](./shape/tensor5dfirstmajor%28_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 5D first-major data layout.
- [case tensor5DLastMajor(Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int))](./shape/tensor5dlastmajor%28_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 5D last-major data layout.
- [case tensor6DFirstMajor(Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int))](./shape/tensor6dfirstmajor%28_,_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 6D first-major data layout.
- [case tensor6DLastMajor(Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int))](./shape/tensor6dlastmajor%28_,_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 6D last-major data layout.
- [case tensor7DFirstMajor(Int, Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int, Int))](./shape/tensor7dfirstmajor%28_,_,_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 7D first-major data layout.
- [case tensor7DLastMajor(Int, Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int, Int))](./shape/tensor7dlastmajor%28_,_,_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 7D last-major data layout.
- [case tensor8DFirstMajor(Int, Int, Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int, Int, Int))](./shape/tensor8dfirstmajor%28_,_,_,_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 8D first-major data layout.
- [case tensor8DLastMajor(Int, Int, Int, Int, Int, Int, Int, Int, stride: (Int, Int, Int, Int, Int, Int, Int, Int))](./shape/tensor8dlastmajor%28_,_,_,_,_,_,_,_,stride%29.md)
  A constant that represents a shape with a 8D last-major data layout.
### Inspecting the Properties of a Shape
- [var batchStride: Int](./shape/batchstride.md)
  The number of elements between each batch of data in the shape.
- [var layout: BNNSDataLayout](./shape/layout.md)
  The data layout of the shape.
- [var rank: Int](./shape/rank.md)
  The number of dimensions of the shape.
- [var size: (Int, Int, Int, Int, Int, Int, Int, Int)](./shape/size.md)
  The size, in elements, of each dimension of the shape.
- [var stride: (Int, Int, Int, Int, Int, Int, Int, Int)](./shape/stride.md)
  The stride, in elements, of each dimension of the shape.
### Default Implementations
- [ExpressibleByArrayLiteral Implementations](./shape/expressiblebyarrayliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)

## See Also

### N-dimensional array descriptor essentials
- [struct BNNSLayerData](../bnnslayerdata.md)
  A structure containing common layer parameters.
- [struct BNNSDataLayout](../bnnsdatalayout.md)
  Constants that describe the data type of an n-dimensional array.
- [struct BNNSDataType](../bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSNDArrayDescriptor](../bnnsndarraydescriptor.md)
  A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.
- [func BNNSDataLayoutGetRank(BNNSDataLayout) -> Int](../bnnsdatalayoutgetrank%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/shape)*