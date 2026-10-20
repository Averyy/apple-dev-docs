# init(descriptor:inputWeights:hiddenWeights:peepholeWeights:biases:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an LSTM layer with the descriptor, weights, and biases you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?)
```

```objc
+ (instancetype) layerWithDescriptor:(MLCLSTMDescriptor *) descriptor inputWeights:(NSArray<MLCTensor *> *) inputWeights hiddenWeights:(NSArray<MLCTensor *> *) hiddenWeights peepholeWeights:(NSArray<MLCTensor *> *) peepholeWeights biases:(NSArray<MLCTensor *> *) biases;
```

## Parameters

- `descriptor`: An object you use to configure the LSTM layer.
- `inputWeights`: An array that contains tensors that describe the input weights.
- `hiddenWeights`: An array that contains tensors that describe the hidden weights.
- `peepholeWeights`: An array that contains tensors that describe the peephole weights.
- `biases`: An array that contains tensors that describe the bias terms.

## See Also

### Creating LSTM Layers
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], biases: [MLCTensor]?)](./init%28descriptor,inputweights,hiddenweights,biases%29.md)
  Creates an LSTM layer with the descriptor, input and hidden weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?, gateActivations: [MLCActivationDescriptor], outputResultActivation: MLCActivationDescriptor)](./init%28descriptor,inputweights,hiddenweights,peepholeweights,biases,gateactivations,outputresultactivation%29.md)
  Creates an LSTM layer using the descriptor, weights, biases, gate activations, and output result activation that you specify.
- [class MLCLSTMDescriptor](../mlclstmdescriptor.md)
  The configuration object you use to create the LSTM layer.
- [enum MLCLSTMResultMode](../mlclstmresultmode.md)
  Constants that describe the result of an LSTM layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmlayer/init(descriptor:inputweights:hiddenweights:peepholeweights:biases:))*