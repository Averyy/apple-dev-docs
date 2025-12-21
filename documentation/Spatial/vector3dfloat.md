# Vector3DFloat

**Framework**: Spatial  
**Kind**: struct

A single-precision structure that defines a three-element vector

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
struct Vector3DFloat
```

## Topics

### Operators
- [static func * (Pose3DFloat, Vector3DFloat) -> Vector3DFloat](vector3dfloat/*(_:_:)-1nqw7.md)
  Returns the vector that results from applying the pose to the vector.
- [static func * (ProjectiveTransform3DFloat, Vector3DFloat) -> Vector3DFloat](vector3dfloat/*(_:_:)-39da3.md)
  Returns the vector that results from applying the transform to the vector.
- [static func * (Vector3DFloat, Float) -> Vector3DFloat](vector3dfloat/*(_:_:)-5f6x6.md)
  Returns the vector that’s the element-wise product of a vector and a scalar value.
- [static func * (Float, Vector3DFloat) -> Vector3DFloat](vector3dfloat/*(_:_:)-77n9y.md)
  Returns the vector that’s the element-wise product of a scalar value and a vector.
- [static func * (AffineTransform3DFloat, Vector3DFloat) -> Vector3DFloat](vector3dfloat/*(_:_:)-86gx9.md)
  Returns the vector that results from applying the transform to the vector.
- [static func *= (inout Vector3DFloat, Float)](vector3dfloat/*=(_:_:).md)
  Calculates the vector that’s the element-wise product of a vector and a scalar value and stores the result in the left-hand-side variable.
- [static func + (Point3DFloat, Vector3DFloat) -> Point3DFloat](vector3dfloat/+(_:_:)-1l8zf.md)
  Returns the point that’s the element-wise sum of a point and a vector.
- [static func + (Vector3DFloat, Point3DFloat) -> Point3DFloat](vector3dfloat/+(_:_:)-1wtkv.md)
  Returns the point that’s the element-wise sum of a vector and a point.
- [static func + (Size3DFloat, Vector3DFloat) -> Size3DFloat](vector3dfloat/+(_:_:)-2l7re.md)
  Returns the size that’s the element-wise sum of a size and a vector.
- [static func + (Vector3DFloat, Size3DFloat) -> Size3DFloat](vector3dfloat/+(_:_:)-94qrx.md)
  Returns the size that’s the element-wise sum of a vector and a size.
- [static func - (Vector3DFloat) -> Vector3DFloat](vector3dfloat/-(_:).md)
  Returns the vector that’s the element-wise negation of the vector.
- [static func - (Vector3DFloat, Size3DFloat) -> Size3DFloat](vector3dfloat/-(_:_:)-115el.md)
  Returns the size that’s the element-wise difference of a vector and a size.
- [static func - (Size3DFloat, Vector3DFloat) -> Size3DFloat](vector3dfloat/-(_:_:)-5qy45.md)
  Returns the size that’s the element-wise difference of a size and a vector.
- [static func - (Vector3DFloat, Point3DFloat) -> Point3DFloat](vector3dfloat/-(_:_:)-7h9bz.md)
  Returns the point that’s the element-wise difference of a vector and a point.
- [static func - (Point3DFloat, Vector3DFloat) -> Point3DFloat](vector3dfloat/-(_:_:)-8k83d.md)
  Returns the point that’s the element-wise difference of a point and a vector.
- [static func / (Vector3DFloat, Float) -> Vector3DFloat](vector3dfloat/_(_:_:).md)
  Returns the vector that’s the element-wise division of a vector and a scalar value.
- [static func /= (inout Vector3DFloat, Float)](vector3dfloat/_=(_:_:).md)
  Calculates the vector that’s the element-wise division of a vector and a scalar value and stores the result in the left-hand-side variable.
### Initializers
- [init()](vector3dfloat/init.md)
- [init(RotationAxis3DFloat)](vector3dfloat/init(_:)-13p20.md)
  Returns a new vector from a rotation axis.
- [init(simd_packed_float4)](vector3dfloat/init(_:)-1w9o5.md)
  Creates a Spatial vector from a simd packed vector.
- [init(Point3DFloat)](vector3dfloat/init(_:)-217dp.md)
  Returns a new vector from a point.
- [init(simd_double3)](vector3dfloat/init(_:)-2qtq8.md)
  Returns a vector point from a single-precision vector.
- [init(simd_float3)](vector3dfloat/init(_:)-3c8f6.md)
  Returns a new vector from a single-precision vector.
- [init(SphericalCoordinates3DFloat)](vector3dfloat/init(_:)-4svr4.md)
  Creates a new vector structure that contains the spherical coordinates converted to Cartesian coordinates.
- [init(Vector3D)](vector3dfloat/init(_:)-538j2.md)
  Returns a single-precision vector from a double-precision vector.
- [init(Size3DFloat)](vector3dfloat/init(_:)-7y4t0.md)
  Returns a new vector from a size.
- [init(vector: simd_float3)](vector3dfloat/init(vector:).md)
- [init<T>(x: T, y: T, z: T)](vector3dfloat/init(x:y:z:)-1h79g.md)
  Returns a new vector from the doubleing-point values.
- [init(x: Float, y: Float, z: Float)](vector3dfloat/init(x:y:z:)-8dkie.md)
  Returns a vector from the specified values.
### Instance Properties
- [var length: Float](vector3dfloat/length.md)
- [var lengthSquared: Float](vector3dfloat/lengthsquared.md)
- [var normalized: Vector3DFloat](vector3dfloat/normalized.md)
  Returns this vector with a length of `1`.
- [var vector: simd_float3](vector3dfloat/vector.md)
- [var x: Float](vector3dfloat/x.md)
- [var y: Float](vector3dfloat/y.md)
- [var z: Float](vector3dfloat/z.md)
### Instance Methods
- [func applying(ScaledPose3DFloat) -> Vector3DFloat](vector3dfloat/applying(_:)-3mahk.md)
  Returns the primitive that results from applying a scaled pose to the primitive.
- [func cross(Vector3DFloat) -> Vector3DFloat](vector3dfloat/cross(_:).md)
  Returns the cross product of this vector and the specified vector.
- [func dot(Vector3DFloat) -> Float](vector3dfloat/dot(_:).md)
  Returns the dot product of this vector and the specified vector.
- [func normalize()](vector3dfloat/normalize.md)
  Normalizes the vector.
- [func projected(Vector3DFloat) -> Vector3DFloat](vector3dfloat/projected(_:).md)
  Returns this vector projected onto the specified vector.
- [func reflected(Vector3DFloat) -> Vector3DFloat](vector3dfloat/reflected(_:).md)
  Returns the reflection direction of this incident vector and the specified unit normal vector.
- [func rotation(to: Vector3DFloat) -> Rotation3DFloat](vector3dfloat/rotation(to:).md)
  Returns the rotation from the normalized first vector to the normalized second vector.
- [func sheared(AxisWithFactors) -> Vector3DFloat](vector3dfloat/sheared(_:).md)
  Returns a sheared vector.
- [func unapplying(ScaledPose3DFloat) -> Vector3DFloat](vector3dfloat/unapplying(_:)-9dwm2.md)
  Returns the primitive that results from unapplying a scaled pose to the primitive.
### Type Properties
- [static let forward: Vector3DFloat](vector3dfloat/forward.md)
  A vector with values `[0, 0, 1]`.
- [static let right: Vector3DFloat](vector3dfloat/right.md)
  A vector with values `[1, 0, 0]`.
- [static let up: Vector3DFloat](vector3dfloat/up.md)
  A vector with values `[0, 1, 0]`.
### Type Methods
- [static func lerp(from: Vector3DFloat, to: Vector3DFloat, t: Vector3DFloat) -> Vector3DFloat](vector3dfloat/lerp(from:to:t:).md)
  Returns a Spatial vector that represents the linear interpolation at `t` between two vectors.
- [static func smoothstep(edge0: Vector3DFloat, edge1: Vector3DFloat, x: Vector3DFloat) -> Vector3DFloat](vector3dfloat/smoothstep(edge0:edge1:x:).md)
  Returns a Spatial vector that represents the smooth interpolation at `x` between two vectors.
### Default Implementations
- [AdditiveArithmetic Implementations](vector3dfloat/additivearithmetic-implementations.md)
- [CustomReflectable Implementations](vector3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](vector3dfloat/decodable-implementations.md)
- [Encodable Implementations](vector3dfloat/encodable-implementations.md)
- [Equatable Implementations](vector3dfloat/equatable-implementations.md)
- [Hashable Implementations](vector3dfloat/hashable-implementations.md)
- [Primitive3DProtocol Implementations](vector3dfloat/primitive3dprotocol-implementations.md)
- [Rotatable3DProtocol Implementations](vector3dfloat/rotatable3dprotocol-implementations.md)
- [Scalable3DProtocol Implementations](vector3dfloat/scalable3dprotocol-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Primitive3DProtocol](primitive3dprotocol.md)
- [ProjectiveTransformable3D](projectivetransformable3d.md)
- [ProjectiveTransformable3DFloat](projectivetransformable3dfloat.md)
- [Rotatable3DProtocol](rotatable3dprotocol.md)
- [Scalable3DProtocol](scalable3dprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)

## See Also

- [struct Vector3D](vector3d.md)
  A three-element vector.
- [struct Axis3D](axis3d.md)
  Constants that describe an axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3dfloat)*