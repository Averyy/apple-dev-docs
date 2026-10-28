# descriptorWithShape:sequenceLengths:sortedSequences:dataType:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a tensor descriptor with the shape, variable sequence lengths, sorting indicator, and data type you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) descriptorWithShape:(NSArray<NSNumber *> *) shape sequenceLengths:(NSArray<NSNumber *> *) sequenceLengths sortedSequences:(BOOL) sortedSequences dataType:(MLCDataType) dataType;
```

## Return Value

A tensor descriptor, or `nil` if initialization fails.

## Discussion

This initializer provides a convenient way to configure sequence tensors used by recurrent layers.

## Parameters

- `shape`: The tensor shape.
- `sequenceLengths`: An array of the variable length of sequences stored in the tensor.
- `sortedSequences`: A Boolean that indicates whether you provide the sequence lengths sorted in descending order.
- `dataType`: The tensor data type.

## See Also

### Creating Tensor Descriptors
- [+ descriptorWithShape:dataType:](./descriptorwithshape_datatype_.md)
  Creates a tensor descriptor with the shape and data type you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int)](./init%28width,height,featurechannelcount,batchsize%29.md)
  Creates a tensor descriptor with the width and height, number of feature channels, and batch size you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, dataType: MLCDataType)](./init%28width,height,featurechannelcount,batchsize,datatype%29.md)
  Creates a tensor descriptor with the width and height, number of feature channels, batch size, and data type you specify.
- [convenience init?(convolutionWeightsWithInputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](./init%28convolutionweightswithinputfeaturechannelcount,outputfeaturechannelcount,datatype%29.md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [convenience init?(convolutionWeightsWithWidth: Int, height: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](./init%28convolutionweightswithwidth,height,inputfeaturechannelcount,outputfeaturechannelcount,datatype%29.md)
  Creates a tensor descriptor with the sizing, number of feature channels, and data type you specify.
- [convenience init?(convolutionBiasesWithFeatureChannelCount: Int, dataType: MLCDataType)](./init%28convolutionbiaseswithfeaturechannelcount,datatype%29.md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [class var maxTensorDimensions: Int](./maxtensordimensions.md)
  The maximum number of tensor dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/descriptorwithshape:sequencelengths:sortedsequences:datatype:)*