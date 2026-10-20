# init(descriptor:data:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor with the descriptor and data you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor tensorDescriptor: MLCTensorDescriptor, data: MLCTensorData)
```

```objc
+ (instancetype) tensorWithDescriptor:(MLCTensorDescriptor *) tensorDescriptor data:(MLCTensorData *) data;
```

## Parameters

- `tensorDescriptor`: An object you use to configure the tensor.
- `data`: The tensor data.

## See Also

### Creating Tensors with Descriptors
- [convenience init(descriptor: MLCTensorDescriptor)](./init%28descriptor%29.md)
  Creates a tensor without data, using the descriptor you specify.
- [convenience init(descriptor: MLCTensorDescriptor, fillWithData: NSNumber)](./init%28descriptor,fillwithdata%29.md)
  Creates a tensor with the descriptor and scalar value you specify.
- [convenience init(descriptor: MLCTensorDescriptor, randomInitializerType: MLCRandomInitializerType)](./init%28descriptor,randominitializertype%29.md)
  Creates a tensor with the descriptor and random initializer type you specify.
- [class MLCTensorDescriptor](../mlctensordescriptor.md)
  A configuration object you use to create a tensor.
- [enum MLCDataType](../mlcdatatype.md)
  A tensor data type.
- [class MLCTensorData](../mlctensordata.md)
  An encapsulation of the memory that tensor data uses.
- [enum MLCRandomInitializerType](../mlcrandominitializertype.md)
  An initializer type you use to create a tensor with random data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/init(descriptor:data:))*