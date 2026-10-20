# PortalComponent.BoundaryStyle

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The shape of a portal’s clipping and crossing boundary.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct BoundaryStyle
```

#### Overview

A portal has two related but separate concepts:

- The *surface*, a flat plane mesh that RealityKit renders with [`PortalMaterial`](../portalmaterial.md) and sizes from [`PortalComponent.SurfaceStyle`](./surfacestyle.md).
- The *boundary*, the volume in space that clips portal world content and that crossing entities pass through. [`PortalComponent.BoundaryStyle`](./boundarystyle.md) describes the shape of that volume.

Pair a boundary style with a [`PortalComponent.BoundaryMode`](./boundarymode.md) to control whether the boundary clips content, allows entities to cross, both, or neither.

## Topics

### Type Methods
- [static func enclosingBox(depth: Float) -> PortalComponent.BoundaryStyle](./boundarystyle/enclosingbox%28depth%29.md)
  Returns a boundary style that uses a box enclosing the portal surface.
- [static func infinitePlane() -> PortalComponent.BoundaryStyle](./boundarystyle/infiniteplane%28%29.md)
  Returns a boundary style that uses an infinite plane.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarystyle)*