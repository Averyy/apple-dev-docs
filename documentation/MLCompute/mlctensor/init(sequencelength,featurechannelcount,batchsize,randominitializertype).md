# init(sequenceLength:featureChannelCount:batchSize:randomInitializerType:)

**Framework**: ML Compute  
**Kind**: init

Creates a tensor with the sequence length, number of feature channels, batch size, and random initializer type you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)
```

## Parameters

- `sequenceLength`: The length of sequences stored in the tensor.
- `featureChannelCount`: The number of feature channels.
- `batchSize`: The tensor batch size.
- `randomInitializerType`: The random initializer type you use to generate random data.

## See Also

- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int)](mlctensor/init(sequencelength:featurechannelcount:batchsize:).md)
  Creates a tensor without data, with the sequence length, number of feature channels, and batch size you specify.
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData?)](mlctensor/init(sequencelength:featurechannelcount:batchsize:data:).md)
  Creates a tensor with the sequence length, number of feature channels, batch size, and data you specify.
- [convenience init?(sequenceLengths: [Int], sortedSequences: Bool, featureChannelCount: Int, batchSize: Int, data: MLCTensorData?)](mlctensor/init(sequencelengths:sortedsequences:featurechannelcount:batchsize:data:).md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and data you specify.
- [convenience init?(sequenceLengths: [Int], sortedSequences: Bool, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](mlctensor/init(sequencelengths:sortedsequences:featurechannelcount:batchsize:randominitializertype:).md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and random initializer type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/init(sequencelength:featurechannelcount:batchsize:randominitializertype:))*