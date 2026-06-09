# LowLevelRenderer.CullConfiguration.Frustum

**Framework**: RealityKit  
**Kind**: struct

A culling frustum defined by a set of planes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Frustum
```

## Topics

### Creating a frustum
- [init(cullingPlanes: [LowLevelRenderer.CullConfiguration.Plane])](lowlevelrenderer/cullconfiguration/frustum-swift.struct/init(cullingplanes:).md)
  Creates a frustum with the given culling planes.
- [var cullingPlanes: [LowLevelRenderer.CullConfiguration.Plane]](lowlevelrenderer/cullconfiguration/frustum-swift.struct/cullingplanes.md)
  The planes that define the culling volume.
### Initializers
- [init(from: LowLevelRenderer.Camera)](lowlevelrenderer/cullconfiguration/frustum-swift.struct/init(from:).md)
  Creates a frustum by computing the culling planes for the given camera.

## See Also

- [var frustum: LowLevelRenderer.CullConfiguration.Frustum](lowlevelrenderer/cullconfiguration/frustum-swift.property.md)
  The frustum to test instances against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullconfiguration/frustum-swift.struct)*