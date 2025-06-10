# init(input_size:hidden_size:batch_size:num_layers:seq_len:dropout:lstm_flags:sequence_descriptor:input_descriptor:output_descriptor:input_gate:forget_gate:candidate_gate:output_gate:hidden_activation:)

**Framework**: Accelerate  
**Kind**: init

Returns a new long short-term memory (LSTM) parameters structure from the specified parameters.

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
init(input_size: Int, hidden_size: Int, batch_size: Int, num_layers: Int, seq_len: Int, dropout: Float, lstm_flags: UInt32, sequence_descriptor: BNNSNDArrayDescriptor, input_descriptor: BNNSLSTMDataDescriptor, output_descriptor: BNNSLSTMDataDescriptor, input_gate: BNNSLSTMGateDescriptor, forget_gate: BNNSLSTMGateDescriptor, candidate_gate: BNNSLSTMGateDescriptor, output_gate: BNNSLSTMGateDescriptor, hidden_activation: BNNSActivation)
```

#### Discussion

To enable peephole connections, set the weights pointer in the corresponding gates descriptor. To enable bias, set the bias pointer in the corresponding gates descriptor.

BNNS treats the [`hidden_desc`](bnnslstmdatadescriptor/hidden_desc.md) of the [`input_descriptor`](bnnslayerparameterslstm/input_descriptor.md) as a zero-filled array if its [`data`](bnnsndarraydescriptor/data.md) is `nil`. BNNS treats the [`cell_state_desc`](bnnslstmdatadescriptor/cell_state_desc.md) of the [`input_descriptor`](bnnslayerparameterslstm/input_descriptor.md) as a zero-filled array if its [`data`](bnnsndarraydescriptor/data.md) is `nil`.

## Parameters

- `input_size`: The number of elements in the input.
- `hidden_size`: The number of elements in the hidden state.
- `batch_size`: The number of input and output samples.
- `num_layers`: The number of stacked LSTM layers.
- `seq_len`: The size of the sequential input.
- `dropout`: The dropout ratio to apply between LSTM layers. BNNS doesn’t apply dropout to the last stacked layer and ignores this parameter when the number of layers is  .
- `lstm_flags`: Flags that control the behavior of an LSTM layer.
- `sequence_descriptor`: A 1D array of unsigned-integer elements that determines the batch size for each step. If   is greater than   and the   property of this descriptor is  , BNNS uses the same   for the entire sequence.
- `input_descriptor`: Descriptors of the input, hidden input, and cell-state input data. For more information, see  .
- `output_descriptor`: Descriptors of the output, hidden output, and cell-state output data. For more information, see  .
- `input_gate`: The descriptor of the input gate, which uses default sigmoid activation. Use C style multidimensional array notation to order the memory pointers as  .
- `forget_gate`: The descriptor of the forget gate, which uses default sigmoid activation. Use C style multidimensional array notation to order the memory pointers as  .
- `candidate_gate`: The descriptor of the candidate gate, which uses default tanh activation. Use C style multidimensional array notation to order the memory pointers as  .
- `output_gate`: The descriptor of the output gate, which uses default sigmoid activation. Use C style multidimensional array notation to order the memory pointers as  .
- `hidden_activation`: Hidden activation function, which uses default tanh activation.

## See Also

- [init()](bnnslayerparameterslstm/init.md)
  Returns a new long short-term memory (LSTM) parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslstm/init(input_size:hidden_size:batch_size:num_layers:seq_len:dropout:lstm_flags:sequence_descriptor:input_descriptor:output_descriptor:input_gate:forget_gate:candidate_gate:output_gate:hidden_activation:))*