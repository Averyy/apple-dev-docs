# init(inputSize:hiddenSize:layerCount:usesBiases:batchFirst:isBidirectional:returnsSequences:dropout:resultMode:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a descriptor with the number of features and layers, dropout, and options for use of biases, batch order, return sequences, bidirectionality, and expected tensors you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, returnsSequences: Bool, dropout: Float, resultMode: MLCLSTMResultMode)
```

```objc
+ (instancetype) descriptorWithInputSize:(NSUInteger) inputSize hiddenSize:(NSUInteger) hiddenSize layerCount:(NSUInteger) layerCount usesBiases:(BOOL) usesBiases batchFirst:(BOOL) batchFirst isBidirectional:(BOOL) isBidirectional returnsSequences:(BOOL) returnsSequences dropout:(float) dropout resultMode:(MLCLSTMResultMode) resultMode;
```

## Parameters

- `inputSize`: The number of expected features in the input.
- `hiddenSize`: The number of features in the hidden state.
- `layerCount`: The number of recurrent layers.
- `usesBiases`: A Boolean that indicates whether you use bias weights. The default value is `true`.
- `batchFirst`: A Boolean that indicates whether the first index of the input and output shape contains the batch size. The default value is `true`.
- `isBidirectional`: A Boolean that indicates whether the layer becomes bidirectional. The default value is `false`.
- `returnsSequences`: A Boolean that indicates whether the layer returns output for all sequences, or if `false`, returns output for only the last sequences. The default value is `true`.
- `dropout`: The dropout probability rate.
- `resultMode`: The expected result mode for the layer. The default value is [`MLCLSTMResultMode.output`](../mlclstmresultmode/output.md).

## See Also

### Creating LSTM Descriptors
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int)](./init%28inputsize,hiddensize,layercount%29.md)
  Creates a batch first LSTM descriptor with the input size and number of layers you specify.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, isBidirectional: Bool, dropout: Float)](./init%28inputsize,hiddensize,layercount,usesbiases,isbidirectional,dropout%29.md)
  Creates a batch first LSTM descriptor with bias and bidirectional options you specify.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, dropout: Float)](./init%28inputsize,hiddensize,layercount,usesbiases,batchfirst,isbidirectional,dropout%29.md)
  Creates a batch first LSTM descriptor that allows you to indicate whether the input and output shape is batch first.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, returnsSequences: Bool, dropout: Float)](./init%28inputsize,hiddensize,layercount,usesbiases,batchfirst,isbidirectional,returnssequences,dropout%29.md)
  Creates a batch first LSTM descriptor that allows you to indicate whether the layer returns output for all sequences, or output for only the last sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmdescriptor/init(inputsize:hiddensize:layercount:usesbiases:batchfirst:isbidirectional:returnssequences:dropout:resultmode:))*