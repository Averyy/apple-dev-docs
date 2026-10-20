# LowLevelRenderer.CullConfiguration

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The configuration for a frustum culling operation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct CullConfiguration
```

## Topics

### Creating a cull configuration
- [init(frustum: LowLevelRenderer.CullConfiguration.Frustum)](./cullconfiguration/init%28frustum%29.md)
  Creates a cull configuration with the given frustum.
### Configuring the frustum
- [var frustum: LowLevelRenderer.CullConfiguration.Frustum](./cullconfiguration/frustum-swift.property.md)
  The frustum to test instances against.
- [LowLevelRenderer.CullConfiguration.Frustum](./cullconfiguration/frustum-swift.struct.md)
  A culling frustum defined by a set of planes.
### Defining frustum planes
- [LowLevelRenderer.CullConfiguration.Plane](./cullconfiguration/plane.md)
  An infinite directed plane used to cull mesh instances.

## See Also

### Culling and sorting instances
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, outIndices: inout OutputSpan<Int>, configuration: LowLevelRenderer.CullConfiguration)](./cullmeshinstances%28_,indices,outindices,configuration%29.md)
  Culls mesh instances against a frustum, writing surviving indices to an output span.
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, configuration: LowLevelRenderer.CullConfiguration) -> [Int]](./cullmeshinstances%28_,indices,configuration%29.md)
  Culls mesh instances against a frustum and returns the surviving indices.
- [static func sortMeshInstances(LowLevelMeshInstanceArray, indices: inout MutableSpan<Int>, configuration: LowLevelRenderer.SortConfiguration)](./sortmeshinstances%28_,indices,configuration%29.md)
  Sorts the given mesh instances by sort category and, for transparent instances, by back-to-front distance from the camera.
- [LowLevelRenderer.SortConfiguration](./sortconfiguration.md)
  The configuration for a mesh instance sort pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullconfiguration)*