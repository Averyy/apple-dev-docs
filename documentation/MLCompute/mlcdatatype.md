# MLCDataType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A tensor data type.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCDataType
```

```c
enum MLCDataType : int32_t;
```

## Topics

### Enumeration Cases
- [MLCDataType.float16](./mlcdatatype/float16.md)
- [MLCDataType.float32](./mlcdatatype/float32.md)
- [MLCDataType.boolean](./mlcdatatype/boolean.md)
- [MLCDataType.int8](./mlcdatatype/int8.md)
- [MLCDataType.int32](./mlcdatatype/int32.md)
- [MLCDataType.int64](./mlcdatatype/int64.md)
- [MLCDataType.uint8](./mlcdatatype/uint8.md)
### Initializers
- [init?(rawValue: Int32)](./mlcdatatype/init%28rawvalue%29.md)

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
- [class MLCTensorData](./mlctensordata.md)
  An encapsulation of the memory that tensor data uses.
- [enum MLCRandomInitializerType](./mlcrandominitializertype.md)
  An initializer type you use to create a tensor with random data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdatatype)*