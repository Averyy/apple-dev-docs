# BNNSLayerParametersLSTM

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a long short-term memory (LSTM) layer.

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
struct BNNSLayerParametersLSTM
```

#### Overview

Use a [`BNNSLayerParametersLSTM`](bnnslayerparameterslstm.md) structure to define the parameters of a long short-term memory (LSTM) operation.

## Topics

### Initializers
- [init(input_size: Int, hidden_size: Int, batch_size: Int, num_layers: Int, seq_len: Int, dropout: Float, lstm_flags: UInt32, sequence_descriptor: BNNSNDArrayDescriptor, input_descriptor: BNNSLSTMDataDescriptor, output_descriptor: BNNSLSTMDataDescriptor, input_gate: BNNSLSTMGateDescriptor, forget_gate: BNNSLSTMGateDescriptor, candidate_gate: BNNSLSTMGateDescriptor, output_gate: BNNSLSTMGateDescriptor, hidden_activation: BNNSActivation)](bnnslayerparameterslstm/init(input_size:hidden_size:batch_size:num_layers:seq_len:dropout:lstm_flags:sequence_descriptor:input_descriptor:output_descriptor:input_gate:forget_gate:candidate_gate:output_gate:hidden_activation:).md)
  Returns a new long short-term memory (LSTM) parameters structure from the specified parameters.
- [init()](bnnslayerparameterslstm/init.md)
  Returns a new long short-term memory (LSTM) parameters structure.
### Instance Properties
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
- [var output_gate: BNNSLSTMGateDescriptor](bnnslayerparameterslstm/output_gate.md)
  The descriptor of the output gate, which uses default sigmoid activation.
- [var hidden_activation: BNNSActivation](bnnslayerparameterslstm/hidden_activation.md)
  Hidden activation function, which uses default tanh activation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [Using Long Short-Term Memory Layers (LSTM)](using-long-short-term-memory-layers-lstm.md)
  Add long short-term memory (LSTM) layers to recurrent neural networks to avoid long-term dependency problems.
- [struct BNNSLSTMDataDescriptor](bnnslstmdatadescriptor.md)
  A structure that contains the input-output, hidden, and cell state n-dimensional array descriptors for a long short-term memory (LSTM) layer.
- [struct BNNSLSTMGateDescriptor](bnnslstmgatedescriptor.md)
  A structure that describes a long short-term memory (LSTM) gate layer.
- [struct BNNSLayerFlags](bnnslayerflags.md)
  Options that control the behavior of a long short-term memory (LSTM) layer.
- [func BNNSComputeLSTMTrainingCacheCapacity(UnsafePointer<BNNSLayerParametersLSTM>) -> Int](bnnscomputelstmtrainingcachecapacity(_:).md)
  Returns the minimum bytes capacity of the training cache buffer a long short-term memory (LSTM) layer uses when it’s applied.
- [func BNNSDirectApplyLSTMBatchTrainingCaching(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeMutableRawPointer?, Int) -> Int32](bnnsdirectapplylstmbatchtrainingcaching(_:_:_:_:).md)
  Applies a long short-term memory (LSTM) layer directly to an input.
- [func BNNSDirectApplyLSTMBatchBackward(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeRawPointer?, Int) -> Int32](bnnsdirectapplylstmbatchbackward(_:_:_:_:_:).md)
  Applies a long short-term memory (LSTM) filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslstm)*