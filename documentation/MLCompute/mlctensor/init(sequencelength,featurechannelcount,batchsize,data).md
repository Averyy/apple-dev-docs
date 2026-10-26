# init(sequenceLength:featureChannelCount:batchSize:data:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor with the sequence length, number of feature channels, batch size, and data you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData?)
```

```objc
+ (instancetype) tensorWithSequenceLength:(NSUInteger) sequenceLength featureChannelCount:(NSUInteger) featureChannelCount batchSize:(NSUInteger) batchSize data:(MLCTensorData *) data;
```

## Parameters

- `sequenceLength`: The length of sequences stored in the tensor.
- `featureChannelCount`: The number of feature channels.
- `batchSize`: The tensor batch size.
- `data`: The tensor data.

## See Also

### Creating Tensors by Specifying Sequence Lengths
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int)](./init%28sequencelength,featurechannelcount,batchsize%29.md)
  Creates a tensor without data, with the sequence length, number of feature channels, and batch size you specify.
- [convenience init?(sequenceLengths: [Int], sortedSequences: Bool, featureChannelCount: Int, batchSize: Int, data: MLCTensorData?)](./init%28sequencelengths,sortedsequences,featurechannelcount,batchsize,data%29.md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and data you specify.
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](./init%28sequencelength,featurechannelcount,batchsize,randominitializertype%29.md)
  Creates a tensor with the sequence length, number of feature channels, batch size, and random initializer type you specify.
- [convenience init?(sequenceLengths: [Int], sortedSequences: Bool, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](./init%28sequencelengths,sortedsequences,featurechannelcount,batchsize,randominitializertype%29.md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and random initializer type you specify.
- [+ tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:data:](./tensorwithsequencelengths_sortedsequences_featurechannelcount_batchsize_data_.md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and data you specify.
- [+ tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:randomInitializerType:](./tensorwithsequencelengths_sortedsequences_featurechannelcount_batchsize_randominitializertype_.md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and random initializer type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/init(sequencelength:featurechannelcount:batchsize:data:))*