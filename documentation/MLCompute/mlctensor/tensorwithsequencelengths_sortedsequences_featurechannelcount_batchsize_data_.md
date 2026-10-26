# tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:data:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and data you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

## Declaration

```objc
+ (instancetype) tensorWithSequenceLengths:(NSArray<NSNumber *> *) sequenceLengths sortedSequences:(BOOL) sortedSequences featureChannelCount:(NSUInteger) featureChannelCount batchSize:(NSUInteger) batchSize data:(MLCTensorData *) data;
```

#### Return Value

A tensor.

## Parameters

- `sequenceLengths`: An array that contains the lengths of sequences stored in the tensor.
- `sortedSequences`: A Boolean that indicates whether you provide the sequence lengths sorted in descending order.
- `featureChannelCount`: The number of feature channels.
- `batchSize`: The tensor batch size.
- `data`: The tensor data.

## See Also

### Creating Tensors by Specifying Sequence Lengths
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int)](./init%28sequencelength,featurechannelcount,batchsize%29.md)
  Creates a tensor without data, with the sequence length, number of feature channels, and batch size you specify.
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData?)](./init%28sequencelength,featurechannelcount,batchsize,data%29.md)
  Creates a tensor with the sequence length, number of feature channels, batch size, and data you specify.
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](./init%28sequencelength,featurechannelcount,batchsize,randominitializertype%29.md)
  Creates a tensor with the sequence length, number of feature channels, batch size, and random initializer type you specify.
- [+ tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:randomInitializerType:](./tensorwithsequencelengths_sortedsequences_featurechannelcount_batchsize_randominitializertype_.md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and random initializer type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/tensorwithsequencelengths:sortedsequences:featurechannelcount:batchsize:data:)*