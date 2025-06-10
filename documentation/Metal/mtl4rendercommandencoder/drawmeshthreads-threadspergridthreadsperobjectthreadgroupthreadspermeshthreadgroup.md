# drawMeshThreads(threadsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func drawMeshThreads(threadsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

## Parameters

- `threadsPerGrid`: A   instance that represents the number of threads for each grid dimension.   For mesh shaders, the command rounds the value down to the nearest multiple of    for each dimension. For object shaders, the value doesn’t   need to be a multiple of  .
- `threadsPerObjectThreadgroup`: A   instance that represents the number of threads in an object   shader threadgroup, if applicable.
- `threadsPerMeshThreadgroup`: A   instance that represents the number of threads in a mesh shader   threadgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawmeshthreads(threadspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:))*