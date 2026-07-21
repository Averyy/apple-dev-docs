# PortalComponent.BoundaryMode

**Framework**: RealityKit  
**Kind**: enum

A combination of clipping and crossing behaviors to apply to a portal boundary.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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
- [PortalComponent.BoundaryMode.disabled](portalcomponent/boundarymode/disabled.md)
  The portal renders without clipping or crossing.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarymode)*