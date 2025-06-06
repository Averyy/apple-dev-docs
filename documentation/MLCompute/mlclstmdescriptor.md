# MLCLSTMDescriptor

**Framework**: ML Compute  
**Kind**: class

The configuration object you use to create the LSTM layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCLSTMDescriptor
```

## Topics

### Creating LSTM Descriptors
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int)](mlclstmdescriptor/init(inputsize:hiddensize:layercount:).md)
  Creates a batch first LSTM descriptor with the input size and number of layers you specify.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, isBidirectional: Bool, dropout: Float)](mlclstmdescriptor/init(inputsize:hiddensize:layercount:usesbiases:isbidirectional:dropout:).md)
  Creates a batch first LSTM descriptor with bias and bidirectional options you specify.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, dropout: Float)](mlclstmdescriptor/init(inputsize:hiddensize:layercount:usesbiases:batchfirst:isbidirectional:dropout:).md)
  Creates a batch first LSTM descriptor that allows you to indicate whether the input and output shape is batch first.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, returnsSequences: Bool, dropout: Float)](mlclstmdescriptor/init(inputsize:hiddensize:layercount:usesbiases:batchfirst:isbidirectional:returnssequences:dropout:).md)
  Creates a batch first LSTM descriptor that allows you to indicate whether the layer returns output for all sequences, or output for only the last sequence.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, returnsSequences: Bool, dropout: Float, resultMode: MLCLSTMResultMode)](mlclstmdescriptor/init(inputsize:hiddensize:layercount:usesbiases:batchfirst:isbidirectional:returnssequences:dropout:resultmode:).md)
  Creates a descriptor with the number of features and layers, dropout, and options for use of biases, batch order, return sequences, bidirectionality, and expected tensors you specify.
### Inspecting LSTM Descriptors
- [var batchFirst: Bool](mlclstmdescriptor/batchfirst.md)
  A Boolean that indicates whether the input and output shape is batch first.
- [var dropout: Float](mlclstmdescriptor/dropout.md)
  The dropout probability.
- [var hiddenSize: Int](mlclstmdescriptor/hiddensize.md)
  The number of features in the hidden state.
- [var inputSize: Int](mlclstmdescriptor/inputsize.md)
  The number of expected features in the input.
- [var isBidirectional: Bool](mlclstmdescriptor/isbidirectional.md)
  A Boolean that indicates whether the layer is bidirectional.
- [var layerCount: Int](mlclstmdescriptor/layercount.md)
  The number of recurrent layers.
- [var resultMode: MLCLSTMResultMode](mlclstmdescriptor/resultmode.md)
  The mode that indicates whether the layer produces a single result tensor or three result tensors — final output, last hidden state, and the cell state.
- [var returnsSequences: Bool](mlclstmdescriptor/returnssequences.md)
  A Boolean that indicates whether the layer returns output for all sequences.
- [var usesBiases: Bool](mlclstmdescriptor/usesbiases.md)
  A Boolean that indicates whether you use bias weights.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], biases: [MLCTensor]?)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:biases:).md)
  Creates an LSTM layer with the descriptor, input and hidden weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:peepholeweights:biases:).md)
  Creates an LSTM layer with the descriptor, weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?, gateActivations: [MLCActivationDescriptor], outputResultActivation: MLCActivationDescriptor)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:peepholeweights:biases:gateactivations:outputresultactivation:).md)
  Creates an LSTM layer using the descriptor, weights, biases, gate activations, and output result activation that you specify.
- [enum MLCLSTMResultMode](mlclstmresultmode.md)
  Constants that describe the result of an LSTM layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmdescriptor)*