# MLCLSTMResultMode

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the result of an LSTM layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCLSTMResultMode
```

```c
enum MLCLSTMResultMode : uint64_t;
```

## Topics

### Enumeration Cases
- [MLCLSTMResultMode.output](./mlclstmresultmode/output.md)
  A result mode that indicates the layer produces a single result tensor that represents the final output of the LSTM.
- [MLCLSTMResultMode.outputAndStates](./mlclstmresultmode/outputandstates.md)
  A result mode that indicates the layer produces three result tensors that represent the final output of the LSTM, the last hidden state, and the cell state.
- [var debugDescription: String](./mlclstmresultmode/debugdescription.md)
  A textual description of the LSTM result mode you use for debugging.
### Initializers
- [init?(rawValue: UInt64)](./mlclstmresultmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating LSTM Layers
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], biases: [MLCTensor]?)](./mlclstmlayer/init%28descriptor,inputweights,hiddenweights,biases%29.md)
  Creates an LSTM layer with the descriptor, input and hidden weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?)](./mlclstmlayer/init%28descriptor,inputweights,hiddenweights,peepholeweights,biases%29.md)
  Creates an LSTM layer with the descriptor, weights, and biases you specify.
- [convenience init?(descriptor: MLCLSTMDescriptor, inputWeights: [MLCTensor], hiddenWeights: [MLCTensor], peepholeWeights: [MLCTensor]?, biases: [MLCTensor]?, gateActivations: [MLCActivationDescriptor], outputResultActivation: MLCActivationDescriptor)](./mlclstmlayer/init%28descriptor,inputweights,hiddenweights,peepholeweights,biases,gateactivations,outputresultactivation%29.md)
  Creates an LSTM layer using the descriptor, weights, biases, gate activations, and output result activation that you specify.
- [class MLCLSTMDescriptor](./mlclstmdescriptor.md)
  The configuration object you use to create the LSTM layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmresultmode)*