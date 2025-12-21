# MTLTensor

**Framework**: Metal  
**Kind**: protocol

A resource representing a multi-dimensional array that you can use with machine learning workloads.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTLTensor : MTLResource
```

## Topics

### Instance Properties
- [var buffer: (any MTLBuffer)?](mtltensor/buffer.md)
  A buffer instance this tensor shares its storage with or nil if this tensor does not wrap an underlying buffer.
- [var bufferOffset: Int](mtltensor/bufferoffset.md)
  An offset, in bytes, into the buffer instance this tensor shares its storage with, or zero if this tensor does not wrap an underlying buffer.
- [var dataType: MTLTensorDataType](mtltensor/datatype.md)
  An underlying data format of this tensor.
- [var dimensions: MTLTensorExtents](mtltensor/dimensions.md)
  An array of sizes, in elements, one for each dimension of this tensor.
- [var gpuResourceID: MTLResourceID](mtltensor/gpuresourceid.md)
  A handle that represents the GPU resource, which you can store in an argument buffer.
- [var strides: MTLTensorExtents?](mtltensor/strides.md)
  An array of strides, in elements, one for each dimension of this tensor.
- [var usage: MTLTensorUsage](mtltensor/usage.md)
  A set of contexts in which you can use this tensor.
### Instance Methods
- [func getBytes(UnsafeMutableRawPointer, strides: MTLTensorExtents, sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents)](mtltensor/getbytes(_:strides:sliceorigin:slicedimensions:).md)
  Copies the data corresponding to a slice of this tensor into a pointer you provide.
- [func replace(sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents, withBytes: UnsafeRawPointer, strides: MTLTensorExtents)](mtltensor/replace(sliceorigin:slicedimensions:withbytes:strides:).md)
  Replaces the contents of a slice of this tensor with data you provide.

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [MTLResource](mtlresource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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
- [struct MTLTensorError](mtltensorerror-swift.struct.md)
- [MTLTensorError.Code](mtltensorerror-swift.struct/code.md)
  The error codes that Metal can raise when you create a tensor.
- [enum MTLTensorDataType](mtltensordatatype.md)
  The possible data types for the elements of a tensor.
- [let MTLTensorDomain: String](mtltensordomain.md)
  An error domain for errors that pertain to creating a tensor.
- [var MTL_TENSOR_MAX_RANK: Int32](mtl_tensor_max_rank.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor)*