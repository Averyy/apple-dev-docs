# init(query:key:value:add_zero_attn:key_attn_bias:value_attn_bias:output:dropout:seed:)

**Framework**: Accelerate  
**Kind**: init

Returns a new multihead attention layer parameters structure from the specified parameters.

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
init(query: BNNSMHAProjectionParameters, key: BNNSMHAProjectionParameters, value: BNNSMHAProjectionParameters, add_zero_attn: Bool, key_attn_bias: BNNSNDArrayDescriptor, value_attn_bias: BNNSNDArrayDescriptor, output: BNNSMHAProjectionParameters, dropout: Float, seed: UInt32)
```

## Parameters

- `query`: A projection parameter structure that describes the query-related input parameters and projection.
- `key`: A projection parameter structure that describes the key-related input parameters and projection.
- `value`: A projection parameter structure that describes the value-related input parameters and projection.
- `add_zero_attn`: A Boolean value that, if true, adds a row of zeroes to the projected   and   inputs to the calculation.
- `key_attn_bias`: A 2D tensor that’s added to the key as part of the attention calculation.
- `value_attn_bias`: A 2D tensor that’s added to the value as part of the attention calculation.
- `output`: A projection parameter structure that describes the output tensor and associated projection.
- `dropout`: The probability that the layer drops out an element.
- `seed`: The seed for the dropout layer’s random number generator.

## See Also

- [init()](bnnslayerparametersmultiheadattention/init.md)
  Returns a new multihead attention layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersmultiheadattention/init(query:key:value:add_zero_attn:key_attn_bias:value_attn_bias:output:dropout:seed:))*