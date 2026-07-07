# PortalComponent.BoundaryMode

**Framework**: RealityKit  
**Kind**: enum

Controls whether a portal clips portal content, enables entity crossing, both, or neither.

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

This is an enum rather than an `OptionSet` because the cases represent explicitly named semantic states. Future cases may carry associated values (e.g. per-mode parameters), which is incompatible with `OptionSet`.

## Topics

### Enumeration Cases
- [PortalComponent.BoundaryMode.clippingAndCrossing](portalcomponent/boundarymode/clippingandcrossing.md)
  Portal content is clipped and entities cross the boundary.
- [PortalComponent.BoundaryMode.clippingOnly](portalcomponent/boundarymode/clippingonly.md)
  Portal content is clipped to the boundary. Entities do not cross.
- [PortalComponent.BoundaryMode.crossingOnly](portalcomponent/boundarymode/crossingonly.md)
  Entities with `PortalCrossingComponent` cross the boundary. Content is not clipped.
- [PortalComponent.BoundaryMode.disabled](portalcomponent/boundarymode/disabled.md)
  Content is not clipped and entities do not cross the portal boundary.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarymode)*