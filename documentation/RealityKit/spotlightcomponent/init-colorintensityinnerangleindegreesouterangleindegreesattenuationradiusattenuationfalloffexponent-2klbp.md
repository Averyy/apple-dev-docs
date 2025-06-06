# init(color:intensity:innerAngleInDegrees:outerAngleInDegrees:attenuationRadius:attenuationFalloffExponent:)

**Framework**: RealityKit  
**Kind**: init

Creates a spotlight with the given parameters.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(color: SpotLightComponent.Color = .white, intensity: Float = 6740.94, innerAngleInDegrees: Float = 45.0, outerAngleInDegrees: Float = 60.0, attenuationRadius: Float = 10.0, attenuationFalloffExponent: Float = 2.0)
```

## Parameters

- `color`: The color of the light.
- `intensity`: The light’s brightness.
- `innerAngleInDegrees`: The angle of the cone that emits light at full intensity, in degrees.
- `outerAngleInDegrees`: The angle of the cone beyond which the spotlight’s intensity is zero.
- `attenuationRadius`: The distance from the light source where its intensity reaches zero.   Any objects at or beyond this distance do not receive illumination.
- `attenuationFalloffExponent`: An exponent value for the light’s intensity falloff-transition curve.

## See Also

- [init(color: SpotLightComponent.Color, intensity: Float, innerAngleInDegrees: Float, outerAngleInDegrees: Float, attenuationRadius: Float)](spotlightcomponent/init(color:intensity:innerangleindegrees:outerangleindegrees:attenuationradius:)-483ep.md)
  Creates a spotlight with the given parameters.
- [init(color: SpotLightComponent.Color, intensity: Float, innerAngleInDegrees: Float, outerAngleInDegrees: Float, attenuationRadius: Float)](spotlightcomponent/init(color:intensity:innerangleindegrees:outerangleindegrees:attenuationradius:)-8u5j6.md)
  Creates a spotlight with the given parameters.
- [init(color: SpotLightComponent.Color, intensity: Float, innerAngleInDegrees: Float, outerAngleInDegrees: Float, attenuationRadius: Float, attenuationFalloffExponent: Float)](spotlightcomponent/init(color:intensity:innerangleindegrees:outerangleindegrees:attenuationradius:attenuationfalloffexponent:)-4v8eh.md)
  Creates a spotlight with the given parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/init(color:intensity:innerangleindegrees:outerangleindegrees:attenuationradius:attenuationfalloffexponent:)-2klbp)*