# data_scale

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

Conversion scale for values, used for integer data types only, ignored for indexed and float data types.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.12+ - Deprecated in 11.0
- tvOS 10.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: BNNS switched to new Layer Parameters data structures

## Declaration

```swift
var data_scale: Float
```

```c
float data_scale;
```

## See Also

### Instance Properties
- [var data: UnsafeRawPointer?](./data.md)
  Pointer to layer values (weights, bias), layout and size are specific to each layer.
- [var data_bias: Float](./data_bias.md)
  Conversion bias for values, used for integer data types only, ignored for indexed and float data types.
- [var data_table: UnsafePointer<Float>?](./data_table.md)
  Conversion table (256 values) for indexed floating point data, used for indexed data types only.
- [var data_type: BNNSDataType](./data_type.md)
  Storage data type for the values stored in data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerdata/data_scale)*