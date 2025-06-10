# Using Long Short-Term Memory Layers (LSTM)

**Framework**: Accelerate

Add long short-term memory (LSTM) layers to recurrent neural networks to avoid long-term dependency problems.

#### Overview

An LSTM layer consists of four gates that manipulate cell-state data:

The following figure illustrates the components of an LSTM layer. The inputs are the cell-state (c), the hidden state (h), and the input data (x). The outputs are the updated cell-state (c) and hidden state (h):

![Visualization of an LSTM layer showing the forget gate, input gate, candidate gate, and output gate as boxes that contain a curve that represents the gate’s activation function. The cell state is multiplied by the output of the forget gate, and then added to the product of the outputs of the input gate and candidate gate.](https://docs-assets.developer.apple.com/published/6565aaa85ca2568104335ed3b51b8ac5/media-3633106%402x.png)

Note that the default activation function for the forget, input, and output gates is [`sigmoid`](bnnsactivationfunction/sigmoid.md); the default activation function for the candidate gate is [`tanh`](bnnsactivationfunction/tanh.md).

BNNS provides direct apply functions for forward and backward LSTM passes, that is, you don’t need to create an explicit LSTM layer. Rather, you create descriptors of the input, output, and gates to create a parameters structure, and pass the parameters structure to the apply function.

The input and out descriptors require n-dimensional array descriptors for the data, hidden state, and cell-state:

```swift
let inputDescriptor = BNNSLSTMDataDescriptor(data_desc: inputDataDescriptor,
                                             hidden_desc: inputHiddenDescriptor,
                                             cell_state_desc: inputCellStateDescriptor)

let outputDescriptor = BNNSLSTMDataDescriptor(data_desc: outputDataDescriptor,
                                              hidden_desc: outputHiddenDescriptor,
                                              cell_state_desc: outputCellStateDescriptor)
```

Define each gate by specifying input, hidden, and cell-state weights, and bias:

```swift
let forgetGate = BNNSLSTMGateDescriptor(iw_desc: (forgetGateInputWeightsDescriptor,
                                                  forgetGateInputWeightsDescriptor),
                                        hw_desc: forgetGateHiddenWeightsDescriptor,
                                        cw_desc: forgetGateCellStateWeightsDescriptor,
                                        b_desc: forgetGateBiasDescriptor,
                                        activation: BNNSActivation(function: .sigmoid))

let inputGate = BNNSLSTMGateDescriptor(iw_desc: (inputGateInputWeightsDescriptor,
                                                 inputGateInputWeightsDescriptor),
                                       hw_desc: inputGateHiddenWeightsDescriptor,
                                       cw_desc: inputGateCellStateWeightsDescriptor,
                                       b_desc: inputGateBiasDescriptor,
                                       activation: BNNSActivation(function: .sigmoid))

let candidateGate = BNNSLSTMGateDescriptor(iw_desc: (candidateGateInputWeightsDescriptor,
                                                     candidateGateInputWeightsDescriptor),
                                           hw_desc: candidateGateHiddenWeightsDescriptor,
                                           cw_desc: candidateGateCellStateWeightsDescriptor,
                                           b_desc: candidateGateBiasDescriptor,
                                           activation: BNNSActivation(function: .tanh))

let outputGate = BNNSLSTMGateDescriptor(iw_desc: (outputGateInputWeightsDescriptor,
                                                  outputGateInputWeightsDescriptor),
                                        hw_desc: outputGateHiddenWeightsDescriptor,
                                        cw_desc: outputGateCellStateWeightsDescriptor,
                                        b_desc: outputGateBiasDescriptor,
                                        activation: BNNSActivation(function: .sigmoid))
```

The following code shows how each gate computes its output:

```objc
 for (size_t o = 0; o < iw_desc.size[1]; o++)
 {
  float res = bias[o]; // init with bias value
  for (size_t i = 0; i < iw_desc.size[0]; i++) // matrix vector multiply
   res += input[i] * input_weights[o][i];
  for (size_t i = 0; i < hw_desc.size[0]; i++) // matrix vector multiply
   res += hidden[i] * hidden_weights[o][i];
  for (size_t i = 0; i < cw_desc.size[0]; i++) // matrix vector multiply
   res += cell[i] * cell_weights[o][i];
  out[i] = activation.func(res); // apply activation function
 }
```

Give the descriptors for the input, output, and gates, you’re ready to create the parameters structure:

```swift
var layerParams = BNNSLayerParametersLSTM(input_size:  ... ,
                                          hidden_size:  ... ,
                                          batch_size: ... ,
                                          num_layers: ... ,
                                          seq_len: ... ,
                                          dropout: ... ,
                                          lstm_flags: BNNSLayerFlagsLSTMDefaultActivations.rawValue,
                                          sequence_descriptor: BNNSNDArrayDescriptor(),
                                          input_descriptor: inputDescriptor,
                                          output_descriptor: outputDescriptor,
                                          input_gate: inputGate,
                                          forget_gate: forgetGate,
                                          candidate_gate: candidateGate,
                                          output_gate: outputGate,
                                          hidden_activation: BNNSActivation(function: .identity))
```

LSTM provides the option to define a training cache that stores intermediate results to accelerate backward computation. Use [`BNNSComputeLSTMTrainingCacheCapacity(_:)`](bnnscomputelstmtrainingcachecapacity(_:).md) to compute the size, in bytes, of the training cache:

```swift
let trainingCacheBufferBytes = BNNSComputeLSTMTrainingCacheCapacity(&layerParams)

let trainingCache = UnsafeMutableRawPointer.allocate(byteCount: trainingCacheBufferBytes,
                                                     alignment: 1)
defer {
    trainingCache.deallocate()
}
```

Finally, call [`BNNSDirectApplyLSTMBatchTrainingCaching(_:_:_:_:)`](bnnsdirectapplylstmbatchtrainingcaching(_:_:_:_:).md) to apply the LSTM layer:

```swift
BNNSDirectApplyLSTMBatchTrainingCaching(&layerParams,
                                        nil,
                                        trainingCache,
                                        trainingCacheBufferBytes)
```

## See Also

- [struct BNNSLSTMDataDescriptor](bnnslstmdatadescriptor.md)
  A structure that contains the input-output, hidden, and cell state n-dimensional array descriptors for a long short-term memory (LSTM) layer.
- [struct BNNSLSTMGateDescriptor](bnnslstmgatedescriptor.md)
  A structure that describes a long short-term memory (LSTM) gate layer.
- [struct BNNSLayerFlags](bnnslayerflags.md)
  Options that control the behavior of a long short-term memory (LSTM) layer.
- [struct BNNSLayerParametersLSTM](bnnslayerparameterslstm.md)
  A structure that contains the parameters of a long short-term memory (LSTM) layer.
- [func BNNSComputeLSTMTrainingCacheCapacity(UnsafePointer<BNNSLayerParametersLSTM>) -> Int](bnnscomputelstmtrainingcachecapacity(_:).md)
  Returns the minimum bytes capacity of the training cache buffer a long short-term memory (LSTM) layer uses when it’s applied.
- [func BNNSDirectApplyLSTMBatchTrainingCaching(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeMutableRawPointer?, Int) -> Int32](bnnsdirectapplylstmbatchtrainingcaching(_:_:_:_:).md)
  Applies a long short-term memory (LSTM) layer directly to an input.
- [func BNNSDirectApplyLSTMBatchBackward(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeRawPointer?, Int) -> Int32](bnnsdirectapplylstmbatchbackward(_:_:_:_:_:).md)
  Applies a long short-term memory (LSTM) filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/using-long-short-term-memory-layers-lstm)*