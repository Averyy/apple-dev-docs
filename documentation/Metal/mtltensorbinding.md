# MTLTensorBinding

**Framework**: Metal  
**Kind**: protocol

An object that represents a tensor bound to a graphics or compute function or a machine learning function.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTLTensorBinding : MTLBinding
```

## Topics

### Instance Properties
- [var dimensions: MTLTensorExtents?](mtltensorbinding/dimensions.md)
  The array of sizes, in elements, one for each dimension of this tensor.
- [var indexType: MTLDataType](mtltensorbinding/indextype.md)
  The data format you use for indexing into the tensor.
- [var tensorDataType: MTLTensorDataType](mtltensorbinding/tensordatatype.md)
  The underlying data format of this tensor.

## Relationships

### Inherits From
- [MTLBinding](mtlbinding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
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
- [struct MTLTensorError](mtltensorerror-swift.struct.md)
- [MTLTensorError.Code](mtltensorerror-swift.struct/code.md)
  The error codes that Metal can raise when you create a tensor.
- [enum MTLTensorDataType](mtltensordatatype.md)
  The possible data types for the elements of a tensor.
- [let MTLTensorDomain: String](mtltensordomain.md)
  An error domain for errors that pertain to creating a tensor.
- [var MTL_TENSOR_MAX_RANK: Int32](mtl_tensor_max_rank.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorbinding)*