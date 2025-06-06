# Point3D

**Framework**: Spatial  
**Kind**: struct

A point in a 3D coordinate system.

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
struct Point3D
```

## Topics

### Creating a 3D point structure
- [init()](point3d/init.md)
  Creates a point.
- [init(x: Double, y: Double, z: Double)](point3d/init(x:y:z:)-3lary.md)
  Creates a point from the specified double-precision values.
- [init<T>(x: T, y: T, z: T)](point3d/init(x:y:z:)-28jhw.md)
  Creates a point from the specified floating-point values.
- [init(vector: simd_double3)](point3d/init(vector:).md)
  Creates a point from the specified double-precision vector.
- [init(Size3D)](point3d/init(_:)-1f1ha.md)
  Creates a point from the specified Spatial size structure.
- [init(simd_float3)](point3d/init(_:)-1kved.md)
  Creates a point from the specified single-precision vector.
- [init(Vector3D)](point3d/init(_:)-34plj.md)
  Creates a point from the specified Spatial vector.
- [init(simd_double3)](point3d/init(_:)-4gu20.md)
  Creates a point from the specified double-precision vector.
- [init(SphericalCoordinates3D)](point3d/init(_:)-50tw4.md)
  Returns a Spatial point that represents the Cartesian coordinates of the specified spherical coordinates structure.
### Inspecting a 3D point’s properties
- [var x: Double](point3d/x.md)
  The x-coordinate value.
- [var y: Double](point3d/y.md)
  The y-coordinate value.
- [var z: Double](point3d/z.md)
  The z-coordinate value.
- [var vector: simd_double3](point3d/vector.md)
- [var magnitudeSquared: Double](point3d/magnitudesquared.md)
### Checking characteristics
- [func distance(to: Point3D) -> Double](point3d/distance(to:).md)
  Returns the distance between two points.
### Transforming a 3D point structure
- [func applying(ScaledPose3D) -> Point3D](point3d/applying(_:)-1f4em.md)
  Returns a point that’s transformed by the specified scaled pose.
- [func applying(ScaledPose3D) -> Point3D](point3d/applying(_:)-1f4em.md)
  Returns a point that’s transformed by the specified scaled pose.
- [func applying(Pose3D) -> Point3D](point3d/applying(_:)-7ulww.md)
  Returns a point that results from applying the specified pose.
- [func clamp(to: Rect3D)](point3d/clamp(to:).md)
  Clamps the mutable point to the specified rectangle.
- [func clamped(to: Rect3D) -> Point3D](point3d/clamped(to:).md)
  Returns a point with coordinates that clamp to the specified rectangle.
- [func scale(by: Double)](point3d/scale(by:).md)
- [func rotated(by: Rotation3D, around: Point3D) -> Point3D](point3d/rotated(by:around:)-4tmfq.md)
  Returns a point that results from applying a rotation around the specified point.
- [func rotated(by: simd_quatd, around: Point3D) -> Point3D](point3d/rotated(by:around:)-chuy.md)
  Returns a point that results from rotating with a quaternion around the specified point.
- [func unapplying(Pose3D) -> Point3D](point3d/unapplying(_:)-5hk6t.md)
  Returns a point that results from unapplying the specified pose.
- [func unapplying(ScaledPose3D) -> Point3D](point3d/unapplying(_:)-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Point3D](point3d/unapplying(_:)-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.
### Comparing values
- [static func == (Point3D, Point3D) -> Bool](point3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
- [func isApproximatelyEqual(to: Point3D, tolerance: Double) -> Bool](point3d/isapproximatelyequal(to:tolerance:).md)
### Applying arithmetic operations
- [static func * (Point3D, Double) -> Point3D](point3d/*(_:_:)-9rqvh.md)
  Returns a point that’s the product of a point and a scalar value.
- [static func * (Double, Point3D) -> Point3D](point3d/*(_:_:)-9w7dk.md)
  Returns a point that’s the product of a scalar value and a point.
- [static func * (AffineTransform3D, Point3D) -> Point3D](point3d/*(_:_:)-8ewep.md)
  Returns the point that results from applying the affine transform to the point.
- [static func * (ProjectiveTransform3D, Point3D) -> Point3D](point3d/*(_:_:)-9ak06.md)
  Returns the point that results from applying the projective transform to the point.
- [static func * (Pose3D, Point3D) -> Point3D](point3d/*(_:_:)-8wgkb.md)
  Returns a new point after applying the pose to the point.
- [static func + (Point3D, Size3D) -> Point3D](point3d/+(_:_:)-5v6x4.md)
  Returns a point that’s the element-wise sum of a point and a size.
- [static func + (Size3D, Point3D) -> Point3D](point3d/+(_:_:)-4g55.md)
  Returns a point that’s the element-wise sum of a size and a point.
- [static func - (Point3D) -> Point3D](point3d/-(_:).md)
  Returns a point that’s the element-wise negation of the point.
- [static func - (Point3D, Size3D) -> Point3D](point3d/-(_:_:)-6om9g.md)
  Returns a point that’s the element-wise difference of a point and a size.
- [static func - (Point3D, Point3D) -> Vector3D](point3d/-(_:_:)-9l6rn.md)
  Returns a point that’s the element-wise difference of two points.
- [static func - (Size3D, Point3D) -> Point3D](point3d/-(_:_:)-5t01r.md)
  Returns a point that’s the element-wise difference of a size and a point.
- [static func += (inout Point3D, Vector3D)](point3d/+=(_:_:)-80hjz.md)
  Adds a point and a vector, and stores the result in the left-hand-side variable.
- [static func += (inout Point3D, Size3D)](point3d/+=(_:_:)-3v0zk.md)
  Adds a point and a size, and stores the result in the left-hand-side variable.
- [static func -= (inout Point3D, Vector3D)](point3d/-=(_:_:)-23bow.md)
  Subtracts a vector from a point and stores the difference in the left-hand-side variable.
- [static func -= (inout Point3D, Size3D)](point3d/-=(_:_:)-9xu2.md)
  Subtracts a vector from a point and stores the difference in the left-hand-side variable.
- [static func *= (inout Point3D, Double)](point3d/*=(_:_:).md)
  Multiplies a point and a double-precision value, and stores the result in the left-hand-side variable.
- [static func / (Point3D, Double) -> Point3D](point3d/_(_:_:).md)
  Returns a point with each element divided by a scalar value.
- [static func /= (inout Point3D, Double)](point3d/_=(_:_:).md)
  Divides a point by a scalar value and stores the result in the left-hand-side variable.
### Deprecated symbols
- [func rotation(to: Point3D) -> Rotation3D](point3d/rotation(to:).md)
  Returns the rotation around the origin from the first point to the second point.
- [var origin: Point3D](point3d/origin.md)
- [var simd: simd_double3](point3d/simd.md)
  A simd three-element vector that contains the x-, y-, and z-coordinate values.
### Default Implementations
- [Animatable Implementations](point3d/animatable-implementations.md)
- [CustomReflectable Implementations](point3d/customreflectable-implementations.md)
- [Decodable Implementations](point3d/decodable-implementations.md)
- [Encodable Implementations](point3d/encodable-implementations.md)
- [Equatable Implementations](point3d/equatable-implementations.md)
- [Hashable Implementations](point3d/hashable-implementations.md)
- [Primitive3D Implementations](point3d/primitive3d-implementations.md)

## Relationships

### Conforms To
- [Animatable](../SwiftUI/Animatable.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3d)*