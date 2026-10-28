# sequence_descriptor

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A 1D array of unsigned-integer elements that determines the batch size for each step.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
var sequence_descriptor: BNNSNDArrayDescriptor
```

```c
BNNSNDArrayDescriptor sequence_descriptor;
```

## Discussion

If [`seq_len`](./seq_len.md) is greater than `1` and the [`data`](../bnnsndarraydescriptor/data.md) property of this descriptor is `nil`, BNNS uses the same [`batch_size`](./batch_size.md) for the entire sequence.

## See Also

### Instance Properties
- [var input_size: Int](./input_size.md)
  The number of elements in the input.
- [var hidden_size: Int](./hidden_size.md)
  The number of elements in the hidden state.
- [var batch_size: Int](./batch_size.md)
  The number of input and output samples.
- [var num_layers: Int](./num_layers.md)
  The number of stacked long short-term memory (LSTM) layers.
- [var seq_len: Int](./seq_len.md)
  The size of the sequential input.
- [var dropout: Float](./dropout.md)
  The dropout ratio to apply between long short-term memory (LSTM) layers.
- [var lstm_flags: UInt32](./lstm_flags.md)
  Flags that control the behavior of a long short-term memory (LSTM) layer.
- [var input_descriptor: BNNSLSTMDataDescriptor](./input_descriptor.md)
  Descriptors of the input, hidden input, and cell-state input data.
- [var output_descriptor: BNNSLSTMDataDescriptor](./output_descriptor.md)
  Descriptors of the output, hidden output, and cell-state output data.
- [var input_gate: BNNSLSTMGateDescriptor](./input_gate.md)
  The descriptor of the input gate, which uses default sigmoid activation.
- [var forget_gate: BNNSLSTMGateDescriptor](./forget_gate.md)
  The descriptor of the forget gate, which uses default sigmoid activation.
- [var candidate_gate: BNNSLSTMGateDescriptor](./candidate_gate.md)
  The descriptor of the candidate gate, which uses default tanh activation.
- [var output_gate: BNNSLSTMGateDescriptor](./output_gate.md)
  The descriptor of the output gate, which uses default sigmoid activation.
- [var hidden_activation: BNNSActivation](./hidden_activation.md)
  Hidden activation function, which uses default tanh activation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslstm/sequence_descriptor)*