# attenuationRadius

**Framework**: RealityKit  
**Kind**: property

The distance from the light source where its intensity reaches zero.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var attenuationRadius: Float
```

#### Discussion

Any objects at or beyond this distance do not receive illumination. The default value is `10.0` meters.

See [`SpotLightComponent`](spotlightcomponent.md) for more information about how the [`intensity`](spotlightcomponent/intensity.md) and `attenuationRadius` properties affect this light.

## See Also

- [var intensity: Float](spotlightcomponent/intensity.md)
  The intensity of the spotlight measured in lumen.
- [var innerAngleInDegrees: Float](spotlightcomponent/innerangleindegrees.md)
  The inner angle of the spotlight in degrees.
- [var outerAngleInDegrees: Float](spotlightcomponent/outerangleindegrees.md)
  The outer angle of the spotlight in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/attenuationradius)*