# PortalComponent.Portal

**Framework**: RealityKit  
**Kind**: struct

A pair of related entities that make up a configured portal.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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