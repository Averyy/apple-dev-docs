# local(parallaxBounds:influenceBounds:blendDistance:)

**Framework**: RealityKit  
**Kind**: method

A local influence with independent parallax correction and influence volumes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func local(parallaxBounds: BoundingBox, influenceBounds: BoundingBox, blendDistance: Float) -> VirtualEnvironmentProbeComponent.Influence
```

## Parameters

- `parallaxBounds`: The bounding box used for parallax correction (local space).
- `influenceBounds`: The bounding box that defines the probe’s area of influence (local space).
- `blendDistance`: The distance from the edge of the influence volume over which the probe fades.

## See Also

- [static var global: VirtualEnvironmentProbeComponent.Influence](virtualenvironmentprobecomponent/influence-swift.struct/global.md)
  A global influence — the probe affects all objects in the world regardless of position.
- [static func local(parallaxBounds: BoundingBox, blendDistance: Float) -> VirtualEnvironmentProbeComponent.Influence](virtualenvironmentprobecomponent/influence-swift.struct/local(parallaxbounds:blenddistance:).md)
  A local influence using a single bounding box for both parallax correction and influence volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/virtualenvironmentprobecomponent/influence-swift.struct/local(parallaxbounds:influencebounds:blenddistance:))*