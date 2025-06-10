# init()

**Framework**: Accelerate  
**Kind**: init

Returns a new long short-term memory (LSTM) parameters structure.

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
init()
```

#### Discussion

This initializer returns a new structure with all numeric properties set to `0`.

## See Also

- [init(input_size: Int, hidden_size: Int, batch_size: Int, num_layers: Int, seq_len: Int, dropout: Float, lstm_flags: UInt32, sequence_descriptor: BNNSNDArrayDescriptor, input_descriptor: BNNSLSTMDataDescriptor, output_descriptor: BNNSLSTMDataDescriptor, input_gate: BNNSLSTMGateDescriptor, forget_gate: BNNSLSTMGateDescriptor, candidate_gate: BNNSLSTMGateDescriptor, output_gate: BNNSLSTMGateDescriptor, hidden_activation: BNNSActivation)](bnnslayerparameterslstm/init(input_size:hidden_size:batch_size:num_layers:seq_len:dropout:lstm_flags:sequence_descriptor:input_descriptor:output_descriptor:input_gate:forget_gate:candidate_gate:output_gate:hidden_activation:).md)
  Returns a new long short-term memory (LSTM) parameters structure from the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslstm/init())*