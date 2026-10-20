# drawMeshThreads(threadsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawMeshThreads(threadsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

```objc
- (void) drawMeshThreads:(MTLSize) threadsPerGrid threadsPerObjectThreadgroup:(MTLSize) threadsPerObjectThreadgroup threadsPerMeshThreadgroup:(MTLSize) threadsPerMeshThreadgroup;
```

## Parameters

- `threadsPerGrid`: A [`MTLSize`](../mtlsize.md) instance that represents the number of threads for each grid dimension. For mesh shaders, the command rounds the value down to the nearest multiple of `threadsPerMeshThreadgroup` for each dimension. For object shaders, the value doesn’t need to be a multiple of `threadsPerObjectThreadgroup`.
- `threadsPerObjectThreadgroup`: A [`MTLSize`](../mtlsize.md) instance that represents the number of threads in an object shader threadgroup, if applicable.
- `threadsPerMeshThreadgroup`: A [`MTLSize`](../mtlsize.md) instance that represents the number of threads in a mesh shader threadgroup.

## See Also

### Drawing with meshes
- [func drawMeshThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](./drawmeshthreadgroups%28threadgroupspergrid,threadsperobjectthreadgroup,threadspermeshthreadgroup%29.md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.
- [func drawMeshThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](./drawmeshthreadgroups%28indirectbuffer,threadsperobjectthreadgroup,threadspermeshthreadgroup%29.md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawmeshthreads(threadspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:))*