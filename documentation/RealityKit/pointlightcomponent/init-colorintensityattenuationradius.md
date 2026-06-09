# init(color:intensity:attenuationRadius:)

**Framework**: RealityKit  
**Kind**: init

Creates a point light component with a configuration.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(color: PointLightComponent.Color = .white, intensity: Float = 26963.76, attenuationRadius: Float = 10.0)
```

## Parameters

- `color`: The color of the light.
- `intensity`: The intensity of the light in lumens.
- `attenuationRadius`: The distance from the light source where its intensity reaches zero. Any objects at or beyond this distance do not receive illumination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/pointlightcomponent/init(color:intensity:attenuationradius:))*