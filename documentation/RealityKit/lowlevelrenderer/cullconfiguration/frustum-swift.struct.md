# LowLevelRenderer.CullConfiguration.Frustum

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A culling frustum defined by a set of planes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Frustum
```

## Topics

### Creating a frustum
- [init(cullingPlanes: [LowLevelRenderer.CullConfiguration.Plane])](./frustum-swift.struct/init%28cullingplanes%29.md)
  Creates a frustum with the given culling planes.
- [var cullingPlanes: [LowLevelRenderer.CullConfiguration.Plane]](./frustum-swift.struct/cullingplanes.md)
  The planes that define the culling volume.
### Initializers
- [init(from: LowLevelRenderer.Camera)](./frustum-swift.struct/init%28from%29.md)
  Creates a frustum by computing the culling planes for the given camera.

## See Also

### Configuring the frustum
- [var frustum: LowLevelRenderer.CullConfiguration.Frustum](./frustum-swift.property.md)
  The frustum to test instances against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullconfiguration/frustum-swift.struct)*