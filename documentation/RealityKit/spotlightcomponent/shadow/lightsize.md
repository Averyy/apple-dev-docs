# lightSize

**Framework**: RealityKit  
**Kind**: property

The light size that determines the softness of the shadows Larger size would mean a larger penumbra and a larger transition range from fully shadowed to lit. It is the radius of the light in world space units. It is also modulated by the attenaution radius, i.e., lights with larger attenuation radius need larger light size.

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

## See Also

- [var quality: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/quality.md)
- [SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode.md)
  The quality for the shadows. Low uses shadows that don’t change with light size and the distance between light-blocker-receiver Medium and high allow soft shadows with varying sample counts


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/lightsize)*