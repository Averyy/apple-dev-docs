# LowLevelRenderer.SortConfiguration

**Framework**: RealityKit  
**Kind**: struct

The parameters for a mesh instance sort pass.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SortConfiguration
```

## Topics

### Creating a sort configuration
- [init(cameraPosition: SIMD3<Float>)](lowlevelrenderer/sortconfiguration/init(cameraposition:).md)
  Creates a sort configuration with the given camera position.
- [var cameraPosition: SIMD3<Float>](lowlevelrenderer/sortconfiguration/cameraposition.md)
  The camera position used to compute per-instance back-to-front sort distances for transparent draw calls.

## See Also

- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, outIndices: inout OutputSpan<Int>, configuration: LowLevelRenderer.CullConfiguration)](lowlevelrenderer/cullmeshinstances(_:indices:outindices:configuration:).md)
  Culls mesh instances against a frustum, writing surviving indices to an output span.
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, configuration: LowLevelRenderer.CullConfiguration) -> [Int]](lowlevelrenderer/cullmeshinstances(_:indices:configuration:).md)
  Culls mesh instances against a frustum and returns the surviving indices.
- [LowLevelRenderer.CullConfiguration](lowlevelrenderer/cullconfiguration.md)
  The parameters for a frustum culling operation.
- [static func sortMeshInstances(LowLevelMeshInstanceArray, indices: inout MutableSpan<Int>, configuration: LowLevelRenderer.SortConfiguration)](lowlevelrenderer/sortmeshinstances(_:indices:configuration:).md)
  Sorts the given mesh instances by sort category and, for transparent instances, by back-to-front distance from the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/sortconfiguration)*