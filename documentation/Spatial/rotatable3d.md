# Rotatable3D

**Framework**: Spatial  
**Kind**: protocol

A set of methods that defines the interface to rotate Spatial entities.

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
protocol Rotatable3D
```

## Topics

### Instance methods
- [func rotate(by: simd_quatd)](rotatable3d/rotate(by:)-usrg.md)
  Rotates the entity by a quaternion.
- [func rotate(by: Rotation3D)](rotatable3d/rotate(by:)-1g3rl.md)
  Rotates the entity by an angle over an axis.
- [func rotated(by: simd_quatd) -> Self](rotatable3d/rotated(by:)-4gdqe.md)
  Returns the entity that a quaternion rotates.
- [func rotated(by: Rotation3D) -> Self](rotatable3d/rotated(by:)-7bx4w.md)
  Returns the entity that results from applying the specified rotation.

## Relationships

### Conforming Types
- [AffineTransform3D](affinetransform3d.md)
- [Point3D](point3d.md)
- [Pose3D](pose3d.md)
- [ProjectiveTransform3D](projectivetransform3d.md)
- [Ray3D](ray3d.md)
- [Rect3D](rect3d.md)
- [Rotation3D](rotation3d.md)
- [ScaledPose3D](scaledpose3d.md)
- [Size3D](size3d.md)
- [Vector3D](vector3d.md)

## See Also

- [protocol Primitive3D](primitive3d.md)
  A set of methods common to Spatial primitives.
- [protocol Scalable3D](scalable3d.md)
  A set of methods that defines the interface to scale Spatial entities.
- [protocol Shearable3D](shearable3d.md)
  A set of methods that defines the interface to shear Spatial entities.
- [protocol Translatable3D](translatable3d.md)
  A set of methods that defines the interface to translate Spatial entities.
- [protocol Volumetric](volumetric.md)
  A set of methods for working with Spatial primitives with volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotatable3d)*