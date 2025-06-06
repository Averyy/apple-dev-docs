# Ray3D

**Framework**: Spatial  
**Kind**: struct

A ray in a 3D coordinate system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Ray3D
```

## Topics

### Creating a 3D ray structure
- [init()](ray3d/init.md)
  Creates a ray structure.
- [init(origin: Point3D, direction: Vector3D)](ray3d/init(origin:direction:)-5sxkl.md)
  Creates a ray with the specified origin and the specified direction from Spatial primitives.
- [init(origin: simd_float3, direction: simd_float3)](ray3d/init(origin:direction:)-3gfcj.md)
  Creates a ray with the specified origin and the specified direction from single-precision vectors.
- [init(origin: simd_double3, direction: simd_double3)](ray3d/init(origin:direction:)-47w1c.md)
  Creates a ray with the specified origin and the specified direction from double-precision vectors.
### Inspecting a 3D ray’s properties
- [var origin: Point3D](ray3d/origin.md)
  The origin of the ray.
- [var direction: Vector3D](ray3d/direction.md)
  The direction of the ray.
### Transforming a 3D ray structure
- [func apply(Pose3D)](ray3d/apply(_:).md)
  Applies the specified pose to the ray.
- [func applying(AffineTransform3D) -> Ray3D](ray3d/applying(_:)-337n0.md)
  Returns a ray that results from applying the specified affine transform.
- [func applying(ProjectiveTransform3D) -> Ray3D](ray3d/applying(_:)-2aom9.md)
  Returns a ray that results from applying the specified projective transform.
- [func applying(Pose3D) -> Ray3D](ray3d/applying(_:)-34rqi.md)
  Returns a ray that results from applying the specified pose.
- [func unapplying(AffineTransform3D) -> Ray3D](ray3d/unapplying(_:)-7bc37.md)
  Returns a ray that results from unapplying the specified affine transform.
- [func unapplying(ProjectiveTransform3D) -> Ray3D](ray3d/unapplying(_:)-6tj2w.md)
  Returns a ray that results from unapplying the specified projective transform.
- [func unapplying(Pose3D) -> Ray3D](ray3d/unapplying(_:)-928o9.md)
  Unapplies the specified pose to the ray.
- [func rotated(by: Rotation3D) -> Ray3D](ray3d/rotated(by:)-qxp0.md)
  Returns a ray that results from applying the specified rotation.
- [func rotated(by: simd_quatd) -> Ray3D](ray3d/rotated(by:)-81glv.md)
  Returns a ray that results from rotating with the specified quaternion.
- [func rotated(by: simd_quatd, around: Point3D) -> Ray3D](ray3d/rotated(by:around:)-uzon.md)
  Returns a ray that’s rotated by the specified quaternion around a specified pivot.
- [func rotated(by: Rotation3D, around: Point3D) -> Ray3D](ray3d/rotated(by:around:)-7h43.md)
  Returns a ray that’s rotated by the specified rotation around a specified pivot.
- [func applying(ScaledPose3D) -> Ray3D](ray3d/applying(_:)-6hfqw.md)
  Returns a ray that’s transformed by the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Ray3D](ray3d/unapplying(_:)-9x164.md)
  Returns a ray that’s transformed by the inverse of the specified scaled pose.
### Checking characteristics
- [var isFinite: Bool](ray3d/isfinite.md)
  A Boolean value that indicates whether all of the values of the ray are finite.
- [var isNaN: Bool](ray3d/isnan.md)
  A Boolean value that indicates whether the ray contains any NaN values.
- [var isZero: Bool](ray3d/iszero.md)
  A Boolean value that indicates whether all of the values of the ray are zero.
- [func intersects(Rect3D) -> Bool](ray3d/intersects(_:).md)
  Returns a Boolean value that indicates whether a ray intersects a rectangle.
- [func intersects(sphereOrigin: Point3D, sphereRadius: Double) -> Bool](ray3d/intersects(sphereorigin:sphereradius:).md)
  Returns a Boolean value that indicates whether the ray intersects a specified sphere.
### Comparing values
- [static func == (Ray3D, Ray3D) -> Bool](ray3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Applying arithmetic operations
- [static func * (Pose3D, Ray3D) -> Ray3D](ray3d/*(_:_:).md)
  Returns the ray that results from applying the pose to the ray.
### Initializers
- [init(origin: Point3D, direction: Vector3D)](ray3d/init(origin:direction:)-63yk4.md)
  Creates a ray from Spatial primitives that describe the origin and direction.
### Default Implementations
- [CustomReflectable Implementations](ray3d/customreflectable-implementations.md)
- [Decodable Implementations](ray3d/decodable-implementations.md)
- [Encodable Implementations](ray3d/encodable-implementations.md)
- [Equatable Implementations](ray3d/equatable-implementations.md)
- [Hashable Implementations](ray3d/hashable-implementations.md)
- [Primitive3D Implementations](ray3d/primitive3d-implementations.md)
- [Rotatable3D Implementations](ray3d/rotatable3d-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Primitive3D](primitive3d.md)
- [Rotatable3D](rotatable3d.md)
- [Sendable](../Swift/Sendable.md)
- [Translatable3D](translatable3d.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3d)*