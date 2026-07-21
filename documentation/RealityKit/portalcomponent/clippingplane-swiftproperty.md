# clippingPlane

**Framework**: RealityKit  
**Kind**: property

The clipping plane of the portal, in the entity’s local coordinates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var clippingPlane: PortalComponent.ClippingPlane? { get set }
```

#### Discussion

When you set this property to a non-`nil` value, the portal clips meshes inside the portal world that are in front of the clipping plane.

This property is a convenience that maps onto the more general [`clippingMode`](portalcomponent/clippingmode-swift.property.md). Reading it returns a value only when [`clippingMode`](portalcomponent/clippingmode-swift.property.md) is [`PortalComponent.ClippingMode.plane(_:)`](portalcomponent/clippingmode-swift.enum/plane(_:).md); for [`PortalComponent.ClippingMode.disabled`](portalcomponent/clippingmode-swift.enum/disabled.md) or [`PortalComponent.ClippingMode.volume(_:)`](portalcomponent/clippingmode-swift.enum/volume(_:).md), it returns `nil`.

For new code, prefer [`clippingMode`](portalcomponent/clippingmode-swift.property.md) directly. It supports [`PortalComponent.ClippingMode.volume(_:)`](portalcomponent/clippingmode-swift.enum/volume(_:).md) for box-shaped clipping boundaries and pairs naturally with [`crossingMode`](portalcomponent/crossingmode-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/clippingplane-swift.property)*