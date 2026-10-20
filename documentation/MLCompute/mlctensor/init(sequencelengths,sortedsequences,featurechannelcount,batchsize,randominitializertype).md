# init(sequenceLengths:sortedSequences:featureChannelCount:batchSize:randomInitializerType:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and random initializer type you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init?(sequenceLengths: [Int], sortedSequences: Bool, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)
```

## Parameters

- `sequenceLengths`: An array that contains the variable lengths of sequences stored in the tensor.
- `sortedSequences`: A Boolean that indicates whether you provide the sequence lengths sorted in descending order.
- `featureChannelCount`: The number of feature channels.
- `batchSize`: The tensor batch size.
- `randomInitializerType`: The random initializer type you use to generate random data.

## See Also

### Creating Tensors by Specifying Sequence Lengths
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int)](./init%28sequencelength,featurechannelcount,batchsize%29.md)
  Creates a tensor without data, with the sequence length, number of feature channels, and batch size you specify.
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData?)](./init%28sequencelength,featurechannelcount,batchsize,data%29.md)
  Creates a tensor with the sequence length, number of feature channels, batch size, and data you specify.
- [convenience init?(sequenceLengths: [Int], sortedSequences: Bool, featureChannelCount: Int, batchSize: Int, data: MLCTensorData?)](./init%28sequencelengths,sortedsequences,featurechannelcount,batchsize,data%29.md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and data you specify.
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](./init%28sequencelength,featurechannelcount,batchsize,randominitializertype%29.md)
  Creates a tensor with the sequence length, number of feature channels, batch size, and random initializer type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/init(sequencelengths:sortedsequences:featurechannelcount:batchsize:randominitializertype:))*