# dispatchThreads(indirectBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func dispatchThreads(indirectBuffer: MTLGPUAddress)
```

## Parameters

- `indirectBuffer`: GPUAddress of a   instance providing arguments. Lay out the data   in this buffer as described in the    structure. This address requires 4-byte alignment.

## See Also

- [func dispatchThreads(threadsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreads(threadspergrid:threadsperthreadgroup:).md)
  Encodes a compute dispatch command using an arbitrarily-sized grid.
- [func dispatchThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreadgroups(threadgroupspergrid:threadsperthreadgroup:).md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.
- [func dispatchThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreadgroups(indirectbuffer:threadsperthreadgroup:).md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/dispatchthreads(indirectbuffer:))*