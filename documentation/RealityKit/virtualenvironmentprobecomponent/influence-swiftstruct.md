# VirtualEnvironmentProbeComponent.Influence

**Framework**: RealityKit  
**Kind**: struct

Defines the spatial influence of an environment probe.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Influence
```

## Topics

### Creating an influence
- [static var global: VirtualEnvironmentProbeComponent.Influence](virtualenvironmentprobecomponent/influence-swift.struct/global.md)
  A global influence — the probe affects all objects in the world regardless of position.
- [static func local(parallaxBounds: BoundingBox, blendDistance: Float) -> VirtualEnvironmentProbeComponent.Influence](virtualenvironmentprobecomponent/influence-swift.struct/local(parallaxbounds:blenddistance:).md)
  A local influence using a single bounding box for both parallax correction and influence volume.
- [static func local(parallaxBounds: BoundingBox, influenceBounds: BoundingBox, blendDistance: Float) -> VirtualEnvironmentProbeComponent.Influence](virtualenvironmentprobecomponent/influence-swift.struct/local(parallaxbounds:influencebounds:blenddistance:).md)
  A local influence with independent parallax correction and influence volumes.

## See Also

- [var influence: VirtualEnvironmentProbeComponent.Influence](virtualenvironmentprobecomponent/influence-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/virtualenvironmentprobecomponent/influence-swift.struct)*