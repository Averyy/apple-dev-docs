# cullModeOverride

**Framework**: RealityKit  
**Kind**: property

The light’s culling mode for shadow map rendering.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var cullModeOverride: SpotLightComponent.Shadow.ShadowMapCullMode? { get set }
```

## See Also

- [var depthBias: Float](spotlightcomponent/shadow/depthbias.md)
  A constant value that RealityKit applies as a bias to its shadow calculations.
- [var zNear: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/znear.md)
  The near-plane of a shadow frustum.
- [var zFar: SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/zfar.md)
  The orthogonal plane of the shadow frustum that’s furthest from the spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/cullmodeoverride)*