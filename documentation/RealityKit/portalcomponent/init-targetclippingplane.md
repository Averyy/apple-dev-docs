# init(target:clippingPlane:)

**Framework**: RealityKit  
**Kind**: init

Creates a portal component with a target entity and a clipping plane.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
init(target: Entity, clippingPlane: PortalComponent.ClippingPlane? = nil)
```

#### Discussion

This initializes the [`PortalComponent`](portalcomponent.md) with the given target entity, and an optional clipping plane. The target entity needs a [`WorldComponent`](worldcomponent.md) in its component set.

To render a portal, an entity needs a [`PortalComponent`](portalcomponent.md) and a [`ModelComponent`](modelcomponent.md), using one or more [`PortalMaterial`](portalmaterial.md) instances.

This initializer is equivalent to setting [`clippingMode`](portalcomponent/clippingmode-swift.property.md) with the same [`PortalComponent.Plane`](portalcomponent/plane.md).

## Parameters

- `target`: A target world entity the portal is looking into.
- `clippingPlane`: A planar representation of a portal to enable the clipping feature.   When  ,   is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/init(target:clippingplane:))*