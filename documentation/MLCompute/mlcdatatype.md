# MLCDataType

**Framework**: ML Compute  
**Kind**: enum

A tensor data type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCDataType
```

## Topics

### Enumeration Cases
- [MLCDataType.float16](mlcdatatype/float16.md)
- [MLCDataType.float32](mlcdatatype/float32.md)
- [MLCDataType.boolean](mlcdatatype/boolean.md)
- [MLCDataType.int8](mlcdatatype/int8.md)
- [MLCDataType.int32](mlcdatatype/int32.md)
- [MLCDataType.int64](mlcdatatype/int64.md)
- [MLCDataType.uint8](mlcdatatype/uint8.md)
### Initializers
- [init?(rawValue: Int32)](mlcdatatype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(descriptor: MLCTensorDescriptor)](mlctensor/init(descriptor:).md)
  Creates a tensor without data, using the descriptor you specify.
- [convenience init(descriptor: MLCTensorDescriptor, data: MLCTensorData)](mlctensor/init(descriptor:data:).md)
  Creates a tensor with the descriptor and data you specify.
- [convenience init(descriptor: MLCTensorDescriptor, fillWithData: NSNumber)](mlctensor/init(descriptor:fillwithdata:).md)
  Creates a tensor with the descriptor and scalar value you specify.
- [convenience init(descriptor: MLCTensorDescriptor, randomInitializerType: MLCRandomInitializerType)](mlctensor/init(descriptor:randominitializertype:).md)
  Creates a tensor with the descriptor and random initializer type you specify.
- [class MLCTensorDescriptor](mlctensordescriptor.md)
  A configuration object you use to create a tensor.
- [class MLCTensorData](mlctensordata.md)
  An encapsulation of the memory that tensor data uses.
- [enum MLCRandomInitializerType](mlcrandominitializertype.md)
  An initializer type you use to create a tensor with random data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdatatype)*