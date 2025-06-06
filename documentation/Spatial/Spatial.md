# Spatial

**Framework**: Spatial  
**Kind**: module

Create and manipulate 3D mathematical primitives.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

#### Overview

The Spatial module is a lightweight 3D mathematical library that provides a simple API for working with 3D primitives. Much of its functionality is similar to the 2D geometry support in Core Graphics, but in three dimensions.

## Topics

### Data structures
- [struct Vector3D](vector3d.md)
  A three-element vector.
- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
### 2D primitives
- [struct Angle2D](angle2d.md)
  A geometric angle with a value you access in either radians or degrees.
### 3D primitives
- [struct Point3D](point3d.md)
  A point in a 3D coordinate system.
- [struct Size3D](size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
- [struct Rect3D](rect3d.md)
  A rectangle in a 3D coordinate system.
- [struct Rotation3D](rotation3d.md)
  A rotation in three dimensions.
- [struct RotationAxis3D](rotationaxis3d.md)
  A 3D rotation axis.
- [struct Pose3D](pose3d.md)
  A structure that contains a 3D position and a 3D rotation.
- [struct ScaledPose3D](scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct Ray3D](ray3d.md)
  A ray in a 3D coordinate system.
### Affine and projective transforms
- [struct AffineTransform3D](affinetransform3d.md)
  A 3D affine transformation matrix.
- [struct ProjectiveTransform3D](projectivetransform3d.md)
  A 3D projective transformation matrix.
### Protocols
- [protocol Primitive3D](primitive3d.md)
  A set of methods common to Spatial primitives.
- [protocol Rotatable3D](rotatable3d.md)
  A set of methods that defines the interface to rotate Spatial entities.
- [protocol Scalable3D](scalable3d.md)
  A set of methods that defines the interface to scale Spatial entities.
- [protocol Shearable3D](shearable3d.md)
  A set of methods that defines the interface to shear Spatial entities.
- [protocol Translatable3D](translatable3d.md)
  A set of methods that defines the interface to translate Spatial entities.
- [protocol Volumetric](volumetric.md)
  A set of methods for working with Spatial primitives with volume.
### Macros
- [Macros & Global Variables](spatial-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Spatial)*