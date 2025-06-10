# output_gate

**Framework**: Accelerate  
**Kind**: property

The descriptor of the output gate, which uses default sigmoid activation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var output_gate: BNNSLSTMGateDescriptor
```

#### Discussion

Use C style multidimensional array notation to order the memory pointers as `[` [`num_layers`](bnnslayerparameterslstm/num_layers.md) `][num_directions][` [`hidden_size`](bnnslayerparameterslstm/hidden_size.md) `][` [`input_size`](bnnslayerparameterslstm/input_size.md) / [`hidden_size`](bnnslayerparameterslstm/hidden_size.md) `]`.

If [`lstm_flags`](bnnslayerparameterslstm/lstm_flags.md) includes [`BNNSLayerFlagsLSTMBidirectional`](bnnslayerflagslstmbidirectional.md), BNNS defines `num_directions` as `2`, or otherwise `1`.

## See Also

- [var input_size: Int](bnnslayerparameterslstm/input_size.md)
  The number of elements in the input.
- [var hidden_size: Int](bnnslayerparameterslstm/hidden_size.md)
  The number of elements in the hidden state.
- [var batch_size: Int](bnnslayerparameterslstm/batch_size.md)
  The number of input and output samples.
- [var num_layers: Int](bnnslayerparameterslstm/num_layers.md)
  The number of stacked long short-term memory (LSTM) layers.
- [var seq_len: Int](bnnslayerparameterslstm/seq_len.md)
  The size of the sequential input.
- [var dropout: Float](bnnslayerparameterslstm/dropout.md)
  The dropout ratio to apply between long short-term memory (LSTM) layers.
- [var lstm_flags: UInt32](bnnslayerparameterslstm/lstm_flags.md)
  Flags that control the behavior of a long short-term memory (LSTM) layer.
- [var sequence_descriptor: BNNSNDArrayDescriptor](bnnslayerparameterslstm/sequence_descriptor.md)
  A 1D array of unsigned-integer elements that determines the batch size for each step.
- [var input_descriptor: BNNSLSTMDataDescriptor](bnnslayerparameterslstm/input_descriptor.md)
  Descriptors of the input, hidden input, and cell-state input data.
- [var output_descriptor: BNNSLSTMDataDescriptor](bnnslayerparameterslstm/output_descriptor.md)
  Descriptors of the output, hidden output, and cell-state output data.
- [var input_gate: BNNSLSTMGateDescriptor](bnnslayerparameterslstm/input_gate.md)
  The descriptor of the input gate, which uses default sigmoid activation.
- [var forget_gate: BNNSLSTMGateDescriptor](bnnslayerparameterslstm/forget_gate.md)
  The descriptor of the forget gate, which uses default sigmoid activation.
- [var candidate_gate: BNNSLSTMGateDescriptor](bnnslayerparameterslstm/candidate_gate.md)
  The descriptor of the candidate gate, which uses default tanh activation.
- [var hidden_activation: BNNSActivation](bnnslayerparameterslstm/hidden_activation.md)
  Hidden activation function, which uses default tanh activation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslstm/output_gate)*