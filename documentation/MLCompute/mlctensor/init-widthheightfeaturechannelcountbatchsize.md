# init(width:height:featureChannelCount:batchSize:)

**Framework**: ML Compute  
**Kind**: init

Creates a tensor without data, with the sizes and number of feature channels you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int)
```

#### Discussion

The tensor data type is [`MLCDataType.float32`](mlcdatatype/float32.md).

## Parameters

- `width`: The tensor width.
- `height`: The tensor height.
- `featureChannelCount`: The number of feature channels.
- `batchSize`: The tensor batch size.

## See Also

- [convenience init(shape: [Int])](mlctensor/init(shape:).md)
  Creates a tensor without data, with the shape you specify.
- [convenience init(shape: [Int], dataType: MLCDataType)](mlctensor/init(shape:datatype:).md)
  Creates a tensor without data, with the shape and data type you specify.
- [convenience init(shape: [Int], data: MLCTensorData, dataType: MLCDataType)](mlctensor/init(shape:data:datatype:).md)
  Creates a tensor with the shape, data, and data type you specify.
- [convenience init(shape: [Int], fillWithData: NSNumber, dataType: MLCDataType)](mlctensor/init(shape:fillwithdata:datatype:).md)
  Creates a tensor with the shape, scalar value, and data type you specify.
- [convenience init(shape: [Int], randomInitializerType: MLCRandomInitializerType)](mlctensor/init(shape:randominitializertype:).md)
  Creates a tensor with the shape and random initializer type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData)](mlctensor/init(width:height:featurechannelcount:batchsize:data:).md)
  Creates a tensor with the sizes, number of feature channels, and data you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData, dataType: MLCDataType)](mlctensor/init(width:height:featurechannelcount:batchsize:data:datatype:).md)
  Creates a tensor with the sizes, number of feature channels, data, and data type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, fillWithData: Float, dataType: MLCDataType)](mlctensor/init(width:height:featurechannelcount:batchsize:fillwithdata:datatype:).md)
  Creates a tensor with the sizes and number of feature channels, and filled with the data and type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](mlctensor/init(width:height:featurechannelcount:batchsize:randominitializertype:).md)
  Creates a tensor with the sizes, number of feature channels, and random data using the random initializer type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/init(width:height:featurechannelcount:batchsize:))*