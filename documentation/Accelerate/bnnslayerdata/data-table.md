# data_table

**Framework**: Accelerate  
**Kind**: property

Conversion table (256 values) for indexed floating point data, used for indexed data types only.

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
var data_table: UnsafePointer<Float>?
```

## See Also

- [var data: UnsafeRawPointer?](bnnslayerdata/data.md)
  Pointer to layer values (weights, bias), layout and size are specific to each layer.
- [var data_bias: Float](bnnslayerdata/data_bias.md)
  Conversion bias for values, used for integer data types only, ignored for indexed and float data types.
- [var data_scale: Float](bnnslayerdata/data_scale.md)
  Conversion scale for values, used for integer data types only, ignored for indexed and float data types.
- [var data_type: BNNSDataType](bnnslayerdata/data_type.md)
  Storage data type for the values stored in data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerdata/data_table)*