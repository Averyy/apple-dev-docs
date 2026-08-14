# PortalComponent.BoundaryStyle

**Framework**: RealityKit  
**Kind**: struct

The shape of a portal’s clipping and crossing boundary.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BoundaryStyle
```

#### Overview

A portal has two related but separate concepts:

- The *surface*, a flat plane mesh that RealityKit renders with [`PortalMaterial`](portalmaterial.md) and sizes from [`PortalComponent.SurfaceStyle`](portalcomponent/surfacestyle.md).
- The *boundary*, the volume in space that clips portal world content and that crossing entities pass through. [`PortalComponent.BoundaryStyle`](portalcomponent/boundarystyle.md) describes the shape of that volume.

Pair a boundary style with a [`PortalComponent.BoundaryMode`](portalcomponent/boundarymode.md) to control whether the boundary clips content, allows entities to cross, both, or neither.

## Topics

### Type Methods
- [static func enclosingBox(depth: Float) -> PortalComponent.BoundaryStyle](portalcomponent/boundarystyle/enclosingbox(depth:).md)
  Returns a boundary style that uses a box enclosing the portal surface.
- [static func infinitePlane() -> PortalComponent.BoundaryStyle](portalcomponent/boundarystyle/infiniteplane.md)
  Returns a boundary style that uses an infinite plane.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarystyle)*