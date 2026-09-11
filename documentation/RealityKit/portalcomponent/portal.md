# PortalComponent.Portal

**Framework**: RealityKit  
**Kind**: struct

A pair of related entities that make up a configured portal.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Portal
```

#### Overview

[`makePortal(surfaceStyle:boundaryStyle:boundaryMode:)`](portalcomponent/makeportal(surfacestyle:boundarystyle:boundarymode:).md) returns this value. You’re responsible for adding both entities to your scene.

## Topics

### Instance Properties
- [let portalEntity: Entity](portalcomponent/portal/portalentity.md)
  The entity that has the portal surface mesh, [`PortalMaterial`](portalmaterial.md), and [`PortalComponent`](portalcomponent.md).
- [let worldEntity: Entity](portalcomponent/portal/worldentity.md)
  The entity that has [`WorldComponent`](worldcomponent.md). Add portal world content as descendants of this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/portal)*