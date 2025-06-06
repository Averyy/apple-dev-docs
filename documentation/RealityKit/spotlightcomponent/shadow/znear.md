# zNear

**Framework**: RealityKit  
**Kind**: property

The near-plane of a shadow frustum.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var zNear: SpotLightComponent.Shadow.ShadowClippingPlane { get set }
```

#### Discussion

The `zNear` is the minimum distance between the light and a visible surface for casting shadows. The default value for `zNear` is [`SpotLightComponent.Shadow.ShadowClippingPlane.automatic`](spotlightcomponent/shadow/shadowclippingplane/automatic.md).

## See Also

- [var depthBias: Float](spotlightcomponent/shadow/depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var zFar: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/zfar.md)
  The orthogonal plane of the shadow frustum that’s furthest from the spotlight.
- [var cullModeOverride: SpotLightComponent.Shadow.ShadowMapCullMode?](spotlightcomponent/shadow/cullmodeoverride.md)
  The light’s culling mode for shadow map rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/znear)*