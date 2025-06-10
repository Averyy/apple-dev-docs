# key_attn_bias

**Framework**: Accelerate  
**Kind**: property

A 2D tensor that’s added to the value as part of the attention calculation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var key_attn_bias: BNNSNDArrayDescriptor
```

## See Also

- [var query: BNNSMHAProjectionParameters](bnnslayerparametersmultiheadattention/query.md)
  A projection parameter structure that describes the query-related input parameters and projection.
- [var key: BNNSMHAProjectionParameters](bnnslayerparametersmultiheadattention/key.md)
  A projection parameter structure that describes the key-related input parameters and projection.
- [var value: BNNSMHAProjectionParameters](bnnslayerparametersmultiheadattention/value.md)
  A projection parameter structure that describes the value-related input parameters and projection.
- [var add_zero_attn: Bool](bnnslayerparametersmultiheadattention/add_zero_attn.md)
  A Boolean value that, if true, adds a row of zeroes to the projected  and  inputs to the calculation.
- [var value_attn_bias: BNNSNDArrayDescriptor](bnnslayerparametersmultiheadattention/value_attn_bias.md)
  An optional `d_value` x `num_heads` 2D tensor that’s added as part of the attention calculation.
- [var output: BNNSMHAProjectionParameters](bnnslayerparametersmultiheadattention/output.md)
  A projection parameter structure that describes the output tensor and associated projection.
- [var dropout: Float](bnnslayerparametersmultiheadattention/dropout.md)
  The seed for the dropout layer’s random number generator.
- [var seed: UInt32](bnnslayerparametersmultiheadattention/seed.md)
  A random seed for the dropout layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersmultiheadattention/key_attn_bias)*