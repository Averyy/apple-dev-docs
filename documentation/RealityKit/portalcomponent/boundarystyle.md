# PortalComponent.BoundaryStyle

**Framework**: RealityKit  
**Kind**: struct

Describes the clipping and crossing boundary shape for a portal.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BoundaryStyle
```

#### Overview

The flat plane mesh rendered for the portal is always sized by `SurfaceStyle`. `BoundaryStyle` controls how `ClippingMode` and `CrossingMode` are configured.

## Topics

### Type Methods
- [static func enclosingBox(depth: Float) -> PortalComponent.BoundaryStyle](portalcomponent/boundarystyle/enclosingbox(depth:).md)
  Portal with box-bounded clipping and crossing.
- [static func infinitePlane() -> PortalComponent.BoundaryStyle](portalcomponent/boundarystyle/infiniteplane.md)
  Portal with infinite half-space clipping and crossing.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarystyle)*