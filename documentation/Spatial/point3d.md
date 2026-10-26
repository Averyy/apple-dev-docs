# Point3D

**Framework**: Spatial  
**Kind**: struct  
**Role**: Structure

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

```c
typedef union { ... } SPPoint3D;
```

## Topics

### Creating a 3D point structure
- [init()](./point3d/init%28%29.md)
  Creates a point.
- [init(x: Double, y: Double, z: Double)](./point3d/init%28x,y,z%29-3lary.md)
  Creates a point from the specified double-precision values.
- [init<T>(x: T, y: T, z: T)](./point3d/init%28x,y,z%29-28jhw.md)
  Creates a point from the specified floating-point values.
- [init(vector: simd_double3)](./point3d/init%28vector%29.md)
  Creates a point from the specified double-precision vector.
- [init(Size3D)](./point3d/init%28_%29-1f1ha.md)
  Creates a point from the specified Spatial size structure.
- [init(simd_float3)](./point3d/init%28_%29-1kved.md)
  Creates a point from the specified single-precision vector.
- [init(Vector3D)](./point3d/init%28_%29-34plj.md)
  Creates a point from the specified Spatial vector.
- [init(simd_double3)](./point3d/init%28_%29-4gu20.md)
  Creates a point from the specified double-precision vector.
- [init(SphericalCoordinates3D)](./point3d/init%28_%29-50tw4.md)
  Returns a Spatial point that represents the Cartesian coordinates of the specified spherical coordinates structure.
- [SPPoint3DMakeWithSize](./sppoint3dmakewithsize.md)
  Creates a point from the specified Spatial size structure.
- [SPPoint3DMakeWithSphericalCoordinates](./sppoint3dmakewithsphericalcoordinates.md)
  Returns a Spatial point that represents the Cartesian coordinates of the specified spherical coordinates structure.
- [SPPoint3DMakeWithVector](./sppoint3dmakewithvector-39d4f.md)
  Creates a point from the specified double-precision vector.
- [SPPoint3DMakeWithVector](./sppoint3dmakewithvector-6eegc.md)
### Inspecting a 3D point’s properties
- [var x: Double](./point3d/x.md)
  The x-coordinate value.
- [var y: Double](./point3d/y.md)
  The y-coordinate value.
- [var z: Double](./point3d/z.md)
  The z-coordinate value.
- [var vector: simd_double3](./point3d/vector.md)
- [var magnitudeSquared: Double](./point3d/magnitudesquared.md)
- [x](./sppoint3d/x.md)
  The x-coordinate value.
- [y](./sppoint3d/y.md)
  The y-coordinate value.
- [z](./sppoint3d/z.md)
  The z-coordinate value.
- [SPPoint3DGetVector](./sppoint3dgetvector.md)
  A simd three-element vector that contains the x-, y-, and z-coordinate values.
### Checking characteristics
- [func distance(to: Point3D) -> Double](./point3d/distance%28to%29.md)
  Returns the distance between two points.
- [SPPoint3DIsFinite](./sppoint3disfinite.md)
- [SPPoint3DIsNaN](./sppoint3disnan.md)
- [SPPoint3DIsZero](./sppoint3diszero.md)
### Transforming a 3D point structure
- [func applying(ScaledPose3D) -> Point3D](./point3d/applying%28_%29-1f4em.md)
  Returns a point that’s transformed by the specified scaled pose.
- [func applying(ScaledPose3D) -> Point3D](./point3d/applying%28_%29-1f4em.md)
  Returns a point that’s transformed by the specified scaled pose.
- [func applying(Pose3D) -> Point3D](./point3d/applying%28_%29-7ulww.md)
  Returns a point that results from applying the specified pose.
- [func clamp(to: Rect3D)](./point3d/clamp%28to%29.md)
  Clamps the mutable point to the specified rectangle.
- [func scale(by: Double)](./point3d/scale%28by%29.md)
- [func rotated(by: Rotation3D, around: Point3D) -> Point3D](./point3d/rotated%28by,around%29-4tmfq.md)
  Returns a point that results from applying a rotation around the specified point.
- [func rotated(by: simd_quatd, around: Point3D) -> Point3D](./point3d/rotated%28by,around%29-chuy.md)
  Returns a point that results from rotating with a quaternion around the specified point.
- [func unapplying(Pose3D) -> Point3D](./point3d/unapplying%28_%29-5hk6t.md)
  Returns a point that results from unapplying the specified pose.
