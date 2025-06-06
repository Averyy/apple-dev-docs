# inputWeights

**Framework**: ML Compute  
**Kind**: property

The array of tensors that describe the input weights you use for the input, hidden, cell, and output gates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var inputWeights: [MLCTensor] { get }
```

## See Also

- [var descriptor: MLCLSTMDescriptor](mlclstmlayer/descriptor.md)
  The configuration object you use to create the LSTM layer.
- [var gateActivations: [MLCActivationDescriptor]](mlclstmlayer/gateactivations.md)
  The array of gate activations you use for input, hidden, cell, and output gates.
- [var outputResultActivation: MLCActivationDescriptor](mlclstmlayer/outputresultactivation.md)
  The output activation descriptor.
- [var hiddenWeights: [MLCTensor]](mlclstmlayer/hiddenweights.md)
  The array of tensors that describe the hidden weights you use for the input, hidden, cell, and output gates.
- [var peepholeWeights: [MLCTensor]?](mlclstmlayer/peepholeweights.md)
  The array of tensors that describe the peephole weights you use for the input, hidden, cell, and output gates.
- [var biases: [MLCTensor]?](mlclstmlayer/biases.md)
  The array of tensors that describe the bias terms you use for the input, hidden, cell, and output gates.
- [var inputWeightsParameters: [MLCTensorParameter]](mlclstmlayer/inputweightsparameters.md)
  The input weights tensor parameters you use for optimizer updates.
- [var hiddenWeightsParameters: [MLCTensorParameter]](mlclstmlayer/hiddenweightsparameters.md)
  The hidden weights tensor parameters you use for optimizer updates.
- [var peepholeWeightsParameters: [MLCTensorParameter]?](mlclstmlayer/peepholeweightsparameters.md)
  The peephole weights tensor parameters you use for optimizer updates.
- [var biasesParameters: [MLCTensorParameter]?](mlclstmlayer/biasesparameters.md)
  The biases tensor parameters you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmlayer/inputweights)*