# PortalComponent.SurfaceStyle

**Framework**: RealityKit  
**Kind**: struct

The size of the flat plane mesh that RealityKit generates for a portal.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SurfaceStyle
```

#### Overview

The factory entry points [`makePortal(surfaceStyle:boundaryStyle:boundaryMode:)`](portalcomponent/makeportal(surfacestyle:boundarystyle:boundarymode:).md) and [`configure(world:portalEntity:surfaceStyle:boundaryStyle:boundaryMode:)`](portalcomponent/configure(world:portalentity:surfacestyle:boundarystyle:boundarymode:).md) use this value to build a [`ModelComponent`](modelcomponent.md) whose mesh is a plane on the entity’s local XY plane, centered at the entity’s origin.

The portal mesh size is independent of the clipping or crossing boundary, which you configure with [`PortalComponent.BoundaryStyle`](portalcomponent/boundarystyle.md).

## Topics

### Initializers
- [init(width: Float, height: Float)](portalcomponent/surfacestyle/init(width:height:).md)
  Creates a surface style with the given width and height in meters.
### Instance Properties
- [var height: Float](portalcomponent/surfacestyle/height.md)
  The height of the portal mesh, in meters, along the entity’s local Y axis.
- [var width: Float](portalcomponent/surfacestyle/width.md)
  The width of the portal mesh, in meters, along the entity’s local X axis.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/surfacestyle)*