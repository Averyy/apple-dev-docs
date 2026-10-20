# init(convolutionBiasesWithFeatureChannelCount:dataType:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor descriptor with the number of feature channels and data type you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(convolutionBiasesWithFeatureChannelCount featureChannelCount: Int, dataType: MLCDataType)
```

```objc
+ (instancetype) convolutionBiasesDescriptorWithFeatureChannelCount:(NSUInteger) featureChannelCount dataType:(MLCDataType) dataType;
```

#### Discussion

This initializer provides a convenient way for you to configure bias tensors.

## Parameters

- `featureChannelCount`: The number of feature channels.
- `dataType`: The tensor data type.

## See Also

### Creating Tensor Descriptors
- [convenience init?(shape: [Int], dataType: MLCDataType)](./init%28shape,datatype%29.md)
  Creates a tensor descriptor with the shape and data type you specify.
- [convenience init?(shape: [Int], sequenceLengths: [Int], sortedSequences: Bool, dataType: MLCDataType)](./init%28shape,sequencelengths,sortedsequences,datatype%29.md)
  Creates a tensor descriptor with the shape, variable sequence lengths, sorting indicator, and data type you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int)](./init%28width,height,featurechannelcount,batchsize%29.md)
  Creates a tensor descriptor with the width and height, number of feature channels, and batch size you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, dataType: MLCDataType)](./init%28width,height,featurechannelcount,batchsize,datatype%29.md)
  Creates a tensor descriptor with the width and height, number of feature channels, batch size, and data type you specify.
- [convenience init?(convolutionWeightsWithInputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](./init%28convolutionweightswithinputfeaturechannelcount,outputfeaturechannelcount,datatype%29.md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [convenience init?(convolutionWeightsWithWidth: Int, height: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](./init%28convolutionweightswithwidth,height,inputfeaturechannelcount,outputfeaturechannelcount,datatype%29.md)
  Creates a tensor descriptor with the sizing, number of feature channels, and data type you specify.
- [class var maxTensorDimensions: Int](./maxtensordimensions.md)
  The maximum number of tensor dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/init(convolutionbiaseswithfeaturechannelcount:datatype:))*