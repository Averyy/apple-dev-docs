# PortalComponent.CrossingMode.volume(_:)

**Framework**: RealityKit  
**Kind**: case

Allows contents within the portal to cross a box-shaped boundary.

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

Entities inside the portal world that have a [`PortalCrossingComponent`](portalcrossingcomponent.md) cross the faces of the box. Parts of a crossing entity inside the volume render as portal content, parts outside render in the host scene.

Use this case for room-sized portals and other bounded portal spaces. For portals where the box should enclose the portal surface, [`enclosingBox(depth:)`](portalcomponent/boundarystyle/enclosingbox(depth:).md) is a convenient way to configure this case alongside the matching [`PortalComponent.ClippingMode.volume(_:)`](portalcomponent/clippingmode-swift.enum/volume(_:).md).

## Parameters

- `volume`: A [`PortalComponent.Volume`](portalcomponent/volume.md) describing the box’s center and extents in portal-local space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/crossingmode-swift.enum/volume(_:))*