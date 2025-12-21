# init(color:intensity:innerAngleInDegrees:outerAngleInDegrees:attenuationRadius:)

**Framework**: RealityKit  
**Kind**: init

Creates a spotlight with the given parameters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(color: SpotLightComponent.Color = .white, intensity: Float = 6740.94, innerAngleInDegrees: Float = 45.0, outerAngleInDegrees: Float = 60.0, attenuationRadius: Float = 10.0)
```

## Parameters

- `color`: The color of the light.
- `intensity`: The light’s brightness.
- `innerAngleInDegrees`: The angle of the cone that emits light at full intensity, in degrees.
- `outerAngleInDegrees`: The angle of the cone beyond which the spotlight’s intensity is zero.
- `attenuationRadius`: The distance from the light source where its intensity reaches zero.   Any objects at or beyond this distance do not receive illumination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/init(color:intensity:innerangleindegrees:outerangleindegrees:attenuationradius:))*