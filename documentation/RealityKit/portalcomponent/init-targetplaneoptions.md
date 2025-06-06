# init(target:plane:options:)

**Framework**: RealityKit  
**Kind**: init

Creates a portal component with a target entity, a single planar definition, and portal options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(target: Entity, plane: PortalComponent.Plane, options: PortalComponent.Options)
```

#### Discussion

Use this initializer to toggle [`clippingMode`](portalcomponent/clippingmode-swift.property.md) and [`crossingMode`](portalcomponent/crossingmode-swift.property.md) with the same [`PortalComponent.Plane`](portalcomponent/plane.md).

## Parameters

- `target`: A target world entity the portal is looking into.
- `plane`: A plane for configuring clipping and crossing features.
- `options`: An option set that determines which clipping and crossing features to enable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/init(target:plane:options:))*