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
- [var auxiliaryPlanes: [any MTLTensorAuxiliaryPlane]](mtltensor/auxiliaryplanes.md)
  The auxiliary planes of this tensor.
- [var buffer: (any MTLBuffer)?](mtltensor/buffer.md)
  A buffer instance this tensor shares its storage with or `nil` if this tensor does not wrap an underlying buffer.
- [var bufferOffset: Int](mtltensor/bufferoffset.md)
  An offset, in bytes, into the buffer instance this tensor shares its storage with, or zero if this tensor does not wrap an underlying buffer.
- [var dataType: MTLTensorDataType](mtltensor/datatype.md)
  The underlying data format of the data plane.
- [var dimensions: MTLTensorExtents](mtltensor/dimensions.md)
  An array of sizes, in elements, one for each dimension of this tensor.
- [var gpuResourceID: MTLResourceID](mtltensor/gpuresourceid.md)
  A handle that represents the GPU resource, which you can store in an argument buffer.
- [var strides: MTLTensorExtents?](mtltensor/strides.md)
  An array of strides, in elements, one for each dimension of this tensor, if applicable.
- [var usage: MTLTensorUsage](mtltensor/usage.md)
  A set of contexts in which you can use this tensor.
### Instance Methods
- [func getBytes(UnsafeMutableRawPointer, strides: MTLTensorExtents, sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents)](mtltensor/getbytes(_:strides:sliceorigin:slicedimensions:).md)
  Copies data from a slice of the data plane of this tensor into a pointer you provide.
- [func getBytes(UnsafeMutableRawPointer, strides: MTLTensorExtents, sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents, plane: MTLTensorPlaneType)](mtltensor/getbytes(_:strides:sliceorigin:slicedimensions:plane:).md)
  Copies data from a slice of a plane of this tensor into a pointer you provide.
- [func replace(sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents, plane: MTLTensorPlaneType, withBytes: UnsafeRawPointer, strides: MTLTensorExtents)](mtltensor/replace(sliceorigin:slicedimensions:plane:withbytes:strides:).md)
  Replaces a slice of a plane of this tensor with data from a pointer you provide.
- [func replace(sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents, withBytes: UnsafeRawPointer, strides: MTLTensorExtents)](mtltensor/replace(sliceorigin:slicedimensions:withbytes:strides:).md)
  Replaces a slice of the data plane of this tensor with data from a pointer you provide.

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [MTLResource](mtlresource.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class MTLTensorDescriptor](mtltensordescriptor.md)
  A configuration type for creating new tensor instances.
- [class MTLTensorExtents](mtltensorextents.md)
  An integer array that holds per-dimension values such as tensor sizes, strides, or block factors
- [class MTLTensorReferenceType](mtltensorreferencetype.md)
  An object that represents a tensor in the shading language in a struct or array.
- [struct MTLTensorUsage](mtltensorusage.md)
  The contexts in which you can use a tensor.
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