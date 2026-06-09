# PortalComponent.Volume

**Framework**: RealityKit  
**Kind**: struct

Defines the geometry of a volumetric (box) portal boundary.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Volume
```

#### Overview

Use this type with [`PortalComponent.ClippingMode.volume(_:)`](portalcomponent/clippingmode-swift.enum/volume(_:).md) and [`PortalComponent.CrossingMode.volume(_:)`](portalcomponent/crossingmode-swift.enum/volume(_:).md) to define a box-bounded portal space.

All geometry is specified in portal-local space.

## Topics

### Creating a volume
- [init(position: SIMD3<Float>, extents: SIMD3<Float>)](portalcomponent/volume/init(position:extents:).md)
  Creates a volume with the given center position and extents.
### Configuring the extents
- [var extents: SIMD3<Float>](portalcomponent/volume/extents.md)
  The size of the volume along the X, Y, and Z axes of portal-local space.
### Instance Properties
- [var position: SIMD3<Float>](portalcomponent/volume/position.md)
  The center position of the volume in portal-local space.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/volume)*