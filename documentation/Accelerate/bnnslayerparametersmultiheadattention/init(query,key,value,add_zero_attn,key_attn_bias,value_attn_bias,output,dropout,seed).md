# init(query:key:value:add_zero_attn:key_attn_bias:value_attn_bias:output:dropout:seed:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new multihead attention layer parameters structure from the specified parameters.

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
init(query: BNNSMHAProjectionParameters, key: BNNSMHAProjectionParameters, value: BNNSMHAProjectionParameters, add_zero_attn: Bool, key_attn_bias: BNNSNDArrayDescriptor, value_attn_bias: BNNSNDArrayDescriptor, output: BNNSMHAProjectionParameters, dropout: Float, seed: UInt32)
```

## Parameters

- `query`: A projection parameter structure that describes the query-related input parameters and projection.
- `key`: A projection parameter structure that describes the key-related input parameters and projection.
- `value`: A projection parameter structure that describes the value-related input parameters and projection.
- `add_zero_attn`: A Boolean value that, if true, adds a row of zeroes to the projected *K* and *V* inputs to the calculation.
- `key_attn_bias`: A 2D tensor that’s added to the key as part of the attention calculation.
- `value_attn_bias`: A 2D tensor that’s added to the value as part of the attention calculation.
- `output`: A projection parameter structure that describes the output tensor and associated projection.
- `dropout`: The probability that the layer drops out an element.
- `seed`: The seed for the dropout layer’s random number generator.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Returns a new multihead attention layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersmultiheadattention/init(query:key:value:add_zero_attn:key_attn_bias:value_attn_bias:output:dropout:seed:))*