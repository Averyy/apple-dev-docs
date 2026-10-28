# cullingPlanes

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The planes that define the culling volume.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var cullingPlanes: [LowLevelRenderer.CullConfiguration.Plane] { get set }
```

## Discussion

An instance is culled if its mesh part bounds lie entirely outside any single plane.

## See Also

### Creating a frustum
- [init(cullingPlanes: [LowLevelRenderer.CullConfiguration.Plane])](./init%28cullingplanes%29.md)
  Creates a frustum with the given culling planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullconfiguration/frustum-swift.struct/cullingplanes)*