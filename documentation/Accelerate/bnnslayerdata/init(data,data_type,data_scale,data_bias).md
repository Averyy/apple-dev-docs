# init(data:data_type:data_scale:data_bias:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 10.0+ - Deprecated in 15.0
- macOS 10.12+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: BNNS switched to new Layer Parameters data structures.

## Declaration

```swift
init(data: UnsafeRawPointer?, data_type: BNNSDataType, data_scale: Float = 1, data_bias: Float = 0)
```

## See Also

### Initializers
- [init()](./init%28%29.md)
- [init(data: UnsafeRawPointer?, data_type: BNNSDataType, data_scale: Float, data_bias: Float, data_table: UnsafePointer<Float>?)](./init%28data,data_type,data_scale,data_bias,data_table%29.md)
  Returns a new layer data structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerdata/init(data:data_type:data_scale:data_bias:))*