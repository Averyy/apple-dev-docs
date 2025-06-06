# init(i_desc:w_desc:o_desc:bias:activation:)

**Framework**: Accelerate  
**Kind**: init

Returns a new fully connected layer parameters structure from the specified parameters.

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
init(i_desc: BNNSNDArrayDescriptor, w_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor, activation: BNNSActivation)
```

#### Discussion

> ❗ **Important**:  The input data type and the weights data type must be equal and be `float`, `float16`, `int8`, or `int16` for the forward pass. The output data type must be `float` for the forward pass. All three arrays must be `float` for the backward pass.

 The input data type and the weights data type must be equal and be `float`, `float16`, `int8`, or `int16` for the forward pass. The output data type must be `float` for the forward pass. All three arrays must be `float` for the backward pass.

## Parameters

- `i_desc`: The descriptor of the input.
- `w_desc`: The descriptor of the weights.
- `o_desc`: The descriptor of the output.
- `bias`: The descriptor of the bias.
- `activation`: The activation function that the layer applies to the output.

## See Also

- [init()](bnnslayerparametersfullyconnected/init.md)
  Returns a new fully connected layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersfullyconnected/init(i_desc:w_desc:o_desc:bias:activation:))*