# intensity

**Framework**: RealityKit  
**Kind**: property

The intensity of the point light, measured in lumen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 2.0+

## Declaration

```swift
var intensity: Float
```

#### Discussion

The default value is `26963.76` lumens.

See [`PointLightComponent`](pointlightcomponent.md) for more information about how the `intensity` and [`attenuationRadius`](pointlightcomponent/attenuationradius.md) properties affect this light.

## See Also

- [var attenuationRadius: Float](pointlightcomponent/attenuationradius.md)
  The distance from the light source where its intensity reaches zero.
- [var attenuationFalloffExponent: Float](pointlightcomponent/attenuationfalloffexponent.md)
  The exponent value for the light’s intensity falloff-transition curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/pointlightcomponent/intensity)*