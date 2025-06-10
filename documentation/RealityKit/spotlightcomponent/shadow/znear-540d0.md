# zNear

**Framework**: RealityKit  
**Kind**: property

The near-plane of a shadow frustum.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var zNear: SpotLightComponent.Shadow.ShadowClippingPlane { get set }
```

#### Discussion

The `zNear` is the minimum distance between the light and a visible surface for casting shadows. The default value for `zNear` is `ShadowClippingPlane/automatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/znear-540d0)*