- [func unapplying(ScaledPose3D) -> Point3D](./point3d/unapplying%28_%29-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Point3D](./point3d/unapplying%28_%29-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.
- [SPPoint3DApplyAffineTransform](./sppoint3dapplyaffinetransform.md)
  Returns a point that results from applying the specified affine transform.
- [SPPoint3DApplyPose](./sppoint3dapplypose.md)
  Returns a point that results from applying the specified pose.
- [SPPoint3DApplyProjectiveTransform](./sppoint3dapplyprojectivetransform.md)
  Returns a point that results from applying the specified projective transform.
- [SPPoint3DApplyScaledPose](./sppoint3dapplyscaledpose.md)
  Returns a point that’s transformed by the specified scaled pose.
- [SPPoint3DRotate](./sppoint3drotate.md)
  Returns a point that results from applying the specified rotation.
- [SPPoint3DRotateByQuaternion](./sppoint3drotatebyquaternion.md)
  Returns a point that results from rotating with the specified quaternion.
- [SPPoint3DTranslate](./sppoint3dtranslate-8xo6b.md)
  Returns a point with an origin that’s offset by the specified size.
- [SPPoint3DTranslate](./sppoint3dtranslate-9aj4h.md)
  Returns a point with an origin that’s offset by the specified vector.
- [SPPoint3DUnapplyAffineTransform](./sppoint3dunapplyaffinetransform.md)
  Returns a point that results from unapplying the specified affine transform.
- [SPPoint3DUnapplyPose](./sppoint3dunapplypose.md)
  Returns a point that results from unapplying the specified pose.
- [SPPoint3DUnapplyProjectiveTransform](./sppoint3dunapplyprojectivetransform.md)
  Returns a point that results from unapplying the specified projective transform.
- [SPPoint3DUnapplyScaledPose](./sppoint3dunapplyscaledpose.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.
### Comparing values
- [static func == (Point3D, Point3D) -> Bool](./point3d/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two values are equal.
- [func isApproximatelyEqual(to: Point3D, tolerance: Double) -> Bool](./point3d/isapproximatelyequal%28to,tolerance%29.md)
- [SPPoint3DAlmostEqualToPoint](./sppoint3dalmostequaltopoint-8qyca.md)
- [SPPoint3DAlmostEqualToPoint](./sppoint3dalmostequaltopoint-9vk02.md)
  Returns a Boolean value that indicates whether the two points are equal within the specified default absolute tolerance.
- [SPPoint3DEqualToPoint](./sppoint3dequaltopoint.md)
  Returns a Boolean value that indicates whether two values are equal.
### Applying arithmetic operations
- [static func * (Point3D, Double) -> Point3D](./point3d/star%28_,_%29-9rqvh.md)
  Returns a point that’s the product of a point and a scalar value.
- [static func * (Double, Point3D) -> Point3D](./point3d/star%28_,_%29-9w7dk.md)
  Returns a point that’s the product of a scalar value and a point.
- [static func * (AffineTransform3D, Point3D) -> Point3D](./point3d/star%28_,_%29-8ewep.md)
  Returns the point that results from applying the affine transform to the point.
- [static func * (ProjectiveTransform3D, Point3D) -> Point3D](./point3d/star%28_,_%29-9ak06.md)
  Returns the point that results from applying the projective transform to the point.
- [static func * (Pose3D, Point3D) -> Point3D](./point3d/star%28_,_%29-8wgkb.md)
  Returns a new point after applying the pose to the point.
- [static func + (Point3D, Size3D) -> Point3D](./point3d/plus%28_,_%29-5v6x4.md)
  Returns a point that’s the element-wise sum of a point and a size.
- [static func + (Size3D, Point3D) -> Point3D](./point3d/plus%28_,_%29-4g55.md)
  Returns a point that’s the element-wise sum of a size and a point.
- [static func - (Point3D) -> Point3D](./point3d/minus%28_%29.md)
  Returns a point that’s the element-wise negation of the point.
- [static func - (Point3D, Size3D) -> Point3D](./point3d/minus%28_,_%29-6om9g.md)
  Returns a point that’s the element-wise difference of a point and a size.
- [static func - (Point3D, Point3D) -> Vector3D](./point3d/minus%28_,_%29-9l6rn.md)
  Returns a point that’s the element-wise difference of two points.
- [static func - (Size3D, Point3D) -> Point3D](./point3d/minus%28_,_%29-5t01r.md)
  Returns a point that’s the element-wise difference of a size and a point.
- [static func += (inout Point3D, Vector3D)](./point3d/pluseq%28_,_%29-80hjz.md)
  Adds a point and a vector, and stores the result in the left-hand-side variable.
- [static func += (inout Point3D, Size3D)](./point3d/pluseq%28_,_%29-3v0zk.md)
  Adds a point and a size, and stores the result in the left-hand-side variable.
- [static func -= (inout Point3D, Vector3D)](./point3d/minuseq%28_,_%29-23bow.md)
  Subtracts a vector from a point and stores the difference in the left-hand-side variable.
- [static func -= (inout Point3D, Size3D)](./point3d/minuseq%28_,_%29-9xu2.md)
  Subtracts a vector from a point and stores the difference in the left-hand-side variable.
- [static func *= (inout Point3D, Double)](./point3d/stareq%28_,_%29.md)
  Multiplies a point and a double-precision value, and stores the result in the left-hand-side variable.
- [static func / (Point3D, Double) -> Point3D](./point3d/op%28_,_%29.md)
  Returns a point with each element divided by a scalar value.
- [static func /= (inout Point3D, Double)](./point3d/opeq%28_,_%29.md)
  Divides a point by a scalar value and stores the result in the left-hand-side variable.
### Deprecated symbols
- [func rotation(to: Point3D) -> Rotation3D](./point3d/rotation%28to%29.md)
  Returns the rotation around the origin from the first point to the second point.
- [var origin: Point3D](./point3d/origin.md)
- [var simd: simd_double3](./point3d/simd.md)
  A simd three-element vector that contains the x-, y-, and z-coordinate values.
- [SPPoint3DGetOrigin](./sppoint3dgetorigin.md)
  The location of the point.
### Initializers
- [init(Point3DFloat)](./point3d/init%28_%29-7wgtj.md)
  Returns a double-precision point from a single-precision point.
- [init(simd_packed_double4)](./point3d/init%28_%29-8r7om.md)
  Creates a Spatial point from a simd packed vector.
### Default Implementations
- [Animatable Implementations](./point3d/animatable-implementations.md)
- [ClampableWithinRectProtocol Implementations](./point3d/clampablewithinrectprotocol-implementations.md)
- [CustomReflectable Implementations](./point3d/customreflectable-implementations.md)
- [Decodable Implementations](./point3d/decodable-implementations.md)
- [Encodable Implementations](./point3d/encodable-implementations.md)
- [Equatable Implementations](./point3d/equatable-implementations.md)
- [Hashable Implementations](./point3d/hashable-implementations.md)
- [Primitive3D Implementations](./point3d/primitive3d-implementations.md)
### Constants
- [SPPoint3DInfinity](./sppoint3dinfinity.md)
  The point with infinite x-, y-, and z-coordinate values.
- [SPPoint3DZero](./sppoint3dzero.md)
  The point with the zero value.

## Relationships

### Conforms To
- [Animatable](../SwiftUI/animatable.md)
- [ClampableWithinRectProtocol](./clampablewithinrectprotocol.md)
- [Copyable](../Swift/copyable.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Primitive3D](./primitive3d.md)
- [Primitive3DProtocol](./primitive3dprotocol.md)
- [ProjectiveTransformable3D](./projectivetransformable3d.md)
- [Rotatable3D](./rotatable3d.md)
- [Rotatable3DProtocol](./rotatable3dprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SpatialTypeProtocol](./spatialtypeprotocol.md)
- [Translatable3D](./translatable3d.md)
- [Translatable3DProtocol](./translatable3dprotocol.md)

## See Also

### 3D primitives
- [struct Point3DFloat](./point3dfloat.md)
  A single-precision structure that contains a point in a three-dimensional coordinate system.
- [struct Size3D](./size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
- [struct Size3DFloat](./size3dfloat.md)
  A single-precision structure that contains width, height, and depth values.
- [struct Rect3D](./rect3d.md)
  A rectangle in a 3D coordinate system.
- [struct Rect3DFloat](./rect3dfloat.md)
  A single-precision structure that contains the location and dimensions of a 3D rectangle.
- [struct Rotation3D](./rotation3d.md)
  A rotation in three dimensions.
- [struct Rotation3DFloat](./rotation3dfloat.md)
  A single-precision structure that represents a rotation in three dimensions.
- [struct RotationAxis3D](./rotationaxis3d.md)
  A 3D rotation axis.
- [struct RotationAxis3DFloat](./rotationaxis3dfloat.md)
  A 3D axis.
- [struct Pose3D](./pose3d.md)
  A structure that contains a 3D position and a 3D rotation.
- [struct Pose3DFloat](./pose3dfloat.md)
  A single-precision structure that contains a position and rotation.
- [struct ScaledPose3D](./scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct ScaledPose3DFloat](./scaledpose3dfloat.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](./sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct SphericalCoordinates3DFloat](./sphericalcoordinates3dfloat.md)
  A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3d)*