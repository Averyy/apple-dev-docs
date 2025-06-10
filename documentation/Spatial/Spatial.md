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
- [struct Vector3DFloat](vector3dfloat.md)
  A single-precision structure that defines a three-element vector
- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
### 2D primitives
- [struct Angle2D](angle2d.md)
  A geometric angle with a value you access in either radians or degrees.
- [struct Angle2DFloat](angle2dfloat.md)
  A single-precision geometric angle whose value you access in either radians or degrees.
### 3D primitives
- [struct Point3D](point3d.md)
  A point in a 3D coordinate system.
- [struct Point3DFloat](point3dfloat.md)
  A single-precision structure that contains a point in a three-dimensional coordinate system.
- [struct Size3D](size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
- [struct Size3DFloat](size3dfloat.md)
  A single-precision structure that contains width, height, and depth values.
- [struct Rect3D](rect3d.md)
  A rectangle in a 3D coordinate system.
- [struct Rect3DFloat](rect3dfloat.md)
  A single-precision structure that contains the location and dimensions of a 3D rectangle.
- [struct Rotation3D](rotation3d.md)
  A rotation in three dimensions.
- [struct Rotation3DFloat](rotation3dfloat.md)
  A single-precision structure that represents a rotation in three dimensions.
- [struct RotationAxis3D](rotationaxis3d.md)
  A 3D rotation axis.
- [struct RotationAxis3DFloat](rotationaxis3dfloat.md)
  A 3D axis.
- [struct Pose3D](pose3d.md)
  A structure that contains a 3D position and a 3D rotation.
- [struct Pose3DFloat](pose3dfloat.md)
  A single-precision structure that contains a position and rotation.
- [struct ScaledPose3D](scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct ScaledPose3DFloat](scaledpose3dfloat.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct SphericalCoordinates3DFloat](sphericalcoordinates3dfloat.md)
  A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct Ray3D](ray3d.md)
  A ray in a 3D coordinate system.
- [struct Ray3DFloat](ray3dfloat.md)
  A single-precision structure that contains the origin and direction of a 3D ray.
### Affine and projective transforms
- [struct AffineTransform3D](affinetransform3d.md)
  A 3D affine transformation matrix.
- [struct AffineTransform3DFloat](affinetransform3dfloat.md)
- [struct ProjectiveTransform3D](projectivetransform3d.md)
  A 3D projective transformation matrix.
- [struct ProjectiveTransform3DFloat](projectivetransform3dfloat.md)
  A single-precision 3D projective transformation matrix.
### Converting between coordinate spaces
- [protocol CoordinateSpace3D](coordinatespace3d.md)
  A type that represents a coordinate space which you can use to convert values to and from other coordinate spaces.
- [protocol CoordinateSpace3DFloat](coordinatespace3dfloat.md)
- [protocol CoordinateSpaceValue3D](coordinatespacevalue3d.md)
  An opaque value which can be resolved to a concrete value in a `CoordinateSpace3D`
- [protocol ProjectiveTransformable3D](projectivetransformable3d.md)
- [protocol ProjectiveTransformable3DFloat](projectivetransformable3dfloat.md)
- [struct WorldReferenceCoordinateSpace](worldreferencecoordinatespace.md)
  A coordinate space that represents a world reference point.
### Applying trigonometric functions
- [func cos(Angle2D) -> Double](cos(_:)-609v4.md)
- [func cos(Angle2DFloat) -> Float](cos(_:)-79fxe.md)
- [func cosh(Angle2D) -> Double](cosh(_:)-6cg6v.md)
- [func cosh(Angle2DFloat) -> Float](cosh(_:)-9mmhn.md)
- [func sin(Angle2DFloat) -> Float](sin(_:)-46su7.md)
- [func sin(Angle2D) -> Double](sin(_:)-5tddt.md)
- [func sinh(Angle2D) -> Double](sinh(_:)-4m7ds.md)
- [func sinh(Angle2DFloat) -> Float](sinh(_:)-8kigy.md)
- [func tan(Angle2D) -> Double](tan(_:)-1sjgu.md)
- [func tan(Angle2DFloat) -> Float](tan(_:)-9x99s.md)
- [func tanh(Angle2D) -> Double](tanh(_:)-1f341.md)
- [func tanh(Angle2DFloat) -> Float](tanh(_:)-5yozs.md)
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
- [protocol ClampableWithinRectProtocol](clampablewithinrectprotocol.md)
  A set of methods that defines the interface for Spatial entities that can be clamped to a volume.
- [protocol Primitive3DProtocol](primitive3dprotocol.md)
  A set of methods common to Spatial primitives.
- [protocol Rotatable3DProtocol](rotatable3dprotocol.md)
  A set of methods that defines the interface for Spatial entities that can rotate.
- [protocol Scalable3DProtocol](scalable3dprotocol.md)
  A set of methods that defines the interface for Spatial entities that can scale.
- [protocol Shearable3DProtocol](shearable3dprotocol.md)
  A set of methods that defines the interface for Spatial entities that can shear.
- [protocol SpatialTypeProtocol](spatialtypeprotocol.md)
- [protocol Transform3DProtocol](transform3dprotocol.md)
  A set of methods that are common to transforms.
- [protocol Translatable3DProtocol](translatable3dprotocol.md)
  A set of methods that defines the interface for Spatial entities that can translate.
- [protocol VolumetricProtocol](volumetricprotocol.md)
  A set of methods for working with Spatial primitives with volume.
### Macros
- [Macros & Global Variables](spatial-macros.md)
### Structures
- [struct EulerAnglesFloat](euleranglesfloat.md)
### Enumerations
- [enum AxisWithFactorsFloat](axiswithfactorsfloat.md)
  The axis of a shear transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Spatial)*