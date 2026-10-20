# BNNSLSTMGateDescriptor

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that describes a long short-term memory (LSTM) gate layer.

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
struct BNNSLSTMGateDescriptor
```

```c
typedef struct { ... } BNNSLSTMGateDescriptor;
```

## Topics

### Initializers
- [init(iw_desc: (BNNSNDArrayDescriptor, BNNSNDArrayDescriptor), hw_desc: BNNSNDArrayDescriptor, cw_desc: BNNSNDArrayDescriptor, b_desc: BNNSNDArrayDescriptor, activation: BNNSActivation)](./bnnslstmgatedescriptor/init%28iw_desc,hw_desc,cw_desc,b_desc,activation%29.md)
  Returns a new long short-term memory (LSTM) gate descriptor structure from the specified parameters.
- [init()](./bnnslstmgatedescriptor/init%28%29.md)
  Returns a new long short-term memory (LSTM) gate descriptor structure.
### Instance Properties
- [var iw_desc: (BNNSNDArrayDescriptor, BNNSNDArrayDescriptor)](./bnnslstmgatedescriptor/iw_desc.md)
  The descriptor of the input weights.
- [var hw_desc: BNNSNDArrayDescriptor](./bnnslstmgatedescriptor/hw_desc.md)
  The descriptor of the hidden weights.
- [var cw_desc: BNNSNDArrayDescriptor](./bnnslstmgatedescriptor/cw_desc.md)
  The descriptor of the cell weights.
- [var b_desc: BNNSNDArrayDescriptor](./bnnslstmgatedescriptor/b_desc.md)
  The descriptor of the bias.
- [var activation: BNNSActivation](./bnnslstmgatedescriptor/activation.md)
  The activation function that the layer applies to the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Recurrent layers
- [Using Long Short-Term Memory Layers (LSTM)](./using-long-short-term-memory-layers-lstm.md)
  Add long short-term memory (LSTM) layers to recurrent neural networks to avoid long-term dependency problems.
- [struct BNNSLSTMDataDescriptor](./bnnslstmdatadescriptor.md)
  A structure that contains the input-output, hidden, and cell state n-dimensional array descriptors for a long short-term memory (LSTM) layer.
- [struct BNNSLayerFlags](./bnnslayerflags.md)
  Options that control the behavior of a long short-term memory (LSTM) layer.
- [struct BNNSLayerParametersLSTM](./bnnslayerparameterslstm.md)
  A structure that contains the parameters of a long short-term memory (LSTM) layer.
- [func BNNSComputeLSTMTrainingCacheCapacity(UnsafePointer<BNNSLayerParametersLSTM>) -> Int](./bnnscomputelstmtrainingcachecapacity%28_%29.md)
  Returns the minimum bytes capacity of the training cache buffer a long short-term memory (LSTM) layer uses when it’s applied.
- [func BNNSDirectApplyLSTMBatchTrainingCaching(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeMutableRawPointer?, Int) -> Int32](./bnnsdirectapplylstmbatchtrainingcaching%28_,_,_,_%29.md)
  Applies a long short-term memory (LSTM) layer directly to an input.
- [func BNNSDirectApplyLSTMBatchBackward(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeRawPointer?, Int) -> Int32](./bnnsdirectapplylstmbatchbackward%28_,_,_,_,_%29.md)
  Applies a long short-term memory (LSTM) filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslstmgatedescriptor)*