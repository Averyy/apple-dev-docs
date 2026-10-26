# tensorWithShape:data:dataType:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a tensor with the shape, data, and data type you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

## Declaration

```objc
+ (instancetype) tensorWithShape:(NSArray<NSNumber *> *) shape data:(MLCTensorData *) data dataType:(MLCDataType) dataType;
```

#### Return Value

A tensor.

## Parameters

- `shape`: An array that contains the sizes of each dimension.
- `data`: The tensor data.
- `dataType`: The tensor data type.

## See Also

### Creating Tensors by Specifying Shape
- [+ tensorWithShape:](./tensorwithshape_.md)
  Creates a tensor without data, with the shape you specify.
- [+ tensorWithShape:dataType:](./tensorwithshape_datatype_.md)
  Creates a tensor without data, with the shape and data type you specify.
- [+ tensorWithShape:fillWithData:dataType:](./tensorwithshape_fillwithdata_datatype_.md)
  Creates a tensor with the shape, scalar value, and data type you specify.
- [+ tensorWithShape:randomInitializerType:](./tensorwithshape_randominitializertype_.md)
  Creates a tensor with the shape and random initializer type you specify.
- [+ tensorWithShape:randomInitializerType:dataType:](./tensorwithshape_randominitializertype_datatype_.md)
  Creates a tensor with the shape, random initializer, and data type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int)](./init%28width,height,featurechannelcount,batchsize%29.md)
  Creates a tensor without data, with the sizes and number of feature channels you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData)](./init%28width,height,featurechannelcount,batchsize,data%29.md)
  Creates a tensor with the sizes, number of feature channels, and data you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData, dataType: MLCDataType)](./init%28width,height,featurechannelcount,batchsize,data,datatype%29.md)
  Creates a tensor with the sizes, number of feature channels, data, and data type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, fillWithData: Float, dataType: MLCDataType)](./init%28width,height,featurechannelcount,batchsize,fillwithdata,datatype%29.md)
  Creates a tensor with the sizes and number of feature channels, and filled with the data and type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](./init%28width,height,featurechannelcount,batchsize,randominitializertype%29.md)
  Creates a tensor with the sizes, number of feature channels, and random data using the random initializer type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/tensorwithshape:data:datatype:)*