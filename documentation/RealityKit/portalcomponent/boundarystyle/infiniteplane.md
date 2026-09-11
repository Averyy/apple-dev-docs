# infinitePlane()

**Framework**: RealityKit  
**Kind**: method

Returns a boundary style that uses an infinite plane.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func infinitePlane() -> PortalComponent.BoundaryStyle
```

#### Discussion

The boundary is the entity’s local XY plane. RealityKit clips portal world content behind the surface and lets crossing entities pass through it freely.

This boundary corresponds to [`PortalComponent.ClippingMode.plane(_:)`](portalcomponent/clippingmode-swift.enum/plane(_:).md) and [`PortalComponent.CrossingMode.plane(_:)`](portalcomponent/crossingmode-swift.enum/plane(_:).md) configured with [`positiveZ`](portalcomponent/plane/positivez.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarystyle/infiniteplane())*