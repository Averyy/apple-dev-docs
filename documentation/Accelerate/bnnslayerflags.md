# BNNSLayerFlags

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Options that control the behavior of a long short-term memory (LSTM) layer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSLayerFlags
```

```c
typedef enum { ... } BNNSLayerFlags;
```

## Topics

### LSTM Layer Flags
- [var rawValue: UInt32](./bnnslayerflags/rawvalue.md)
- [init(UInt32)](./bnnslayerflags/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnslayerflags/init%28rawvalue%29.md)
- [var BNNSLayerFlagsLSTMBidirectional: BNNSLayerFlags](./bnnslayerflagslstmbidirectional.md)
  A flag that enables bidirectional long short-term memory (LSTM).
- [var BNNSLayerFlagsLSTMDefaultActivations: BNNSLayerFlags](./bnnslayerflagslstmdefaultactivations.md)
  A flag that ignores the specified gate activations and instructs the operation to use default activations.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Recurrent layers
- [Using Long Short-Term Memory Layers (LSTM)](./using-long-short-term-memory-layers-lstm.md)
  Add long short-term memory (LSTM) layers to recurrent neural networks to avoid long-term dependency problems.
- [struct BNNSLSTMDataDescriptor](./bnnslstmdatadescriptor.md)
  A structure that contains the input-output, hidden, and cell state n-dimensional array descriptors for a long short-term memory (LSTM) layer.
- [struct BNNSLSTMGateDescriptor](./bnnslstmgatedescriptor.md)
  A structure that describes a long short-term memory (LSTM) gate layer.
- [struct BNNSLayerParametersLSTM](./bnnslayerparameterslstm.md)
  A structure that contains the parameters of a long short-term memory (LSTM) layer.
- [func BNNSComputeLSTMTrainingCacheCapacity(UnsafePointer<BNNSLayerParametersLSTM>) -> Int](./bnnscomputelstmtrainingcachecapacity%28_%29.md)
  Returns the minimum bytes capacity of the training cache buffer a long short-term memory (LSTM) layer uses when it’s applied.
- [func BNNSDirectApplyLSTMBatchTrainingCaching(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeMutableRawPointer?, Int) -> Int32](./bnnsdirectapplylstmbatchtrainingcaching%28_,_,_,_%29.md)
  Applies a long short-term memory (LSTM) layer directly to an input.
- [func BNNSDirectApplyLSTMBatchBackward(UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSLayerParametersLSTM>, UnsafePointer<BNNSFilterParameters>?, UnsafeRawPointer?, Int) -> Int32](./bnnsdirectapplylstmbatchbackward%28_,_,_,_,_%29.md)
  Applies a long short-term memory (LSTM) filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerflags)*