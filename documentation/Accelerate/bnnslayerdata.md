# BNNSLayerData

**Framework**: Accelerate  
**Kind**: struct

A structure containing common layer parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct BNNSLayerData
```

## Topics

### Initializers
- [init()](bnnslayerdata/init.md)
- [init(data: UnsafeRawPointer?, data_type: BNNSDataType, data_scale: Float, data_bias: Float, data_table: UnsafePointer<Float>?)](bnnslayerdata/init(data:data_type:data_scale:data_bias:data_table:).md)
  Returns a new layer data structure.
- [init(data: UnsafeRawPointer?, data_type: BNNSDataType, data_scale: Float, data_bias: Float)](bnnslayerdata/init(data:data_type:data_scale:data_bias:).md)
### Instance Properties
- [var data: UnsafeRawPointer?](bnnslayerdata/data.md)
  Pointer to layer values (weights, bias), layout and size are specific to each layer.
- [var data_bias: Float](bnnslayerdata/data_bias.md)
  Conversion bias for values, used for integer data types only, ignored for indexed and float data types.
- [var data_scale: Float](bnnslayerdata/data_scale.md)
  Conversion scale for values, used for integer data types only, ignored for indexed and float data types.
- [var data_table: UnsafePointer<Float>?](bnnslayerdata/data_table.md)
  Conversion table (256 values) for indexed floating point data, used for indexed data types only.
- [var data_type: BNNSDataType](bnnslayerdata/data_type.md)
  Storage data type for the values stored in data.
### Type Properties
- [static var zero: BNNSLayerData](bnnslayerdata/zero.md)
### Type Methods
- [static func indexed8(data: UnsafePointer<Int8>?, data_table: UnsafePointer<Float>) -> BNNSLayerData](bnnslayerdata/indexed8(data:data_table:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [BNNS.Shape](bnns/shape.md)
  Constants that describe the size and data layout of an n-dimensional array descriptor.
- [struct BNNSDataLayout](bnnsdatalayout.md)
  Constants that describe the data type of an n-dimensional array.
- [struct BNNSDataType](bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSNDArrayDescriptor](bnnsndarraydescriptor.md)
  A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.
- [func BNNSDataLayoutGetRank(BNNSDataLayout) -> Int](bnnsdatalayoutgetrank(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerdata)*