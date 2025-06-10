# init(data:data_type:data_scale:data_bias:data_table:)

**Framework**: Accelerate  
**Kind**: init

Returns a new layer data structure.

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
init(data: UnsafeRawPointer?, data_type: BNNSDataType, data_scale: Float, data_bias: Float, data_table: UnsafePointer<Float>?)
```

#### Return Value

A new layer data structure.

## Parameters

- `data`: Pointer to layer values (weights, bias), layout and size are specific to each layer.
- `data_type`: Storage data type for the values stored in  .
- `data_scale`: Conversion scale for values, used for integer data types only, ignored for indexed and float data types.
- `data_bias`: Conversion bias for values, used for integer data types only, ignored for indexed and float data types.
- `data_table`: Conversion table (256 values) for indexed floating point data, used for indexed data types only.

## See Also

- [init()](bnnslayerdata/init.md)
- [init(data: UnsafeRawPointer?, data_type: BNNSDataType, data_scale: Float, data_bias: Float)](bnnslayerdata/init(data:data_type:data_scale:data_bias:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerdata/init(data:data_type:data_scale:data_bias:data_table:))*