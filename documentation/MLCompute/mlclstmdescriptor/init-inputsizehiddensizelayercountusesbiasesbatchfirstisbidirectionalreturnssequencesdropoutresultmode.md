# init(inputSize:hiddenSize:layerCount:usesBiases:batchFirst:isBidirectional:returnsSequences:dropout:resultMode:)

**Framework**: ML Compute  
**Kind**: init

Creates a descriptor with the number of features and layers, dropout, and options for use of biases, batch order, return sequences, bidirectionality, and expected tensors you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, returnsSequences: Bool, dropout: Float, resultMode: MLCLSTMResultMode)
```

## Parameters

- `inputSize`: The number of expected features in the input.
- `hiddenSize`: The number of features in the hidden state.
- `layerCount`: The number of recurrent layers.
- `usesBiases`: A Boolean that indicates whether you use bias weights. The default value is  .
- `batchFirst`: A Boolean that indicates whether the first index of the input and output shape contains the batch size. The default value is  .
- `isBidirectional`: A Boolean that indicates whether the layer becomes bidirectional. The default value is  .
- `returnsSequences`: A Boolean that indicates whether the layer returns output for all sequences, or if  , returns output for only the last sequences. The default value is  .
- `dropout`: The dropout probability rate.
- `resultMode`: The expected result mode for the layer. The default value is  .

## See Also

- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int)](mlclstmdescriptor/init(inputsize:hiddensize:layercount:).md)
  Creates a batch first LSTM descriptor with the input size and number of layers you specify.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, isBidirectional: Bool, dropout: Float)](mlclstmdescriptor/init(inputsize:hiddensize:layercount:usesbiases:isbidirectional:dropout:).md)
  Creates a batch first LSTM descriptor with bias and bidirectional options you specify.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, dropout: Float)](mlclstmdescriptor/init(inputsize:hiddensize:layercount:usesbiases:batchfirst:isbidirectional:dropout:).md)
  Creates a batch first LSTM descriptor that allows you to indicate whether the input and output shape is batch first.
- [convenience init(inputSize: Int, hiddenSize: Int, layerCount: Int, usesBiases: Bool, batchFirst: Bool, isBidirectional: Bool, returnsSequences: Bool, dropout: Float)](mlclstmdescriptor/init(inputsize:hiddensize:layercount:usesbiases:batchfirst:isbidirectional:returnssequences:dropout:).md)
  Creates a batch first LSTM descriptor that allows you to indicate whether the layer returns output for all sequences, or output for only the last sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmdescriptor/init(inputsize:hiddensize:layercount:usesbiases:batchfirst:isbidirectional:returnssequences:dropout:resultmode:))*