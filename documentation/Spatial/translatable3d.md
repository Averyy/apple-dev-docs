# Translatable3D

**Framework**: Spatial  
**Kind**: protocol

A set of methods that defines the interface to translate Spatial entities.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol Translatable3D
```

## Topics

### Instance methods
- [func translate(by: Vector3D)](translatable3d/translate(by:)-6dj5o.md)
  Translates the entity by the specified vector.
- [func translated(by: Vector3D) -> Self](translatable3d/translated(by:)-5h847.md)
  Returns the entity that results from translating with the specified vector.
### Deprecated methods
- [func translate(by: Size3D)](translatable3d/translate(by:)-86nwy.md)
  Translates the entity by the specified size.
- [func translated(by: Size3D) -> Self](translatable3d/translated(by:)-9ndur.md)
  Returns the entity that results from translating with the specified size.

## Relationships

### Conforming Types
- [AffineTransform3D](affinetransform3d.md)
- [Point3D](point3d.md)
- [Pose3D](pose3d.md)
- [ProjectiveTransform3D](projectivetransform3d.md)
- [Ray3D](ray3d.md)
- [Rect3D](rect3d.md)
- [ScaledPose3D](scaledpose3d.md)

## See Also

- [protocol Primitive3D](primitive3d.md)
  A set of methods common to Spatial primitives.
- [protocol Rotatable3D](rotatable3d.md)
  A set of methods that defines the interface to rotate Spatial entities.
- [protocol Scalable3D](scalable3d.md)
  A set of methods that defines the interface to scale Spatial entities.
- [protocol Shearable3D](shearable3d.md)
  A set of methods that defines the interface to shear Spatial entities.
- [protocol Volumetric](volumetric.md)
  A set of methods for working with Spatial primitives with volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/translatable3d)*