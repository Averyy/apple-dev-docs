# PortalComponent.Volume

**Framework**: RealityKit  
**Kind**: struct

A box-shaped region in portal-local space that defines a volumetric portal boundary.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Volume
```

#### Overview

Pair this type with [`PortalComponent.ClippingMode.volume(_:)`](portalcomponent/clippingmode-swift.enum/volume(_:).md) to clip portal world content to a box, or with [`PortalComponent.CrossingMode.volume(_:)`](portalcomponent/crossingmode-swift.enum/volume(_:).md) to allow crossing entities to pass through the box’s faces.

[`PortalComponent.Volume`](portalcomponent/volume.md) describes an axis-aligned box in the portal entity’s local coordinate space. The box is centered at [`position`](portalcomponent/volume/position.md) and spans the full lengths given by [`extents`](portalcomponent/volume/extents.md) along each axis. [`extents`](portalcomponent/volume/extents.md) are full extents, not half-extents — a volume with `extents = [1, 1, 1]` is a one-cubic-meter box.

For typical room-sized portals where the box should enclose the portal surface, prefer [`enclosingBox(depth:)`](portalcomponent/boundarystyle/enclosingbox(depth:).md), which derives the X and Y extents from the portal’s [`PortalComponent.SurfaceStyle`](portalcomponent/surfacestyle.md) for you.

## Topics

### Creating a volume
- [init(position: SIMD3<Float>, extents: SIMD3<Float>)](portalcomponent/volume/init(position:extents:).md)
  Creates a volume with the given center position and extents.
### Configuring the extents
- [var extents: SIMD3<Float>](portalcomponent/volume/extents.md)
  The full lengths of the volume along the X, Y, and Z axes of portal-local space, in meters.
### Instance Properties
- [var position: SIMD3<Float>](portalcomponent/volume/position.md)
  The center of the volume in portal-local space, in meters.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/volume)*