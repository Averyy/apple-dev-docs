# init(descriptor:inputWeights:hiddenWeights:biases:)

**Framework**: ML Compute  
**Kind**: init

Creates an LSTM layer with the descriptor, input and hidden weights, and biases you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], biases: [MLCTensor]?)
```

## Parameters

- `descriptor`: An object you use to configure the LSTM layer.
- `inputWeights`: An array that contains tensors that describe the input weights.
- `hiddenWeights`: An array that contains tensors that describe the hidden weights.
- `biases`: An array that contains tensors that describe the bias terms.

## See Also

- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:peepholeweights:biases:).md)
  Creates an LSTM layer with the descriptor, weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?, gateActivations: [MLCActivationDescriptor], outputResultActivation: MLCActivationDescriptor)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:peepholeweights:biases:gateactivations:outputresultactivation:).md)
  Creates an LSTM layer using the descriptor, weights, biases, gate activations, and output result activation that you specify.
- [class MLCLSTMDescriptor](mlclstmdescriptor.md)
  The configuration object you use to create the LSTM layer.
- [enum MLCLSTMResultMode](mlclstmresultmode.md)
  Constants that describe the result of an LSTM layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmlayer/init(descriptor:inputweights:hiddenweights:biases:))*