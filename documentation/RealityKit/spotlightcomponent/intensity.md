# intensity

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The intensity of the spotlight measured in lumen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var intensity: Float
```

## Discussion

The default value is `6740.94` lumens.

For more information on how the `intensity` and [`attenuationRadius`](./attenuationradius.md) affect this light, see  [`SpotLightComponent`](../spotlightcomponent.md).

## See Also

### Configuring the spotlight
- [var innerAngleInDegrees: Float](./innerangleindegrees.md)
  The inner angle of the spotlight in degrees.
- [var outerAngleInDegrees: Float](./outerangleindegrees.md)
  The outer angle of the spotlight in degrees.
- [var attenuationRadius: Float](./attenuationradius.md)
  The distance from the light source where its intensity reaches zero.
- [var attenuationFalloffExponent: Float](./attenuationfalloffexponent.md)
  The exponent value for the light’s intensity falloff-transition curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/intensity)*