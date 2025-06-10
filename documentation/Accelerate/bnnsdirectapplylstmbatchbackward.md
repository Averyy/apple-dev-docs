# BNNSDirectApplyLSTMBatchBackward(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a long short-term memory (LSTM) filter backward to generate gradients.

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
func BNNSDirectApplyLSTMBatchBackward(_ layer_params: UnsafePointer<BNNSLayerParametersLSTM>, _ layer_delta_params: UnsafePointer<BNNSLayerParametersLSTM>, _ filter_params: UnsafePointer<BNNSFilterParameters>?, _ training_cache_ptr: UnsafeRawPointer?, _ training_cache_capacity: Int) -> Int32
```

## Parameters

- `layer_params`: The LSTM layer parameters.
- `layer_delta_params`: The LSTM layer delta parameters.
- `filter_params`: Filter runtime parameters.
- `training_cache_ptr`: A pointer to the training cache buffer.
- `training_cache_capacity`: The minimum bytes capacity of the training cache buffer as computed by the training cache capacity function.

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
- [func BNNSComputeLSTMTrainingCacheCapacity(UnsafePointer<BNNSLayerParametersLSTM>) -> Int](bnnscomputelstmtrainingcachecapacity(_:).md)
  Returns the minimum bytes capacity of the training cache buffer a long short-term memory (LSTM) layer uses when it’s applied.
- [func BNNSDirectApplyLSTMBatchTrainingCaching(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeMutableRawPointer?, Int) -> Int32](bnnsdirectapplylstmbatchtrainingcaching(_:_:_:_:).md)
  Applies a long short-term memory (LSTM) layer directly to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdirectapplylstmbatchbackward(_:_:_:_:_:))*