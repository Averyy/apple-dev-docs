# drawMeshThreadgroups(_:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func drawMeshThreadgroups(_ threadgroupsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

```objc
- (void) drawMeshThreadgroups:(MTLSize) threadgroupsPerGrid threadsPerObjectThreadgroup:(MTLSize) threadsPerObjectThreadgroup threadsPerMeshThreadgroup:(MTLSize) threadsPerMeshThreadgroup;
```

## Parameters

- `threadgroupsPerGrid`: An [`MTLSize`](../mtlsize.md) instance that represents the number of threadgroups for each grid dimension.
- `threadsPerObjectThreadgroup`: An [`MTLSize`](../mtlsize.md) instance that represents the number of threads in an object shader threadgroup, if applicable.
- `threadsPerMeshThreadgroup`: An [`MTLSize`](../mtlsize.md) instance that represents the number of threads in a mesh shader threadgroup.

## See Also

### Drawing with meshes
- [func drawMeshThreads(MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](./drawmeshthreads%28_,threadsperobjectthreadgroup,threadspermeshthreadgroup%29.md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [func drawMeshThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](./drawmeshthreadgroups%28indirectbuffer,indirectbufferoffset,threadsperobjectthreadgroup,threadspermeshthreadgroup%29.md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawmeshthreadgroups(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:))*