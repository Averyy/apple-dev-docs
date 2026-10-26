# init(width:height:featureChannelCount:batchSize:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor without data, with the sizes and number of feature channels you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int)
```

```objc
+ (instancetype) tensorWithWidth:(NSUInteger) width height:(NSUInteger) height featureChannelCount:(NSUInteger) featureChannelCount batchSize:(NSUInteger) batchSize;
```

#### Discussion

The tensor data type is [`MLCDataType.float32`](../mlcdatatype/float32.md).

## Parameters

- `width`: The tensor width.
- `height`: The tensor height.
- `featureChannelCount`: The number of feature channels.
- `batchSize`: The tensor batch size.

## See Also

### Creating Tensors by Specifying Shape
- [convenience init(shape: [Int])](./init%28shape%29.md)
  Creates a tensor without data, with the shape you specify.
- [convenience init(shape: [Int], dataType: MLCDataType)](./init%28shape,datatype%29.md)
  Creates a tensor without data, with the shape and data type you specify.
- [convenience init(shape: [Int], data: MLCTensorData, dataType: MLCDataType)](./init%28shape,data,datatype%29.md)
  Creates a tensor with the shape, data, and data type you specify.
- [convenience init(shape: [Int], fillWithData: NSNumber, dataType: MLCDataType)](./init%28shape,fillwithdata,datatype%29.md)
  Creates a tensor with the shape, scalar value, and data type you specify.
- [convenience init(shape: [Int], randomInitializerType: MLCRandomInitializerType)](./init%28shape,randominitializertype%29.md)
  Creates a tensor with the shape and random initializer type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData)](./init%28width,height,featurechannelcount,batchsize,data%29.md)
  Creates a tensor with the sizes, number of feature channels, and data you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData, dataType: MLCDataType)](./init%28width,height,featurechannelcount,batchsize,data,datatype%29.md)
  Creates a tensor with the sizes, number of feature channels, data, and data type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, fillWithData: Float, dataType: MLCDataType)](./init%28width,height,featurechannelcount,batchsize,fillwithdata,datatype%29.md)
  Creates a tensor with the sizes and number of feature channels, and filled with the data and type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](./init%28width,height,featurechannelcount,batchsize,randominitializertype%29.md)
  Creates a tensor with the sizes, number of feature channels, and random data using the random initializer type you specify.
- [+ tensorWithShape:](./tensorwithshape_.md)
  Creates a tensor without data, with the shape you specify.
- [+ tensorWithShape:dataType:](./tensorwithshape_datatype_.md)
  Creates a tensor without data, with the shape and data type you specify.
- [+ tensorWithShape:data:dataType:](./tensorwithshape_data_datatype_.md)
  Creates a tensor with the shape, data, and data type you specify.
- [+ tensorWithShape:fillWithData:dataType:](./tensorwithshape_fillwithdata_datatype_.md)
  Creates a tensor with the shape, scalar value, and data type you specify.
- [+ tensorWithShape:randomInitializerType:](./tensorwithshape_randominitializertype_.md)
  Creates a tensor with the shape and random initializer type you specify.
- [+ tensorWithShape:randomInitializerType:dataType:](./tensorwithshape_randominitializertype_datatype_.md)
  Creates a tensor with the shape, random initializer, and data type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/init(width:height:featurechannelcount:batchsize:))*