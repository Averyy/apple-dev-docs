# LowLevelRenderer.SortConfiguration

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The configuration for a mesh instance sort pass.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SortConfiguration
```

## Topics

### Creating a sort configuration
- [init(cameraPosition: SIMD3<Float>)](./sortconfiguration/init%28cameraposition%29.md)
  Creates a sort configuration with the given camera position.
- [var cameraPosition: SIMD3<Float>](./sortconfiguration/cameraposition.md)
  The camera position used to compute per-instance back-to-front sort distances for transparent draw calls.

## See Also

### Culling and sorting instances
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, outIndices: inout OutputSpan<Int>, configuration: LowLevelRenderer.CullConfiguration)](./cullmeshinstances%28_,indices,outindices,configuration%29.md)
  Culls mesh instances against a frustum, writing surviving indices to an output span.
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, configuration: LowLevelRenderer.CullConfiguration) -> [Int]](./cullmeshinstances%28_,indices,configuration%29.md)
  Culls mesh instances against a frustum and returns the surviving indices.
- [LowLevelRenderer.CullConfiguration](./cullconfiguration.md)
  The configuration for a frustum culling operation.
- [static func sortMeshInstances(LowLevelMeshInstanceArray, indices: inout MutableSpan<Int>, configuration: LowLevelRenderer.SortConfiguration)](./sortmeshinstances%28_,indices,configuration%29.md)
  Sorts the given mesh instances by sort category and, for transparent instances, by back-to-front distance from the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/sortconfiguration)*