# drawMeshThreadgroups(threadgroupsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawMeshThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

## Parameters

- `threadgroupsPerGrid`: A   instance that represents the number of threadgroups for each grid dimension.
- `threadsPerObjectThreadgroup`: A   instance that represents the number of threads in an object   shader threadgroup, if applicable.
- `threadsPerMeshThreadgroup`: A   instance that represents the number of threads in a mesh shader   threadgroup.

## See Also

- [func drawMeshThreads(threadsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreads(threadspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [func drawMeshThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreadgroups(indirectbuffer:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:))*