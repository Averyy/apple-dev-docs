# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor without data, using the descriptor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor tensorDescriptor: MLCTensorDescriptor)
```

```objc
+ (instancetype) tensorWithDescriptor:(MLCTensorDescriptor *) tensorDescriptor;
```

#### Discussion

The tensor data type is [`MLCDataType.float32`](../mlcdatatype/float32.md).

## Parameters

- `tensorDescriptor`: An object you use to configure the tensor.

## See Also

### Creating Tensors with Descriptors
- [convenience init(descriptor: MLCTensorDescriptor, data: MLCTensorData)](./init%28descriptor,data%29.md)
  Creates a tensor with the descriptor and data you specify.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/init(descriptor:))*