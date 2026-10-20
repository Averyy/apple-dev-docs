# BNNSDirectApplyLSTMBatchTrainingCaching(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a long short-term memory (LSTM) layer directly to an input.

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
func BNNSDirectApplyLSTMBatchTrainingCaching(_ layer_params: UnsafePointer<BNNSLayerParametersLSTM>, _ filter_params: UnsafePointer<BNNSFilterParameters>?, _ training_cache_ptr: UnsafeMutableRawPointer?, _ training_cache_capacity: Int) -> Int32
```

```c
int BNNSDirectApplyLSTMBatchTrainingCaching(const BNNSLayerParametersLSTM *layer_params, const BNNSFilterParameters *filter_params, void *training_cache_ptr, const size_t training_cache_capacity);
```

## Mentions

- [Using Long Short-Term Memory Layers (LSTM)](./using-long-short-term-memory-layers-lstm.md)

## Parameters

- `layer_params`: The LSTM layer parameters.
- `filter_params`: Filter runtime parameters.
- `training_cache_ptr`: A pointer to the training cache buffer.
- `training_cache_capacity`: The minimum bytes capacity of the training cache buffer as computed by the training cache capacity function.

## See Also

### Recurrent layers
- [Using Long Short-Term Memory Layers (LSTM)](./using-long-short-term-memory-layers-lstm.md)
  Add long short-term memory (LSTM) layers to recurrent neural networks to avoid long-term dependency problems.
- [struct BNNSLSTMDataDescriptor](./bnnslstmdatadescriptor.md)
  A structure that contains the input-output, hidden, and cell state n-dimensional array descriptors for a long short-term memory (LSTM) layer.
- [struct BNNSLSTMGateDescriptor](./bnnslstmgatedescriptor.md)
  A structure that describes a long short-term memory (LSTM) gate layer.
- [struct BNNSLayerFlags](./bnnslayerflags.md)
  Options that control the behavior of a long short-term memory (LSTM) layer.
- [struct BNNSLayerParametersLSTM](./bnnslayerparameterslstm.md)
  A structure that contains the parameters of a long short-term memory (LSTM) layer.
- [func BNNSComputeLSTMTrainingCacheCapacity(UnsafePointer<BNNSLayerParametersLSTM>) -> Int](./bnnscomputelstmtrainingcachecapacity%28_%29.md)
  Returns the minimum bytes capacity of the training cache buffer a long short-term memory (LSTM) layer uses when it’s applied.
- [func BNNSDirectApplyLSTMBatchBackward(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeRawPointer?, Int) -> Int32](./bnnsdirectapplylstmbatchbackward%28_,_,_,_,_%29.md)
  Applies a long short-term memory (LSTM) filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdirectapplylstmbatchtrainingcaching(_:_:_:_:))*