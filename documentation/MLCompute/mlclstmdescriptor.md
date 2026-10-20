# MLCLSTMDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

The configuration object you use to create the LSTM layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCLSTMDescriptor
```

```objc
@interface MLCLSTMDescriptor : NSObject
```

## Topics

### Creating LSTM Descriptors
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int)](./mlclstmdescriptor/init%28inputsize,hiddensize,layercount%29.md)
  Creates a batch first LSTM descriptor with the input size and number of layers you specify.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, isBidirectional: Bool, dropout: Float)](./mlclstmdescriptor/init%28inputsize,hiddensize,layercount,usesbiases,isbidirectional,dropout%29.md)
  Creates a batch first LSTM descriptor with bias and bidirectional options you specify.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, dropout: Float)](./mlclstmdescriptor/init%28inputsize,hiddensize,layercount,usesbiases,batchfirst,isbidirectional,dropout%29.md)
  Creates a batch first LSTM descriptor that allows you to indicate whether the input and output shape is batch first.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, returnsSequences: Bool, dropout: Float)](./mlclstmdescriptor/init%28inputsize,hiddensize,layercount,usesbiases,batchfirst,isbidirectional,returnssequences,dropout%29.md)
  Creates a batch first LSTM descriptor that allows you to indicate whether the layer returns output for all sequences, or output for only the last sequence.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, returnsSequences: Bool, dropout: Float, resultMode: MLCLSTMResultMode)](./mlclstmdescriptor/init%28inputsize,hiddensize,layercount,usesbiases,batchfirst,isbidirectional,returnssequences,dropout,resultmode%29.md)
  Creates a descriptor with the number of features and layers, dropout, and options for use of biases, batch order, return sequences, bidirectionality, and expected tensors you specify.
### Inspecting LSTM Descriptors
- [var batchFirst: Bool](./mlclstmdescriptor/batchfirst.md)
  A Boolean that indicates whether the input and output shape is batch first.
- [var dropout: Float](./mlclstmdescriptor/dropout.md)
  The dropout probability.
- [var hiddenSize: Int](./mlclstmdescriptor/hiddensize.md)
  The number of features in the hidden state.
- [var inputSize: Int](./mlclstmdescriptor/inputsize.md)
  The number of expected features in the input.
- [var isBidirectional: Bool](./mlclstmdescriptor/isbidirectional.md)
  A Boolean that indicates whether the layer is bidirectional.
- [var layerCount: Int](./mlclstmdescriptor/layercount.md)
  The number of recurrent layers.
- [var resultMode: MLCLSTMResultMode](./mlclstmdescriptor/resultmode.md)
  The mode that indicates whether the layer produces a single result tensor or three result tensors — final output, last hidden state, and the cell state.
- [var returnsSequences: Bool](./mlclstmdescriptor/returnssequences.md)
  A Boolean that indicates whether the layer returns output for all sequences.
- [var usesBiases: Bool](./mlclstmdescriptor/usesbiases.md)
  A Boolean that indicates whether you use bias weights.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating LSTM Layers
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], biases: [MLCTensor]?)](./mlclstmlayer/init%28descriptor,inputweights,hiddenweights,biases%29.md)
  Creates an LSTM layer with the descriptor, input and hidden weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?)](./mlclstmlayer/init%28descriptor,inputweights,hiddenweights,peepholeweights,biases%29.md)
  Creates an LSTM layer with the descriptor, weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?, gateActivations: [MLCActivationDescriptor], outputResultActivation: MLCActivationDescriptor)](./mlclstmlayer/init%28descriptor,inputweights,hiddenweights,peepholeweights,biases,gateactivations,outputresultactivation%29.md)
  Creates an LSTM layer using the descriptor, weights, biases, gate activations, and output result activation that you specify.
- [enum MLCLSTMResultMode](./mlclstmresultmode.md)
  Constants that describe the result of an LSTM layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmdescriptor)*