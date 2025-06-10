# MTLTensorError

**Framework**: Metal  
**Kind**: enum

The error codes that Metal can raise when you create a tensor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum MTLTensorError
```

## Topics

### Enumeration Cases
- [MTLTensorError.internalError](mtltensorerror/internalerror.md)
- [MTLTensorError.invalidDescriptor](mtltensorerror/invaliddescriptor.md)
- [MTLTensorError.none](mtltensorerror/none.md)
### Initializers
- [init?(rawValue: UInt)](mtltensorerror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTLTensor](mtltensor.md)
  A resource representing a multi-dimensional array that you can use with machine learning workloads.
- [class MTLTensorDescriptor](mtltensordescriptor.md)
  A configuration type for creating new tensor instances.
- [class MTLTensorExtents](mtltensorextents.md)
  An array of length matching the rank, holding the dimensions of a tensor.
- [class MTLTensorReferenceType](mtltensorreferencetype.md)
  An object that represents a tensor in the shading language in a struct or array.
- [struct MTLTensorUsage](mtltensorusage.md)
  The type that represents the different contexts for a tensor.
- [let MTLTensorDomain: String](mtltensordomain.md)
  An error domain for errors that pertain to creating a tensor.
- [protocol MTLTensorBinding](mtltensorbinding.md)
  An object that represents a tensor bound to a graphics or compute function or a machine learning function.
- [enum MTLTensorDataType](mtltensordatatype.md)
  The possible data types for the elements of a tensor.
- [let MTLTensorDomain: String](mtltensordomain.md)
  An error domain for errors that pertain to creating a tensor.
- [var MTL_TENSOR_MAX_RANK: Int32](mtl_tensor_max_rank.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorerror)*