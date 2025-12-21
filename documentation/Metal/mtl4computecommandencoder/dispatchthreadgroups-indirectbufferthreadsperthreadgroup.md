# dispatchThreadgroups(indirectBuffer:threadsPerThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func dispatchThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerThreadgroup: MTLSize)
```

#### Discussion

This method allows you to supply the threadgroups-per-grid counts indirectly via an [`MTLBuffer`](mtlbuffer.md) index. This enables you to calculate this value in the GPU timeline from a shader function, enabling GPU-driven workflows.

Metal assumes that the buffer contents correspond to the layout of struct [`MTLDispatchThreadgroupsIndirectArguments`](mtldispatchthreadgroupsindirectarguments.md). You are responsible for ensuring this address aligns to 4-bytes.

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectBuffer` parameter references.

## Parameters

- `indirectBuffer`: GPUAddress of a   instance providing compute parameters.   Lay out the data in this buffer as described in the    structure. This address   requires 4-byte alignment.
- `threadsPerThreadgroup`: A   instance that represents the number of threads in one   threadgroup, in each dimension.

## See Also

- [func dispatchThreads(threadsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreads(threadspergrid:threadsperthreadgroup:).md)
  Encodes a compute dispatch command using an arbitrarily-sized grid.
- [func dispatchThreads(indirectBuffer: MTLGPUAddress)](mtl4computecommandencoder/dispatchthreads(indirectbuffer:).md)
  Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.
- [func dispatchThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](mtl4computecommandencoder/dispatchthreadgroups(threadgroupspergrid:threadsperthreadgroup:).md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/dispatchthreadgroups(indirectbuffer:threadsperthreadgroup:))*