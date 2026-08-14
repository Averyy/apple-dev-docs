# SpotLightComponent.Shadow

**Framework**: RealityKit  
**Kind**: struct

A spotlight component that adds shadows to entities that it illuminates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Shadow
```

## Topics

### Creating a shadow
- [init()](spotlightcomponent/shadow/init.md)
  Creates a new spot light shadow object.
- [init(layers: RenderLayer.Set?)](spotlightcomponent/shadow/init(layers:).md)
  Creates a spot light shadow that accepts shadow casters from the specified layers.
- [var layers: RenderLayer.Set?](spotlightcomponent/shadow/layers.md)
  The layers of entities that cast shadows from this light.
### Configuring the shadow
- [var depthBias: Float](spotlightcomponent/shadow/depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var zNear: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/znear.md)
  The near-plane of a shadow frustum.
- [var zFar: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/zfar.md)
  The orthogonal plane of the shadow frustum that’s furthest from the spotlight.
- [var cullModeOverride: SpotLightComponent.Shadow.ShadowMapCullMode?](spotlightcomponent/shadow/cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.
### Configuring shadow quality
- [var quality: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/quality.md)
  The shadow-filtering algorithm this light uses.
- [SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode.md)
  Constants that select the shadow-filtering algorithm a spotlight uses.
- [var lightSize: Float](spotlightcomponent/shadow/lightsize.md)
  The radius of the spotlight’s emitting surface, in meters.
### Type Aliases
- [SpotLightComponent.Shadow.ShadowMapCullMode](spotlightcomponent/shadow/shadowmapcullmode.md)
### Enumerations
- [SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/shadowclippingplane.md)
  An object that specifies the mode of a shadow clipping plane.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../swift/equatable.md)

## See Also

- [struct SpotLightComponent](spotlightcomponent.md)
  A component that defines a spotlight source.
- [SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/shadowclippingplane.md)
  An object that specifies the mode of a shadow clipping plane.
- [SpotLightComponent.Shadow.ShadowMapCullMode](spotlightcomponent/shadow/shadowmapcullmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow)*