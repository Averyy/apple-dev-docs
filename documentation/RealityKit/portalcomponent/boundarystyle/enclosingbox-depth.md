# enclosingBox(depth:)

**Framework**: RealityKit  
**Kind**: method

Portal with box-bounded clipping and crossing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func enclosingBox(depth: Float) -> PortalComponent.BoundaryStyle
```

#### Discussion

Content inside the portal world is clipped to a box volume. The box X and Y extents are taken from the accompanying `SurfaceStyle`. Entities with `PortalCrossingComponent` cross the box boundary rather than the plane.

Corresponds to `ClippingMode.volume(_:)` and `CrossingMode.volume(_:)`.

The box is always centered at the portal entity’s origin. To offset the box, use [`PortalComponent.ClippingMode.volume(_:)`](portalcomponent/clippingmode-swift.enum/volume(_:).md) and [`PortalComponent.CrossingMode.volume(_:)`](portalcomponent/crossingmode-swift.enum/volume(_:).md) directly with a `Volume` that has a non-zero `position`.

## Parameters

- `depth`: Depth of the enclosing box in meters (box extent Z)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarystyle/enclosingbox(depth:))*