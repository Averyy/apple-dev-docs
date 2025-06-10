# MLCRandomInitializerType

**Framework**: ML Compute  
**Kind**: enum

An initializer type you use to create a tensor with random data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCRandomInitializerType
```

## Topics

### Enumeration Cases
- [MLCRandomInitializerType.uniform](mlcrandominitializertype/uniform.md)
- [MLCRandomInitializerType.glorotUniform](mlcrandominitializertype/glorotuniform.md)
- [MLCRandomInitializerType.xavier](mlcrandominitializertype/xavier.md)
### Initializers
- [init?(rawValue: Int32)](mlcrandominitializertype/init(rawvalue:).md)

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
- [enum MLCDataType](mlcdatatype.md)
  A tensor data type.
- [class MLCTensorData](mlctensordata.md)
  An encapsulation of the memory that tensor data uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrandominitializertype)*