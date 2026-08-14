# MTLTensorDescriptor

**Framework**: Metal  
**Kind**: class

A configuration type for creating new tensor instances.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTLTensorDescriptor
```

## Topics

### Instance Properties
- [var auxiliaryPlanes: MTLTensorAuxiliaryPlaneDescriptorMap?](mtltensordescriptor/auxiliaryplanes.md)
  The auxiliary plane configurations for this tensor.
- [var cpuCacheMode: MTLCPUCacheMode](mtltensordescriptor/cpucachemode.md)
  A value that configures the cache mode of CPU mapping of tensors you create with this descriptor.
- [var dataType: MTLTensorDataType](mtltensordescriptor/datatype.md)
  The data format of all elements in the data plane.
- [var dimensions: MTLTensorExtents](mtltensordescriptor/dimensions.md)
  An array of sizes, in elements, one for each dimension of the tensors you create with this descriptor.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtltensordescriptor/hazardtrackingmode.md)
  A value that configures the hazard tracking of tensors you create with this descriptor.
- [var resourceOptions: MTLResourceOptions](mtltensordescriptor/resourceoptions.md)
  A packed set of the [`storageMode`](mtltensordescriptor/storagemode.md), [`cpuCacheMode`](mtltensordescriptor/cpucachemode.md), and [`hazardTrackingMode`](mtltensordescriptor/hazardtrackingmode.md) properties.
- [var storageMode: MTLStorageMode](mtltensordescriptor/storagemode.md)
  A value that configures the memory location and access permissions of tensors you create with this descriptor.
- [var strides: MTLTensorExtents?](mtltensordescriptor/strides.md)
  An array of strides, in elements, one for each dimension of this tensor, if applicable.
- [var usage: MTLTensorUsage](mtltensordescriptor/usage.md)
  A set of contexts in which you can use tensors you create with this descriptor.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [protocol MTLTensor](mtltensor.md)
  A resource representing a multi-dimensional array that you can use with machine learning workloads.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor)*