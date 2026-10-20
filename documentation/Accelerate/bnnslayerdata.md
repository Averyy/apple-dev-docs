# BNNSLayerData

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure containing common layer parameters.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.12+ - Deprecated in 11.0
- tvOS 10.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: Use [`BNNSNDArrayDescriptor`](./bnnsndarraydescriptor.md) instead.

## Declaration

```swift
struct BNNSLayerData
```

```c
typedef struct { ... } BNNSLayerData;
```

## Topics

### Initializers
- [init()](./bnnslayerdata/init%28%29.md)
- [init(data: UnsafeRawPointer?, data_type: BNNSDataType, data_scale: Float, data_bias: Float, data_table: UnsafePointer<Float>?)](./bnnslayerdata/init%28data,data_type,data_scale,data_bias,data_table%29.md)
  Returns a new layer data structure.
- [init(data: UnsafeRawPointer?, data_type: BNNSDataType, data_scale: Float, data_bias: Float)](./bnnslayerdata/init%28data,data_type,data_scale,data_bias%29.md)
### Instance Properties
- [var data: UnsafeRawPointer?](./bnnslayerdata/data.md)
  Pointer to layer values (weights, bias), layout and size are specific to each layer.
- [var data_bias: Float](./bnnslayerdata/data_bias.md)
  Conversion bias for values, used for integer data types only, ignored for indexed and float data types.
- [var data_scale: Float](./bnnslayerdata/data_scale.md)
  Conversion scale for values, used for integer data types only, ignored for indexed and float data types.
- [var data_table: UnsafePointer<Float>?](./bnnslayerdata/data_table.md)
  Conversion table (256 values) for indexed floating point data, used for indexed data types only.
- [var data_type: BNNSDataType](./bnnslayerdata/data_type.md)
  Storage data type for the values stored in data.
### Type Properties
- [static var zero: BNNSLayerData](./bnnslayerdata/zero.md)
### Type Methods
- [static func indexed8(data: UnsafePointer<Int8>?, data_table: UnsafePointer<Float>) -> BNNSLayerData](./bnnslayerdata/indexed8%28data,data_table%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### N-dimensional array descriptor essentials
- [BNNS.Shape](./bnns/shape.md)
  Constants that describe the size and data layout of an n-dimensional array descriptor.
- [struct BNNSDataLayout](./bnnsdatalayout.md)
  Constants that describe the data type of an n-dimensional array.
- [struct BNNSDataType](./bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSNDArrayDescriptor](./bnnsndarraydescriptor.md)
  A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.
- [func BNNSDataLayoutGetRank(BNNSDataLayout) -> Int](./bnnsdatalayoutgetrank%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerdata)*