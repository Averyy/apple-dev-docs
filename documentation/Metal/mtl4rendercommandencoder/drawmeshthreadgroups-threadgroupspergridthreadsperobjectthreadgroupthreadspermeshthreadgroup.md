# drawMeshThreadgroups(threadgroupsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func drawMeshThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

## Parameters

- `threadgroupsPerGrid`: A   instance that represents the number of threadgroups for each grid dimension.
- `threadsPerObjectThreadgroup`: A   instance that represents the number of threads in an object   shader threadgroup, if applicable.
- `threadsPerMeshThreadgroup`: A   instance that represents the number of threads in a mesh shader   threadgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:))*