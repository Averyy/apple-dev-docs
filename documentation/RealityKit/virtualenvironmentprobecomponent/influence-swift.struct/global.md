# global

**Framework**: RealityKit  
**Kind**: property

A global influence — the probe affects all objects in the world regardless of position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var global: VirtualEnvironmentProbeComponent.Influence { get }
```

## See Also

- [static func local(parallaxBounds: BoundingBox, blendDistance: Float) -> VirtualEnvironmentProbeComponent.Influence](virtualenvironmentprobecomponent/influence-swift.struct/local(parallaxbounds:blenddistance:).md)
  A local influence using a single bounding box for both parallax correction and influence volume. Local influence for virtual environment probes is available on devices with Apple6 GPU family feature support.
- [static func local(parallaxBounds: BoundingBox, influenceBounds: BoundingBox, blendDistance: Float) -> VirtualEnvironmentProbeComponent.Influence](virtualenvironmentprobecomponent/influence-swift.struct/local(parallaxbounds:influencebounds:blenddistance:).md)
  A local influence with independent parallax correction and influence volumes. Local influence for virtual environment probes is available on devices with Apple6 GPU family feature support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/virtualenvironmentprobecomponent/influence-swift.struct/global)*