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
  Creates a spot light shadow with the specified layers.
- [var layers: RenderLayer.Set?](spotlightcomponent/shadow/layers.md)
  The layers from which this light casts shadows. If nil, uses layers for shadow casting. Only entities whose RenderLayerComponent.layers intersect with these layers will cast shadows in this light’s shadow map. If `nil`, the light uses its `layers` for shadow casting. Set to an empty set to disable shadow casting entirely.
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
  The quality of the soft shadows this light casts.
- [SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode.md)
  The quality for the shadows. Low uses shadows that don’t change with light size and the distance between light-blocker-receiver Medium and high allow soft shadows with varying sample counts
- [var lightSize: Float](spotlightcomponent/shadow/lightsize.md)
  The light size that determines the softness of the shadows Larger size would mean a larger penumbra and a larger transition range from fully shadowed to lit. It is the radius of the light in world space units. It is also modulated by the attenaution radius, i.e., lights with larger attenuation radius need larger light size.
### Type Aliases
- [SpotLightComponent.Shadow.ShadowMapCullMode](spotlightcomponent/shadow/shadowmapcullmode.md)
### Enumerations
- [SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/shadowclippingplane.md)
  An object that specifies the mode of a shadow clipping plane.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct SpotLightComponent](spotlightcomponent.md)
  A component that defines a spotlight source.
- [SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/shadowclippingplane.md)
  An object that specifies the mode of a shadow clipping plane.
- [SpotLightComponent.Shadow.ShadowMapCullMode](spotlightcomponent/shadow/shadowmapcullmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow)*