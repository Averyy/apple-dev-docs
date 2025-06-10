# BNNSLSTMGateDescriptor

**Framework**: Accelerate  
**Kind**: struct

A structure that describes a long short-term memory (LSTM) gate layer.

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
struct BNNSLSTMGateDescriptor
```

## Topics

### Initializers
- [init(iw_desc: (BNNSNDArrayDescriptor, BNNSNDArrayDescriptor), hw_desc: BNNSNDArrayDescriptor, cw_desc: BNNSNDArrayDescriptor, b_desc: BNNSNDArrayDescriptor, activation: BNNSActivation)](bnnslstmgatedescriptor/init(iw_desc:hw_desc:cw_desc:b_desc:activation:).md)
  Returns a new long short-term memory (LSTM) gate descriptor structure from the specified parameters.
- [init()](bnnslstmgatedescriptor/init.md)
  Returns a new long short-term memory (LSTM) gate descriptor structure.
### Instance Properties
- [var iw_desc: (BNNSNDArrayDescriptor, BNNSNDArrayDescriptor)](bnnslstmgatedescriptor/iw_desc.md)
  The descriptor of the input weights.
- [var hw_desc: BNNSNDArrayDescriptor](bnnslstmgatedescriptor/hw_desc.md)
  The descriptor of the hidden weights.
- [var cw_desc: BNNSNDArrayDescriptor](bnnslstmgatedescriptor/cw_desc.md)
  The descriptor of the cell weights.
- [var b_desc: BNNSNDArrayDescriptor](bnnslstmgatedescriptor/b_desc.md)
  The descriptor of the bias.
- [var activation: BNNSActivation](bnnslstmgatedescriptor/activation.md)
  The activation function that the layer applies to the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [Using Long Short-Term Memory Layers (LSTM)](using-long-short-term-memory-layers-lstm.md)
  Add long short-term memory (LSTM) layers to recurrent neural networks to avoid long-term dependency problems.
- [struct BNNSLSTMDataDescriptor](bnnslstmdatadescriptor.md)
  A structure that contains the input-output, hidden, and cell state n-dimensional array descriptors for a long short-term memory (LSTM) layer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslstmgatedescriptor)*