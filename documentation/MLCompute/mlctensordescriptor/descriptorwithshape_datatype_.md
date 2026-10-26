# descriptorWithShape:dataType:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a tensor descriptor with the shape and data type you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) descriptorWithShape:(NSArray<NSNumber *> *) shape dataType:(MLCDataType) dataType;
```

#### Return Value

A tensor descriptor, or `nil` if initialization fails.

## Parameters

- `shape`: The tensor shape.
- `dataType`: The tensor data type.

## See Also

### Creating Tensor Descriptors
- [+ descriptorWithShape:sequenceLengths:sortedSequences:dataType:](./descriptorwithshape_sequencelengths_sortedsequences_datatype_.md)
  Creates a tensor descriptor with the shape, variable sequence lengths, sorting indicator, and data type you specify.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/descriptorwithshape:datatype:)*