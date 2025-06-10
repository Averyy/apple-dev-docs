# BNNSLSTMDataDescriptor

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the input-output, hidden, and cell state n-dimensional array descriptors for a long short-term memory (LSTM) layer.

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
struct BNNSLSTMDataDescriptor
```

## Topics

### Initializers
- [init(data_desc: BNNSNDArrayDescriptor, hidden_desc: BNNSNDArrayDescriptor, cell_state_desc: BNNSNDArrayDescriptor)](bnnslstmdatadescriptor/init(data_desc:hidden_desc:cell_state_desc:).md)
  Returns a new long short-term memory (LSTM) data descriptor structure from the specified parameters.
- [init()](bnnslstmdatadescriptor/init.md)
  Returns a new long short-term memory (LSTM) data descriptor structure.
### Instance Properties
- [var data_desc: BNNSNDArrayDescriptor](bnnslstmdatadescriptor/data_desc.md)
  The descriptor of the input-output.
- [var hidden_desc: BNNSNDArrayDescriptor](bnnslstmdatadescriptor/hidden_desc.md)
  The descriptor of the hidden input-output.
- [var cell_state_desc: BNNSNDArrayDescriptor](bnnslstmdatadescriptor/cell_state_desc.md)
  The descriptor of the cell-state input-output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [Using Long Short-Term Memory Layers (LSTM)](using-long-short-term-memory-layers-lstm.md)
  Add long short-term memory (LSTM) layers to recurrent neural networks to avoid long-term dependency problems.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslstmdatadescriptor)*