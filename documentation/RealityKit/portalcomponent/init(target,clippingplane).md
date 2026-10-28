# init(target:clippingPlane:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a portal component with a target entity and an optional clipping plane.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
init(target: Entity, clippingPlane: PortalComponent.ClippingPlane? = nil)
```

## Discussion

This initializes the [`PortalComponent`](../portalcomponent.md) with the given target entity, and an optional clipping plane. The target entity needs a [`WorldComponent`](../worldcomponent.md) in its component set.

To render a portal, an entity needs a [`PortalComponent`](../portalcomponent.md) and a [`ModelComponent`](../modelcomponent.md), using one or more [`PortalMaterial`](../portalmaterial.md) instances.

This initializer is equivalent to setting [`clippingMode`](./clippingmode-swift.property.md) with the corresponding [`PortalComponent.Plane`](./plane.md), leaving [`crossingMode`](./crossingmode-swift.property.md) at [`PortalComponent.CrossingMode.disabled`](./crossingmode-swift.enum/disabled.md).

For new code, prefer [`init(target:clippingMode:crossingMode:)`](./init%28target,clippingmode,crossingmode%29.md), which lets you configure clipping and crossing together and supports volumetric boundaries.

## Parameters

- `target`: A target world entity the portal is looking into.
- `clippingPlane`: A planar representation of a portal to enable the clipping feature. When `nil`, [`clippingMode`](./clippingmode-swift.property.md) is [`PortalComponent.ClippingMode.disabled`](./clippingmode-swift.enum/disabled.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/init(target:clippingplane:))*