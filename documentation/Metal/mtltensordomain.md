# MTLTensorDomain

**Framework**: Metal  
**Kind**: var

An error domain for errors that pertain to creating a tensor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let MTLTensorDomain: String
```

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
- [protocol MTLTensorBinding](mtltensorbinding.md)
  An object that represents a tensor bound to a graphics or compute function or a machine learning function.
- [struct MTLTensorError](mtltensorerror-swift.struct.md)
- [MTLTensorError.Code](mtltensorerror-swift.struct/code.md)
  The error codes that Metal can raise when you create a tensor.
- [enum MTLTensorDataType](mtltensordatatype.md)
  The possible data types for the elements of a tensor.
- [var MTL_TENSOR_MAX_RANK: Int32](mtl_tensor_max_rank.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordomain)*