# Point3DFloat

**Framework**: Spatial  
**Kind**: struct  
**Role**: Structure

A single-precision structure that contains a point in a three-dimensional coordinate system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Point3DFloat
```

```c
typedef union { ... } SPPoint3DFloat;
```

## Topics

### Operators
- [static func * (Pose3DFloat, Point3DFloat) -> Point3DFloat](./point3dfloat/star%28_,_%29-1r8dj.md)
  Returns the point that results from applying the pose to the point.
- [static func * (ProjectiveTransform3DFloat, Point3DFloat) -> Point3DFloat](./point3dfloat/star%28_,_%29-22247.md)
  Returns the point that results from applying the transform to the point.
- [static func * (AffineTransform3DFloat, Point3DFloat) -> Point3DFloat](./point3dfloat/star%28_,_%29-3doxu.md)
  Returns the point that results from applying the transform to the point.
- [static func * (Float, Point3DFloat) -> Point3DFloat](./point3dfloat/star%28_,_%29-5k7wl.md)
  Returns a point with each element mulitplied by a scalar value.
- [static func * (Point3DFloat, Float) -> Point3DFloat](./point3dfloat/star%28_,_%29-8ug4a.md)
  Returns a point with each element mulitplied by a scalar value.
- [static func *= (inout Point3DFloat, Float)](./point3dfloat/stareq%28_,_%29.md)
  Calculates the product of each element of a point and a scalar value and stores the result in the left-hand-side variable.
- [static func + (Size3DFloat, Point3DFloat) -> Point3DFloat](./point3dfloat/plus%28_,_%29-1t1gn.md)
  Returns a point that’s the element-wise sum of a size’s `width`, `height`, and `depth` and a point’s `x`, `y`, and `z` .
- [static func + (Point3DFloat, Size3DFloat) -> Point3DFloat](./point3dfloat/plus%28_,_%29-6ihv8.md)
  Returns a point that’s the element-wise sum of a point’s `x`, `y`, and `z` and a size’s `width`, `height`, and `depth`.
- [static func += (inout Point3DFloat, Vector3DFloat)](./point3dfloat/pluseq%28_,_%29-1x97i.md)
  Calculates the point that’s the element-wise sum of a point and a vector and stores the result in the left-hand-side variable.
- [static func += (inout Point3DFloat, Size3DFloat)](./point3dfloat/pluseq%28_,_%29-83599.md)
  Calculates the element-wise sum of a point’s `x`, `y`, and `z` and a size’s `width`, `height`, and `depth` and stores the result in the left-hand-side variable.
- [static func - (Point3DFloat) -> Point3DFloat](./point3dfloat/minus%28_%29.md)
  Returns a point that’s the element-wise negation of the point.
- [static func - (Size3DFloat, Point3DFloat) -> Point3DFloat](./point3dfloat/minus%28_,_%29-46bqa.md)
  Returns a point that’s the element-wise difference of a size’s `width`, `height`, and `depth` and a point’s `x`, `y`, and `z`.
- [static func - (Point3DFloat, Point3DFloat) -> Vector3DFloat](./point3dfloat/minus%28_,_%29-5jrc.md)
  Returns a vector that’s the element-wise difference of two points.
- [static func - (Point3DFloat, Size3DFloat) -> Point3DFloat](./point3dfloat/minus%28_,_%29-5rz8s.md)
  Returns a point that’s the element-wise difference of a point’s `x`, `y`, and `z` and a size’s `width`, `height`, and `depth`.
- [static func -= (inout Point3DFloat, Size3DFloat)](./point3dfloat/minuseq%28_,_%29-7r1d1.md)
  Calculates the element-wise difference of a point’s `x`, `y`, and `z` and a size’s `width`, `height`, and `depth` and stores the result in the left-hand-side variable.
- [static func -= (inout Point3DFloat, Vector3DFloat)](./point3dfloat/minuseq%28_,_%29-8fp0l.md)
  Calculates the point that’s the element-wise difference of a point and a vector and stores the result in the left-hand-side variable.
- [static func / (Point3DFloat, Float) -> Point3DFloat](./point3dfloat/op%28_,_%29.md)
  Returns a point with each element divided by a scalar value.
- [static func /= (inout Point3DFloat, Float)](./point3dfloat/opeq%28_,_%29.md)
  Calculates the division of each element of a point and a scalar value and stores the result in the left-hand-side variable.
### Initializers
- [init()](./point3dfloat/init%28%29.md)
- [init(Size3DFloat)](./point3dfloat/init%28_%29-1h5vt.md)
  Returns a new point from a size.
- [init(Vector3DFloat)](./point3dfloat/init%28_%29-4sdjs.md)
  Returns a new point from a Spatial vector.
- [init(simd_packed_float4)](./point3dfloat/init%28_%29-4uwq7.md)
  Creates a Spatial point from a simd packed vector.
- [init(simd_double3)](./point3dfloat/init%28_%29-5fcqk.md)
  Returns a new point from a double-precision vector.
- [init(Point3D)](./point3dfloat/init%28_%29-5g1ob.md)
  Returns a single-precision point from a double-precision point.
- [init(SphericalCoordinates3DFloat)](./point3dfloat/init%28_%29-8c02t.md)
  Creates a new point structure that contains the spherical coordinates converted to Cartesian coordinates.
- [init(simd_float3)](./point3dfloat/init%28_%29-8dj77.md)
  Returns a new point from a double-precision vector.
- [init(vector: simd_float3)](./point3dfloat/init%28vector%29.md)
- [init<T>(x: T, y: T, z: T)](./point3dfloat/init%28x,y,z%29-3hzkg.md)
  Returns a new point from the doubleing-point values.
- [init(x: Float, y: Float, z: Float)](./point3dfloat/init%28x,y,z%29-59uqs.md)
  Returns a point from the specified values.
### Instance Properties
- [var vector: simd_float3](./point3dfloat/vector.md)
- [var x: Float](./point3dfloat/x.md)
- [var y: Float](./point3dfloat/y.md)
- [var z: Float](./point3dfloat/z.md)
- [x](./sppoint3dfloat/x.md)
  The x-coordinate of the point.
- [y](./sppoint3dfloat/y.md)
  The y-coordinate of the point.
- [z](./sppoint3dfloat/z.md)
  The z-coordinate of the point.
### Instance Methods
- [func applying(ScaledPose3DFloat) -> Point3DFloat](./point3dfloat/applying%28_%29-2dhmf.md)
  Returns the primitive that results from applying a scaled pose to the primitive.
- [func distance(to: Point3DFloat) -> Float](./point3dfloat/distance%28to%29.md)
- [func isApproximatelyEqual(to: Point3DFloat, tolerance: Float) -> Bool](./point3dfloat/isapproximatelyequal%28to,tolerance%29.md)
  Returns a Boolean value that indicates whether two points are equal within a specified tolerance.
- [func rotated(by: simd_quatf, around: Point3DFloat) -> Point3DFloat](./point3dfloat/rotated%28by,around%29-1ejmw.md)
- [func rotated(by: Rotation3DFloat, around: Point3DFloat) -> Point3DFloat](./point3dfloat/rotated%28by,around%29-5xwwi.md)
- [func unapplying(ScaledPose3DFloat) -> Point3DFloat](./point3dfloat/unapplying%28_%29-93yzx.md)
  Returns the primitive that results from unapplying a scaled pose to the primitive.
### Default Implementations
- [CustomReflectable Implementations](./point3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](./point3dfloat/decodable-implementations.md)
- [Encodable Implementations](./point3dfloat/encodable-implementations.md)
- [Equatable Implementations](./point3dfloat/equatable-implementations.md)
- [Hashable Implementations](./point3dfloat/hashable-implementations.md)
- [Primitive3DProtocol Implementations](./point3dfloat/primitive3dprotocol-implementations.md)

## Relationships

### Conforms To
- [ClampableWithinRectProtocol](./clampablewithinrectprotocol.md)
- [Copyable](../Swift/copyable.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Primitive3DProtocol](./primitive3dprotocol.md)
- [ProjectiveTransformable3D](./projectivetransformable3d.md)
- [ProjectiveTransformable3DFloat](./projectivetransformable3dfloat.md)
- [Rotatable3DProtocol](./rotatable3dprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SpatialTypeProtocol](./spatialtypeprotocol.md)
- [Translatable3DProtocol](./translatable3dprotocol.md)

## See Also

### 3D primitives
- [struct Point3D](./point3d.md)
  A point in a 3D coordinate system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3dfloat)*