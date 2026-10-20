# add_zero_attn

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A Boolean value that, if true, adds a row of zeroes to the projected *K* and *V* inputs to the calculation.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
var add_zero_attn: Bool
```

```c
bool add_zero_attn;
```

## See Also

### Instance Properties
- [var query: BNNSMHAProjectionParameters](./query.md)
  A projection parameter structure that describes the query-related input parameters and projection.
- [var key: BNNSMHAProjectionParameters](./key.md)
  A projection parameter structure that describes the key-related input parameters and projection.
- [var value: BNNSMHAProjectionParameters](./value.md)
  A projection parameter structure that describes the value-related input parameters and projection.
- [var key_attn_bias: BNNSNDArrayDescriptor](./key_attn_bias.md)
  A 2D tensor that’s added to the value as part of the attention calculation.
- [var value_attn_bias: BNNSNDArrayDescriptor](./value_attn_bias.md)
  An optional `d_value` x `num_heads` 2D tensor that’s added as part of the attention calculation.
- [var output: BNNSMHAProjectionParameters](./output.md)
  A projection parameter structure that describes the output tensor and associated projection.
- [var dropout: Float](./dropout.md)
  The seed for the dropout layer’s random number generator.
- [var seed: UInt32](./seed.md)
  A random seed for the dropout layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersmultiheadattention/add_zero_attn)*