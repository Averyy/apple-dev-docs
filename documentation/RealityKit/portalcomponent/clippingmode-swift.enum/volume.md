# PortalComponent.ClippingMode.volume(_:)

**Framework**: RealityKit  
**Kind**: case

Clips the contents within the portal using a volumetric box.

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

The volume is defined by a box with position and extents in portal-local space. This is useful for room portals and bounded portal spaces.

## Parameters

- `volume`: A [`PortalComponent.Volume`](portalcomponent/volume.md) describing the box position and extents


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/clippingmode-swift.enum/volume(_:))*