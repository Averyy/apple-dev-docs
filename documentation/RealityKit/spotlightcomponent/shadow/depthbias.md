# depthBias

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A constant value that RealityKit applies as a bias to its shadow calculations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var depthBias: Float { get set }
```

#### Discussion

Reduce visual effects such as *shadow acne*, by adjusting this property. The default value is `1.0`.

## See Also

### Configuring the shadow
- [var zNear: SpotLightComponent.Shadow.ShadowClippingPlane](./znear.md)
  The near-plane of a shadow frustum.
- [var zFar: SpotLightComponent.Shadow.ShadowClippingPlane](./zfar.md)
  The orthogonal plane of the shadow frustum that’s furthest from the spotlight.
- [var cullModeOverride: SpotLightComponent.Shadow.ShadowMapCullMode?](./cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/depthbias)*