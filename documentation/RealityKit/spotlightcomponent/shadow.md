# SpotLightComponent.Shadow

**Framework**: RealityKit  
**Kind**: struct

A spotlight component that adds shadows to entities that it illuminates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct Shadow
```

## Topics

### Creating a shadow
- [init()](spotlightcomponent/shadow/init.md)
  Creates a new spot light shadow object.
### Instance Properties
- [var cullModeOverride: SpotLightComponent.Shadow.ShadowMapCullMode?](spotlightcomponent/shadow/cullmodeoverride-2tfql.md)
  The light’s culling mode for shadow map rendering.
- [var cullModeOverride: SpotLightComponent.Shadow.ShadowMapCullMode?](spotlightcomponent/shadow/cullmodeoverride-5k4x0.md)
  The light’s culling mode for shadow map rendering.
- [var depthBias: Float](spotlightcomponent/shadow/depthbias-9guxp.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var depthBias: Float](spotlightcomponent/shadow/depthbias-tpq0.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var zFar: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/zfar-6a4wu.md)
  The orthogonal plane of the shadow frustum that’s furthest from the spotlight.
- [var zFar: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/zfar-7e70l.md)
  The orthogonal plane of the shadow frustum that’s furthest from the spotlight.
- [var zNear: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/znear-4b0cv.md)
  The near-plane of a shadow frustum.
- [var zNear: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/znear-540d0.md)
  The near-plane of a shadow frustum.
### Type Aliases
- [SpotLightComponent.Shadow.ShadowMapCullMode](spotlightcomponent/shadow/shadowmapcullmode-2mkih.md)
- [SpotLightComponent.Shadow.ShadowMapCullMode](spotlightcomponent/shadow/shadowmapcullmode-35vi3.md)
### Enumerations
- [SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/shadowclippingplane-3b4xa.md)
  An object that specifies the mode of a shadow clipping plane.
- [SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/shadowclippingplane-6s3gy.md)
  An object that specifies the mode of a shadow clipping plane.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct SpotLightComponent](spotlightcomponent.md)
  A component that defines a spotlight source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow)*