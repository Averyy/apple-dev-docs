# SpotLightComponent

**Framework**: RealityKit  
**Kind**: struct

A component that defines a spotlight source.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 2.0+

## Declaration

```swift
struct SpotLightComponent
```

#### Overview

A spotlight illuminates a cone-shaped volume in the entity’s local forward direction along the z-axis’s negative direction, or `[0.0, 0.0, -1.0]`. Change the a spotlight’s direction with the [`orientation`](entity/orientation.md) or [`look(at:from:upVector:relativeTo:)`](hastransform/look(at:from:upvector:relativeto:).md) method, of the [`Entity`](entity.md) with a spotlight component.

The light’s [`innerAngleInDegrees`](spotlightcomponent/innerangleindegrees.md) and [`outerAngleInDegrees`](spotlightcomponent/outerangleindegrees.md) reflect the size of the light’s cone relative to the entity’s forward direction. The light is at full intensity between `0` degrees and [`innerAngleInDegrees`](spotlightcomponent/innerangleindegrees.md). RealityKit attenuates the light’s intensity between the inner angle and the outer angle. The spotlight’s intensity is `0.0` beyond the outer angle.

> 💡 **Tip**: Turn on shadows for a spotlight by adding the [`SpotLightComponent.Shadow`](spotlightcomponent/shadow.md) component to an entity that has a `SpotLightComponent`.

Turn on shadows for a spotlight by adding the [`SpotLightComponent.Shadow`](spotlightcomponent/shadow.md) component to an entity that has a `SpotLightComponent`.

The following table shows some real-world scenarios, to better explain how you can use [`intensity`](spotlightcomponent/intensity.md) to control the brightness of the light in lumens, and [`attenuationRadius`](spotlightcomponent/attenuationradius.md) to control how the level of brightness diminishes with distance from the light source:

| Scenario | Approximate Lumens | Attenuation Radius | Description |
| --- | --- | --- | --- |
| Small Accent Spotlight | 100-200 lumens | 5-10 meters | Highlights small objects or artwork |
| LED flashlight | 300-600 lumens | 50-70 meters | Beams a long distance illumination |
| Theatrical Spotlight | 500-1,000 lumens | 20-40 meters | Focuses attention to performers on a stage |
| Outdoor Security Spotlight | 1,000-2,000 lumens | 20-30 meters | Brightly illuminates specific outdoor areas |
| Film/TV Production Spotlight | 5,000-10,000 lumens | 50-100 meters | Provides focused, high-intensity lighting for sets |
| Large-Scale Event Spotlight | 50,000-100,000 lumens | 200-500 meters | Lights large outdoor events or concerts |

## Topics

### Creating a spotlight
- [init(color: SpotLightComponent.Color, intensity: Float, innerAngleInDegrees: Float, outerAngleInDegrees: Float, attenuationRadius: Float)](spotlightcomponent/init(color:intensity:innerangleindegrees:outerangleindegrees:attenuationradius:)-483ep.md)
  Creates a spotlight with the given parameters.
- [init(color: SpotLightComponent.Color, intensity: Float, innerAngleInDegrees: Float, outerAngleInDegrees: Float, attenuationRadius: Float)](spotlightcomponent/init(color:intensity:innerangleindegrees:outerangleindegrees:attenuationradius:)-8u5j6.md)
  Creates a spotlight with the given parameters.
- [init(color: SpotLightComponent.Color, intensity: Float, innerAngleInDegrees: Float, outerAngleInDegrees: Float, attenuationRadius: Float, attenuationFalloffExponent: Float)](spotlightcomponent/init(color:intensity:innerangleindegrees:outerangleindegrees:attenuationradius:attenuationfalloffexponent:)-2klbp.md)
  Creates a spotlight with the given parameters.
- [init(color: SpotLightComponent.Color, intensity: Float, innerAngleInDegrees: Float, outerAngleInDegrees: Float, attenuationRadius: Float, attenuationFalloffExponent: Float)](spotlightcomponent/init(color:intensity:innerangleindegrees:outerangleindegrees:attenuationradius:attenuationfalloffexponent:)-4v8eh.md)
  Creates a spotlight with the given parameters.
### Setting the color
- [var color: SpotLightComponent.Color](spotlightcomponent/color-74jle.md)
  A color for the spotlight.
- [var color: SpotLightComponent.Color](spotlightcomponent/color-3e72t.md)
  A color for the spotlight.
### Configuring the spotlight
- [var intensity: Float](spotlightcomponent/intensity.md)
  The intensity of the spotlight measured in lumen.
- [var innerAngleInDegrees: Float](spotlightcomponent/innerangleindegrees.md)
  The inner angle of the spotlight in degrees.
- [var outerAngleInDegrees: Float](spotlightcomponent/outerangleindegrees.md)
  The outer angle of the spotlight in degrees.
- [var attenuationRadius: Float](spotlightcomponent/attenuationradius.md)
  The distance from the light source where its intensity reaches zero.
- [var attenuationFalloffExponent: Float](spotlightcomponent/attenuationfalloffexponent.md)
  The exponent value for the light’s intensity falloff-transition curve.
### Registering a components type
- [static func registerComponent()](spotlightcomponent/registercomponent.md)
  Registers a new component type.
### Comparing spotlight components
- [static func == (SpotLightComponent, SpotLightComponent) -> Bool](spotlightcomponent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](spotlightcomponent/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Supporting types
- [SpotLightComponent.Color](spotlightcomponent/color-swift.typealias.md)
  A platform-specific type used to define color for a spotlight.
### Structures
- [SpotLightComponent.Shadow](spotlightcomponent/shadow.md)
  A spotlight component that adds shadows to entities that it illuminates.
### Default Implementations
- [Component Implementations](spotlightcomponent/component-implementations.md)
- [Equatable Implementations](spotlightcomponent/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [SpotLightComponent.Shadow](spotlightcomponent/shadow.md)
  A spotlight component that adds shadows to entities that it illuminates.
- [SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/shadowclippingplane.md)
  An object that specifies the mode of a shadow clipping plane.
- [SpotLightComponent.Shadow.ShadowMapCullMode](spotlightcomponent/shadow/shadowmapcullmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent)*