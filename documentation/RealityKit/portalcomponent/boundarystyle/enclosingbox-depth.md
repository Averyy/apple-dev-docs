# enclosingBox(depth:)

**Framework**: RealityKit  
**Kind**: method

Returns a boundary style that uses a box enclosing the portal surface.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func enclosingBox(depth: Float) -> PortalComponent.BoundaryStyle
```

#### Discussion

The box is centered on the portal entity’s origin. Its X and Y extents come from the accompanying [`PortalComponent.SurfaceStyle`](portalcomponent/surfacestyle.md); its Z extent is the `depth` you provide.

Use this style for room-sized portals and other bounded portal spaces where content shouldn’t extend infinitely behind the surface. Entities with [`PortalCrossingComponent`](portalcrossingcomponent.md) cross the box’s faces rather than an infinite plane.

This boundary corresponds to [`PortalComponent.ClippingMode.volume(_:)`](portalcomponent/clippingmode-swift.enum/volume(_:).md) and [`PortalComponent.CrossingMode.volume(_:)`](portalcomponent/crossingmode-swift.enum/volume(_:).md). To offset the box from the portal entity’s origin, configure those modes directly with a [`PortalComponent.Volume`](portalcomponent/volume.md) that has a non-zero `position`.

## Parameters

- `depth`: The depth of the box in meters, along the entity’s local Z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarystyle/enclosingbox(depth:))*