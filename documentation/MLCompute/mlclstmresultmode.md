# MLCLSTMResultMode

**Framework**: ML Compute  
**Kind**: enum

Constants that describe the result of an LSTM layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCLSTMResultMode
```

## Topics

### Enumeration Cases
- [MLCLSTMResultMode.output](mlclstmresultmode/output.md)
  A result mode that indicates the layer produces a single result tensor that represents the final output of the LSTM.
- [MLCLSTMResultMode.outputAndStates](mlclstmresultmode/outputandstates.md)
  A result mode that indicates the layer produces three result tensors that represent the final output of the LSTM, the last hidden state, and the cell state.
- [var debugDescription: String](mlclstmresultmode/debugdescription.md)
  A textual description of the LSTM result mode you use for debugging.
### Initializers
- [init?(rawValue: UInt64)](mlclstmresultmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], biases: [MLCTensor]?)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:biases:).md)
  Creates an LSTM layer with the descriptor, input and hidden weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:peepholeweights:biases:).md)
  Creates an LSTM layer with the descriptor, weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?, gateActivations: [MLCActivationDescriptor], outputResultActivation: MLCActivationDescriptor)](mlclstmlayer/init(descriptor:inputweights:hiddenweights:peepholeweights:biases:gateactivations:outputresultactivation:).md)
  Creates an LSTM layer using the descriptor, weights, biases, gate activations, and output result activation that you specify.
- [class MLCLSTMDescriptor](mlclstmdescriptor.md)
  The configuration object you use to create the LSTM layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmresultmode)*