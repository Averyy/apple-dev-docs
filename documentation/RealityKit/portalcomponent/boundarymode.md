# PortalComponent.BoundaryMode

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

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

## Overview

Pass this value to the factory entry points to configure [`clippingMode`](./clippingmode-swift.property.md) and [`crossingMode`](./crossingmode-swift.property.md) together.

## Topics

### Enumeration Cases
- [PortalComponent.BoundaryMode.clippingAndCrossing](./boundarymode/clippingandcrossing.md)
  The portal clips its content to the boundary, and entities with [`PortalCrossingComponent`](../portalcrossingcomponent.md) cross the boundary.
- [PortalComponent.BoundaryMode.clippingOnly](./boundarymode/clippingonly.md)
  The portal clips its content to the boundary.
- [PortalComponent.BoundaryMode.crossingOnly](./boundarymode/crossingonly.md)
  Entities with [`PortalCrossingComponent`](../portalcrossingcomponent.md) cross the boundary.
- [PortalComponent.BoundaryMode.none](./boundarymode/none.md)
  The portal renders without clipping or crossing.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarymode)*