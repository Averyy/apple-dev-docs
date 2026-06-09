# PortalFactory.Style.plane(width:height:radius:)

**Framework**: RealityKit  
**Kind**: case

A flat or curved planar portal.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case plane(width: Float, height: Float, radius: Float = 0.0)
```

#### Discussion

Creates a rectangular portal that can be flat or curved into a cylindrical shape. The portal surface uses a plane mesh generated with `MeshResource.generatePlane`.

#### Coordinate Space

The portal plane is positioned at the entity’s local origin `[0, 0, 0]` with a normal facing the positive Z direction `[0, 0, 1]`.

## Parameters

- `width`: The width of the portal plane in meters. Must be positive.
- `height`: The height of the portal plane in meters. Must be positive.
- `radius`: The radius of curvature. Zero creates a flat plane (default), positive values create a cylindrical curved portal. Must be non-negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalfactory/style/plane(width:height:radius:))*