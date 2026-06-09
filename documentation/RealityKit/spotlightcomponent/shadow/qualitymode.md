# SpotLightComponent.Shadow.QualityMode

**Framework**: RealityKit  
**Kind**: struct

The quality for the shadows. Low uses shadows that don’t change with light size and the distance between light-blocker-receiver Medium and high allow soft shadows with varying sample counts

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct QualityMode
```

## Topics

### Choosing a quality level
- [static var low: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode/low.md)
- [static var medium: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode/medium.md)
### Initializers
- [init(rawValue: Int)](spotlightcomponent/shadow/qualitymode/init(rawvalue:).md)
### Instance Properties
- [var rawValue: Int](spotlightcomponent/shadow/qualitymode/rawvalue.md)
### Type Properties
- [static var high: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode/high.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var quality: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/quality.md)
- [var lightSize: Float](spotlightcomponent/shadow/lightsize.md)
  The light size that determines the softness of the shadows Larger size would mean a larger penumbra and a larger transition range from fully shadowed to lit. It is the radius of the light in world space units. It is also modulated by the attenaution radius, i.e., lights with larger attenuation radius need larger light size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/qualitymode)*