# cullingPlanes

**Framework**: RealityKit  
**Kind**: property

The planes that define the culling volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var cullingPlanes: [LowLevelRenderer.CullConfiguration.Plane] { get set }
```

#### Discussion

An instance is culled if its mesh part bounds lie entirely outside any single plane.

## See Also

- [init(cullingPlanes: [LowLevelRenderer.CullConfiguration.Plane])](lowlevelrenderer/cullconfiguration/frustum-swift.struct/init(cullingplanes:).md)
  Creates a frustum with the given culling planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullconfiguration/frustum-swift.struct/cullingplanes)*