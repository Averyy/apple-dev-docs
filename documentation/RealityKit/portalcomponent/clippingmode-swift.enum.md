# PortalComponent.ClippingMode

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Specifies the mode of clipping for a portal.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum ClippingMode
```

#### Overview

This type can be passed into [`clippingMode`](./clippingmode-swift.property.md) to configure the portal component’s clipping feature.

With [`PortalComponent.ClippingMode.disabled`](./clippingmode-swift.enum/disabled.md), contents in portal world are not clipped.

With [`PortalComponent.ClippingMode.plane(_:)`](./clippingmode-swift.enum/plane%28_%29.md), contents within portal are clipped by a plane.

With [`PortalComponent.ClippingMode.volume(_:)`](./clippingmode-swift.enum/volume%28_%29.md), contents within portal are clipped by a volumetric box.

## Topics

### Clipping to a volume
- [PortalComponent.ClippingMode.volume(_:)](./clippingmode-swift.enum/volume%28_%29.md)
  Clips the contents within the portal to a box-shaped region.
### Enumeration Cases
- [PortalComponent.ClippingMode.disabled](./clippingmode-swift.enum/disabled.md)
  Disables clipping of the contents within the portal.
- [PortalComponent.ClippingMode.plane(_:)](./clippingmode-swift.enum/plane%28_%29.md)
  Clips the contents within the portal by the edge of the plane.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/clippingmode-swift.enum)*