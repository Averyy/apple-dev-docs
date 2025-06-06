# MLCLSTMLayer

**Framework**: ML Compute  
**Kind**: class

A layer that represents long short-term memory (LSTM) networks.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCLSTMLayer
```

#### Overview

Use this class to create an LSTM layer with one of the following configurations:

## Topics

### Creating LSTM Layers
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], biases: [MLCTensor]?)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:biases:).md)
  Creates an LSTM layer with the descriptor, input and hidden weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:peepholeweights:biases:).md)
  Creates an LSTM layer with the descriptor, weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?, gateActivations: [MLCActivationDescriptor], outputResultActivation: MLCActivationDescriptor)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:peepholeweights:biases:gateactivations:outputresultactivation:).md)
  Creates an LSTM layer using the descriptor, weights, biases, gate activations, and output result activation that you specify.
- [class MLCLSTMDescriptor](mlclstmdescriptor.md)
  The configuration object you use to create the LSTM layer.
- [enum MLCLSTMResultMode](mlclstmresultmode.md)
  Constants that describe the result of an LSTM layer.
### Inspecting LSTM Layers
- [var descriptor: MLCLSTMDescriptor](mlclstmlayer/descriptor.md)
  The configuration object you use to create the LSTM layer.
- [var gateActivations: [MLCActivationDescriptor]](mlclstmlayer/gateactivations.md)
  The array of gate activations you use for input, hidden, cell, and output gates.
- [var outputResultActivation: MLCActivationDescriptor](mlclstmlayer/outputresultactivation.md)
  The output activation descriptor.
- [var inputWeights: [MLCTensor]](mlclstmlayer/inputweights.md)
  The array of tensors that describe the input weights you use for the input, hidden, cell, and output gates.
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

## Relationships

### Inherits From
- [MLCLayer](mlclayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCConvolutionLayer](mlcconvolutionlayer.md)
  A layer that applies a convolution over a signal.
- [class MLCPoolingLayer](mlcpoolinglayer.md)
  A layer that summarizes the average presence of a feature.
- [class MLCUpsampleLayer](mlcupsamplelayer.md)
  A layer that applies upsampling with the shape you specify.
- [class MLCEmbeddingLayer](mlcembeddinglayer.md)
  A layer that stores a word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmlayer)*