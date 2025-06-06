# init(shape:dataType:)

**Framework**: ML Compute  
**Kind**: init

Creates a tensor descriptor with the shape and data type you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(shape: [Int], dataType: MLCDataType)
```

## Parameters

- `shape`: The tensor shape.
- `dataType`: The tensor data type.

## See Also

- [convenience init?(shape: [Int], sequenceLengths: [Int], sortedSequences: Bool, dataType: MLCDataType)](mlctensordescriptor/init(shape:sequencelengths:sortedsequences:datatype:).md)
  Creates a tensor descriptor with the shape, variable sequence lengths, sorting indicator, and data type you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int)](mlctensordescriptor/init(width:height:featurechannelcount:batchsize:).md)
  Creates a tensor descriptor with the width and height, number of feature channels, and batch size you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, dataType: MLCDataType)](mlctensordescriptor/init(width:height:featurechannelcount:batchsize:datatype:).md)
  Creates a tensor descriptor with the width and height, number of feature channels, batch size, and data type you specify.
- [convenience init?(convolutionWeightsWithInputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](mlctensordescriptor/init(convolutionweightswithinputfeaturechannelcount:outputfeaturechannelcount:datatype:).md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [convenience init?(convolutionWeightsWithWidth: Int, height: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](mlctensordescriptor/init(convolutionweightswithwidth:height:inputfeaturechannelcount:outputfeaturechannelcount:datatype:).md)
  Creates a tensor descriptor with the sizing, number of feature channels, and data type you specify.
- [convenience init?(convolutionBiasesWithFeatureChannelCount: Int, dataType: MLCDataType)](mlctensordescriptor/init(convolutionbiaseswithfeaturechannelcount:datatype:).md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [class var maxTensorDimensions: Int](mlctensordescriptor/maxtensordimensions.md)
  The maximum number of tensor dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/init(shape:datatype:))*