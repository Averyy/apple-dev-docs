# MLCRandomInitializerType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

An initializer type you use to create a tensor with random data.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCRandomInitializerType
```

```c
enum MLCRandomInitializerType : int32_t;
```

## Topics

### Enumeration Cases
- [MLCRandomInitializerType.uniform](./mlcrandominitializertype/uniform.md)
- [MLCRandomInitializerType.glorotUniform](./mlcrandominitializertype/glorotuniform.md)
- [MLCRandomInitializerType.xavier](./mlcrandominitializertype/xavier.md)
### Initializers
- [init?(rawValue: Int32)](./mlcrandominitializertype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Tensors with Descriptors
- [convenience init(descriptor: MLCTensorDescriptor)](./mlctensor/init%28descriptor%29.md)
  Creates a tensor without data, using the descriptor you specify.
- [convenience init(descriptor: MLCTensorDescriptor, data: MLCTensorData)](./mlctensor/init%28descriptor,data%29.md)
  Creates a tensor with the descriptor and data you specify.
- [convenience init(descriptor: MLCTensorDescriptor, fillWithData: NSNumber)](./mlctensor/init%28descriptor,fillwithdata%29.md)
  Creates a tensor with the descriptor and scalar value you specify.
- [convenience init(descriptor: MLCTensorDescriptor, randomInitializerType: MLCRandomInitializerType)](./mlctensor/init%28descriptor,randominitializertype%29.md)
  Creates a tensor with the descriptor and random initializer type you specify.
- [class MLCTensorDescriptor](./mlctensordescriptor.md)
  A configuration object you use to create a tensor.
- [enum MLCDataType](./mlcdatatype.md)
  A tensor data type.
- [class MLCTensorData](./mlctensordata.md)
  An encapsulation of the memory that tensor data uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrandominitializertype)*