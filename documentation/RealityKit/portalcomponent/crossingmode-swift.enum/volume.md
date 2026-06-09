# PortalComponent.CrossingMode.volume(_:)

**Framework**: RealityKit  
**Kind**: case

Allows contents within the portal to cross using a volumetric box.

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

Entities with `PortalCrossingComponent` will cross the box boundary. Parts of entities inside the volume render as portal content, parts outside render normally.

## Parameters

- `volume`: A [`PortalComponent.Volume`](portalcomponent/volume.md) describing the box position and extents


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/crossingmode-swift.enum/volume(_:))*