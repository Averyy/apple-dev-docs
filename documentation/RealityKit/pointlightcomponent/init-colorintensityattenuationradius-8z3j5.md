# init(color:intensity:attenuationRadius:)

**Framework**: RealityKit  
**Kind**: init

Creates a point light component with a configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 2.0+

## Declaration

```swift
init(color: PointLightComponent.Color = .white, intensity: Float = 26963.76, attenuationRadius: Float = 10.0)
```

## Parameters

- `color`: The color of the light.
- `intensity`: The intensity of the light in lumens.
- `attenuationRadius`: The distance from the light source where its intensity reaches zero.   Any objects at or beyond this distance do not receive illumination.

## See Also

- [init(color: PointLightComponent.Color, intensity: Float, attenuationRadius: Float)](pointlightcomponent/init(color:intensity:attenuationradius:)-hp22.md)
  Creates a point light component with a configuration.
- [init(cgColor: CGColor, intensity: Float, attenuationRadius: Float)](pointlightcomponent/init(cgcolor:intensity:attenuationradius:).md)
  Creates a new instance with the specified color, intensity and attenuation.
- [init(color: PointLightComponent.Color, intensity: Float, attenuationRadius: Float, attenuationFalloffExponent: Float)](pointlightcomponent/init(color:intensity:attenuationradius:attenuationfalloffexponent:)-603s0.md)
  Creates a point light component with a configuration.
- [init(color: PointLightComponent.Color, intensity: Float, attenuationRadius: Float, attenuationFalloffExponent: Float)](pointlightcomponent/init(color:intensity:attenuationradius:attenuationfalloffexponent:)-6dm4f.md)
  Creates a point light component with a configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/pointlightcomponent/init(color:intensity:attenuationradius:)-8z3j5)*