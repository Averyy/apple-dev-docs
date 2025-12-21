# attenuationRadius

**Framework**: RealityKit  
**Kind**: property

The distance from the light source where its intensity reaches zero.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var attenuationRadius: Float
```

#### Discussion

Any objects at or beyond this distance do not receive illumination. The default value is `10.0` meters.

See [`PointLightComponent`](pointlightcomponent.md) for more information about how the [`intensity`](pointlightcomponent/intensity.md) and `attenuationRadius` properties affect this light.

## See Also

- [var intensity: Float](pointlightcomponent/intensity.md)
  The intensity of the point light, measured in lumen.
- [var attenuationFalloffExponent: Float](pointlightcomponent/attenuationfalloffexponent.md)
  The exponent value for the light’s intensity falloff-transition curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/pointlightcomponent/attenuationradius)*