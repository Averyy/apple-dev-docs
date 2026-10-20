# BNNSComputeLSTMTrainingCacheCapacity(_:)

**Framework**: Accelerate  
**Kind**: func

Returns the minimum bytes capacity of the training cache buffer a long short-term memory (LSTM) layer uses when it’s applied.

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
func BNNSComputeLSTMTrainingCacheCapacity(_ layer_params: UnsafePointer<BNNSLayerParametersLSTM>) -> Int
```

## Mentions

- [Using Long Short-Term Memory Layers (LSTM)](using-long-short-term-memory-layers-lstm.md)

## Parameters

- `layer_params`: The LSTM layer parameters.

## See Also

- [Using Long Short-Term Memory Layers (LSTM)](using-long-short-term-memory-layers-lstm.md)
  Add long short-term memory (LSTM) layers to recurrent neural networks to avoid long-term dependency problems.
- [struct BNNSLSTMDataDescriptor](bnnslstmdatadescriptor.md)
  A structure that contains the input-output, hidden, and cell state n-dimensional array descriptors for a long short-term memory (LSTM) layer.
- [struct BNNSLSTMGateDescriptor](bnnslstmgatedescriptor.md)
  A structure that describes a long short-term memory (LSTM) gate layer.
- [struct BNNSLayerFlags](bnnslayerflags.md)
  Options that control the behavior of a long short-term memory (LSTM) layer.
- [struct BNNSLayerParametersLSTM](bnnslayerparameterslstm.md)
  A structure that contains the parameters of a long short-term memory (LSTM) layer.
- [func BNNSDirectApplyLSTMBatchTrainingCaching(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeMutableRawPointer?, Int) -> Int32](bnnsdirectapplylstmbatchtrainingcaching(_:_:_:_:).md)
  Applies a long short-term memory (LSTM) layer directly to an input.
- [func BNNSDirectApplyLSTMBatchBackward(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeRawPointer?, Int) -> Int32](bnnsdirectapplylstmbatchbackward(_:_:_:_:_:).md)
  Applies a long short-term memory (LSTM) filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnscomputelstmtrainingcachecapacity(_:))*