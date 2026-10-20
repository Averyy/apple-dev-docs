# peepholeWeightsParameters

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The peephole weights tensor parameters you use for optimizer updates.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var peepholeWeightsParameters: [MLCTensorParameter]? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) NSArray<MLCTensorParameter *> * peepholeWeightsParameters;
```

## See Also

### Inspecting LSTM Layers
- [var descriptor: MLCLSTMDescriptor](./descriptor.md)
  The configuration object you use to create the LSTM layer.
- [var gateActivations: [MLCActivationDescriptor]](./gateactivations.md)
  The array of gate activations you use for input, hidden, cell, and output gates.
- [var outputResultActivation: MLCActivationDescriptor](./outputresultactivation.md)
  The output activation descriptor.
- [var inputWeights: [MLCTensor]](./inputweights.md)
  The array of tensors that describe the input weights you use for the input, hidden, cell, and output gates.
- [var hiddenWeights: [MLCTensor]](./hiddenweights.md)
  The array of tensors that describe the hidden weights you use for the input, hidden, cell, and output gates.
- [var peepholeWeights: [MLCTensor]?](./peepholeweights.md)
  The array of tensors that describe the peephole weights you use for the input, hidden, cell, and output gates.
- [var biases: [MLCTensor]?](./biases.md)
  The array of tensors that describe the bias terms you use for the input, hidden, cell, and output gates.
- [var inputWeightsParameters: [MLCTensorParameter]](./inputweightsparameters.md)
  The input weights tensor parameters you use for optimizer updates.
- [var hiddenWeightsParameters: [MLCTensorParameter]](./hiddenweightsparameters.md)
  The hidden weights tensor parameters you use for optimizer updates.
- [var biasesParameters: [MLCTensorParameter]?](./biasesparameters.md)
  The biases tensor parameters you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmlayer/peepholeweightsparameters)*