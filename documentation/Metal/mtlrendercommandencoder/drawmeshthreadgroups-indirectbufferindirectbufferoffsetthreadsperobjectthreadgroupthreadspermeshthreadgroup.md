# drawMeshThreadgroups(indirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func drawMeshThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

## Parameters

- `indirectBuffer`: An   instance with data that matches the layout of the   structure.
- `indirectBufferOffset`: See the   to check for offset alignment requirements for buffers in   and   address space.
- `threadsPerObjectThreadgroup`: An   instance that represents the number of threads in an object shader threadgroup, if applicable.
- `threadsPerMeshThreadgroup`: An   instance that represents the number of threads in a mesh shader threadgroup.

## See Also

- [func drawMeshThreads(MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtlrendercommandencoder/drawmeshthreads(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [func drawMeshThreadgroups(MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtlrendercommandencoder/drawmeshthreadgroups(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawmeshthreadgroups(indirectbuffer:indirectbufferoffset:threadsperobjectthreadgroup:threadspermeshthreadgroup:))*