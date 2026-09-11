# PortalComponent.BoundaryMode

**Framework**: RealityKit  
**Kind**: enum

A combination of clipping and crossing behaviors to apply to a portal boundary.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum BoundaryMode
```

#### Overview

Pass this value to the factory entry points to configure [`clippingMode`](portalcomponent/clippingmode-swift.property.md) and [`crossingMode`](portalcomponent/crossingmode-swift.property.md) together.

## Topics

### Enumeration Cases
- [PortalComponent.BoundaryMode.clippingAndCrossing](portalcomponent/boundarymode/clippingandcrossing.md)
  The portal clips its content to the boundary, and entities with [`PortalCrossingComponent`](portalcrossingcomponent.md) cross the boundary.
- [PortalComponent.BoundaryMode.clippingOnly](portalcomponent/boundarymode/clippingonly.md)
  The portal clips its content to the boundary.
- [PortalComponent.BoundaryMode.crossingOnly](portalcomponent/boundarymode/crossingonly.md)
  Entities with [`PortalCrossingComponent`](portalcrossingcomponent.md) cross the boundary.
- [PortalComponent.BoundaryMode.none](portalcomponent/boundarymode/none.md)
  The portal renders without clipping or crossing.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarymode)*