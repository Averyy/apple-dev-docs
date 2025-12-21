# drawMeshThreadgroups(indirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawMeshThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

#### Discussion

This method enables you to determine the number of threadgroups per grid indirectly, in the GPU timeline. Metal expects this buffer’s contents to match the layout of structure [`MTLDispatchThreadgroupsIndirectArguments`](mtldispatchthreadgroupsindirectarguments.md). You are responsible for ensuring the address of this buffer has 4-byte alignment.

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectBuffer` parameter references.

## Parameters

- `indirectBuffer`: GPUAddress of an   instance with data that matches the layout of the    structure. This address requires 4-byte alignment.
- `threadsPerObjectThreadgroup`: A   instance that represents the number of threads in an object   shader threadgroup, if applicable.
- `threadsPerMeshThreadgroup`: A   instance that represents the number of threads in a mesh shader   threadgroup.

## See Also

- [func drawMeshThreads(threadsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreads(threadspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [func drawMeshThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawmeshthreadgroups(indirectbuffer:threadsperobjectthreadgroup:threadspermeshthreadgroup:))*