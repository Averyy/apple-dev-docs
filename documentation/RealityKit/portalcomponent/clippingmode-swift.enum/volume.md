# PortalComponent.ClippingMode.volume(_:)

**Framework**: RealityKit  
**Kind**: case

Clips the contents within the portal to a box-shaped region.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.0+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case volume(PortalComponent.Volume)
```

#### Discussion

Use this case for room-sized portals and other bounded portal spaces where content shouldn’t extend infinitely behind the portal surface. RealityKit hides any portal world content outside the volume.

For portals where the box should enclose the portal surface, [`enclosingBox(depth:)`](portalcomponent/boundarystyle/enclosingbox(depth:).md) is a convenient way to configure this case alongside the matching [`PortalComponent.CrossingMode.volume(_:)`](portalcomponent/crossingmode-swift.enum/volume(_:).md).

## Parameters

- `volume`: A [`PortalComponent.Volume`](portalcomponent/volume.md) describing the box’s center and extents in portal-local space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/clippingmode-swift.enum/volume(_:))*