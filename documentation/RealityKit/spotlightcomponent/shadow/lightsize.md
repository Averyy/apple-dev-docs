# lightSize

**Framework**: RealityKit  
**Kind**: property

The radius of the spotlight’s emitting surface, in meters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS 27.0+ (Beta)

## Declaration

```swift
var lightSize: Float { get set }
```

#### Discussion

Larger values widen the penumbra and lengthen the transition between fully-shadowed and fully-lit regions, approximating the way an area light of that radius would shade a scene. The default value is `0.1`.

This property has no effect when [`quality`](spotlightcomponent/shadow/quality.md) is [`low`](spotlightcomponent/shadow/qualitymode/low.md), which always produces a hard-edged shadow.

## See Also

- [var quality: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/quality.md)
  The shadow-filtering algorithm this light uses.
- [SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode.md)
  Constants that select the shadow-filtering algorithm a spotlight uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/lightsize)*