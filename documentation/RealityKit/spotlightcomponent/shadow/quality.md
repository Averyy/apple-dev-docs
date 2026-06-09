# quality

**Framework**: RealityKit  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS 27.0+ (Beta)

## Declaration

```swift
var quality: SpotLightComponent.Shadow.QualityMode { get set }
```

## See Also

- [SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode.md)
  The quality for the shadows. Low uses shadows that don’t change with light size and the distance between light-blocker-receiver Medium and high allow soft shadows with varying sample counts
- [var lightSize: Float](spotlightcomponent/shadow/lightsize.md)
  The light size that determines the softness of the shadows Larger size would mean a larger penumbra and a larger transition range from fully shadowed to lit. It is the radius of the light in world space units. It is also modulated by the attenaution radius, i.e., lights with larger attenuation radius need larger light size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/quality)*