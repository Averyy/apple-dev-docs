# zFar

**Framework**: RealityKit  
**Kind**: property

The orthogonal plane of the shadow frustum that’s furthest from the spotlight.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var zFar: SpotLightComponent.Shadow.ShadowClippingPlane { get set }
```

#### Discussion

The `zFar` is the maximum distance between the light and a visible surface for casting shadows.

The spotlight applies the value from [`attenuationRadius`](spotlightcomponent/attenuationradius.md), when you set this property to `ShadowClippingPlane/automatic`, which is its default value. Setting this value to `ShadowClippingPlane/fixed(_:)` is equivalent to assigning it to `min(zFar, attenuationRadius)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/zfar-6a4wu)*