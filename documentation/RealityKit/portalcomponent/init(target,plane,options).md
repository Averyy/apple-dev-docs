# init(target:plane:options:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a portal component with a target entity, a single planar definition, and portal options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(target: Entity, plane: PortalComponent.Plane, options: PortalComponent.Options)
```

#### Discussion

Use this initializer to toggle [`clippingMode`](./clippingmode-swift.property.md) and [`crossingMode`](./crossingmode-swift.property.md) with the same [`PortalComponent.Plane`](./plane.md).

For new code, prefer [`init(target:clippingMode:crossingMode:)`](./init%28target,clippingmode,crossingmode%29.md), which lets you configure clipping and crossing independently and supports [`PortalComponent.ClippingMode.volume(_:)`](./clippingmode-swift.enum/volume%28_%29.md) and [`PortalComponent.CrossingMode.volume(_:)`](./crossingmode-swift.enum/volume%28_%29.md) for box-shaped boundaries.

## Parameters

- `target`: A target world entity the portal is looking into.
- `plane`: A plane for configuring clipping and crossing features.
- `options`: An option set that determines which clipping and crossing features to enable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/init(target:plane:options:))*