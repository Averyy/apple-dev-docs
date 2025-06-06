# init(descriptor:data:)

**Framework**: ML Compute  
**Kind**: init

Creates a tensor with the descriptor and data you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(descriptor tensorDescriptor: MLCTensorDescriptor, data: MLCTensorData)
```

## Parameters

- `tensorDescriptor`: An object you use to configure the tensor.
- `data`: The tensor data.

## See Also

- [convenience init(descriptor: MLCTensorDescriptor)](mlctensor/init(descriptor:).md)
  Creates a tensor without data, using the descriptor you specify.
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
- [enum MLCRandomInitializerType](mlcrandominitializertype.md)
  An initializer type you use to create a tensor with random data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/init(descriptor:data:))*