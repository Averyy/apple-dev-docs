# SpotLightComponent.Shadow

**Framework**: RealityKit  
**Kind**: struct

A spotlight component that adds shadows to entities that it illuminates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 2.0+

## Declaration

```swift
struct Shadow
```

## Topics

### Creating a shadow
- [init()](spotlightcomponent/shadow/init.md)
  Creates a new spot light shadow object.
### Configuring the shadow
- [var depthBias: Float](spotlightcomponent/shadow/depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var zNear: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/znear.md)
  The near-plane of a shadow frustum.
- [var zFar: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/zfar.md)
  The orthogonal plane of the shadow frustum that’s furthest from the spotlight.
- [var cullModeOverride: SpotLightComponent.Shadow.ShadowMapCullMode?](spotlightcomponent/shadow/cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.
### Registering a component type
- [static func registerComponent()](spotlightcomponent/shadow/registercomponent.md)
  Registers a new component type.
### Comparing shadows
- [static func == (SpotLightComponent.Shadow, SpotLightComponent.Shadow) -> Bool](spotlightcomponent/shadow/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](spotlightcomponent/shadow/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Type Aliases
- [SpotLightComponent.Shadow.ShadowMapCullMode](spotlightcomponent/shadow/shadowmapcullmode.md)
### Enumerations
- [SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/shadowclippingplane.md)
  An object that specifies the mode of a shadow clipping plane.
### Default Implementations
- [Component Implementations](spotlightcomponent/shadow/component-implementations.md)
- [Equatable Implementations](spotlightcomponent/shadow/equatable-implementations.md)

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