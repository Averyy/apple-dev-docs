# init(convolutionWeightsWithWidth:height:inputFeatureChannelCount:outputFeatureChannelCount:dataType:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor descriptor with the sizing, number of feature channels, and data type you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(convolutionWeightsWithWidth width: Int, height: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)
```

```objc
+ (instancetype) convolutionWeightsDescriptorWithWidth:(NSUInteger) width height:(NSUInteger) height inputFeatureChannelCount:(NSUInteger) inputFeatureChannelCount outputFeatureChannelCount:(NSUInteger) outputFeatureChannelCount dataType:(MLCDataType) dataType;
```

#### Discussion

This initializer provides a convenient way for you to configure weights tensors.

## Parameters

- `width`: The tensor width.
- `height`: The tensor height.
- `inputFeatureChannelCount`: The number of input feature channels.
- `outputFeatureChannelCount`: The number of output feature channels.
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
- [convenience init?(convolutionBiasesWithFeatureChannelCount: Int, dataType: MLCDataType)](./init%28convolutionbiaseswithfeaturechannelcount,datatype%29.md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [class var maxTensorDimensions: Int](./maxtensordimensions.md)
  The maximum number of tensor dimensions.
- [+ descriptorWithShape:dataType:](./descriptorwithshape_datatype_.md)
  Creates a tensor descriptor with the shape and data type you specify.
- [+ descriptorWithShape:sequenceLengths:sortedSequences:dataType:](./descriptorwithshape_sequencelengths_sortedsequences_datatype_.md)
  Creates a tensor descriptor with the shape, variable sequence lengths, sorting indicator, and data type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/init(convolutionweightswithwidth:height:inputfeaturechannelcount:outputfeaturechannelcount:datatype:))*