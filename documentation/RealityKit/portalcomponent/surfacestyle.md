# PortalComponent.SurfaceStyle

**Framework**: RealityKit  
**Kind**: struct

Describes the surface geometry of the portal mesh.

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

Passed to [`makePortal(surfaceStyle:boundaryStyle:boundaryMode:)`](portalcomponent/makeportal(surfacestyle:boundarystyle:boundarymode:).md) or [`configure(world:portalEntity:surfaceStyle:boundaryStyle:boundaryMode:)`](portalcomponent/configure(world:portalentity:surfacestyle:boundarystyle:boundarymode:).md) to define the flat plane mesh generated for the portal surface. It is independent of the clipping boundary.

## Topics

### Initializers
- [init(width: Float, height: Float)](portalcomponent/surfacestyle/init(width:height:).md)
  Creates a surface style with explicit width and height.
### Instance Properties
- [var height: Float](portalcomponent/surfacestyle/height.md)
  Portal mesh height in meters.
- [var width: Float](portalcomponent/surfacestyle/width.md)
  Portal mesh width in meters.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/surfacestyle)*