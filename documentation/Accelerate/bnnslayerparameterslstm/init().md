# init()

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new long short-term memory (LSTM) parameters structure.

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
init()
```

## Discussion

This initializer returns a new structure with all numeric properties set to `0`.

## See Also

### Initializers
- [init(input_size: Int, hidden_size: Int, batch_size: Int, num_layers: Int, seq_len: Int, dropout: Float, lstm_flags: UInt32, sequence_descriptor: BNNSNDArrayDescriptor, input_descriptor: BNNSLSTMDataDescriptor, output_descriptor: BNNSLSTMDataDescriptor, input_gate: BNNSLSTMGateDescriptor, forget_gate: BNNSLSTMGateDescriptor, candidate_gate: BNNSLSTMGateDescriptor, output_gate: BNNSLSTMGateDescriptor, hidden_activation: BNNSActivation)](./init%28input_size,hidden_size,batch_size,num_layers,seq_len,dropout,lstm_flags,sequence_descriptor,input_descriptor,output_descriptor,input_gate,forget_gate,candidate_gate,output_gate,hidden_activation%29.md)
  Returns a new long short-term memory (LSTM) parameters structure from the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslstm/init())*