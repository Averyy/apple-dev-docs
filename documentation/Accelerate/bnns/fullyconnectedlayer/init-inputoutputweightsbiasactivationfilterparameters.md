# init(input:output:weights:bias:activation:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new fully connected layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?, activation: BNNS.ActivationFunction, filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  The input data type and the weights data type must be equal and be `float`, `float16`, `int8`, or `int16` for the forward pass. The output data type must be `float` for the forward pass. All three arrays must be `float` for the backward pass.

 The input data type and the weights data type must be equal and be `float`, `float16`, `int8`, or `int16` for the forward pass. The output data type must be `float` for the forward pass. All three arrays must be `float` for the backward pass.

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `weights`: The descriptor of the weights.
- `bias`: The descriptor of the bias.
- `activation`: The activation function that the layer applies to the output.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fullyconnectedlayer/init(input:output:weights:bias:activation:filterparameters:))*