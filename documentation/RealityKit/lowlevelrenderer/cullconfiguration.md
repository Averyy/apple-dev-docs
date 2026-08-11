# LowLevelRenderer.CullConfiguration

**Framework**: RealityKit  
**Kind**: struct

The configuration for a frustum culling operation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct CullConfiguration
```

## Topics

### Creating a cull configuration
- [init(frustum: LowLevelRenderer.CullConfiguration.Frustum)](lowlevelrenderer/cullconfiguration/init(frustum:).md)
  Creates a cull configuration with the given frustum.
### Configuring the frustum
- [var frustum: LowLevelRenderer.CullConfiguration.Frustum](lowlevelrenderer/cullconfiguration/frustum-swift.property.md)
  The frustum to test instances against.
- [LowLevelRenderer.CullConfiguration.Frustum](lowlevelrenderer/cullconfiguration/frustum-swift.struct.md)
  A culling frustum defined by a set of planes.
### Defining frustum planes
- [LowLevelRenderer.CullConfiguration.Plane](lowlevelrenderer/cullconfiguration/plane.md)
  An infinite directed plane used to cull mesh instances.

## See Also

- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, outIndices: inout OutputSpan<Int>, configuration: LowLevelRenderer.CullConfiguration)](lowlevelrenderer/cullmeshinstances(_:indices:outindices:configuration:).md)
  Culls mesh instances against a frustum, writing surviving indices to an output span.
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, configuration: LowLevelRenderer.CullConfiguration) -> [Int]](lowlevelrenderer/cullmeshinstances(_:indices:configuration:).md)
  Culls mesh instances against a frustum and returns the surviving indices.
- [static func sortMeshInstances(LowLevelMeshInstanceArray, indices: inout MutableSpan<Int>, configuration: LowLevelRenderer.SortConfiguration)](lowlevelrenderer/sortmeshinstances(_:indices:configuration:).md)
  Sorts the given mesh instances by sort category and, for transparent instances, by back-to-front distance from the camera.
- [LowLevelRenderer.SortConfiguration](lowlevelrenderer/sortconfiguration.md)
  The configuration for a mesh instance sort pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullconfiguration)*