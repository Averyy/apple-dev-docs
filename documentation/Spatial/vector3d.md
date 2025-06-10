# Vector3D

**Framework**: Spatial  
**Kind**: struct

A three-element vector.

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
struct Vector3D
```

## Topics

### Creating a vector
- [init()](vector3d/init.md)
  Creates a vector.
- [init(x: Double, y: Double, z: Double)](vector3d/init(x:y:z:)-2ejxw.md)
  Creates a vector from the specified double-precision values.
- [init<T>(x: T, y: T, z: T)](vector3d/init(x:y:z:)-29hwg.md)
  Creates a vector from the specified floating-point values.
- [init(simd_float3)](vector3d/init(_:)-73gdm.md)
  Creates a ray from the specified single-precision vector.
- [init(simd_double3)](vector3d/init(_:)-1a9i3.md)
  Creates a vector from the specified double-precision vector.
- [init(vector: simd_double3)](vector3d/init(vector:).md)
  Creates a vector from the specified double-precision vector.
- [init(RotationAxis3D)](vector3d/init(_:)-3br9h.md)
  Creates a vector from the specified Spatial rotation axis.
- [init(Point3D)](vector3d/init(_:)-8vcph.md)
  Creates a vector from the specified Spatial point structure.
- [init(Size3D)](vector3d/init(_:)-8egfs.md)
  Creates a vector from the specified Spatial size structure.
- [init(SphericalCoordinates3D)](vector3d/init(_:)-9ker1.md)
  Creates a vector from the specified Spatial spherical coordinates structure.
### Inspecting a vector’s properties
- [var x: Double](vector3d/x.md)
  The x-element value.
- [var y: Double](vector3d/y.md)
  The y-element value.
- [var z: Double](vector3d/z.md)
  The z-element value.
- [var vector: simd_double3](vector3d/vector.md)
  A simd three-element vector that contains the x-, y-, and z-element values.
### Checking characteristics
- [func rotation(to: Vector3D) -> Rotation3D](vector3d/rotation(to:).md)
  Returns the rotation from the normalized first vector to the normalized second vector.
### Geometry functions
- [func cross(Vector3D) -> Vector3D](vector3d/cross(_:).md)
  Returns the cross product of the vector and the specified vector.
- [func dot(Vector3D) -> Double](vector3d/dot(_:).md)
  Returns the dot product of the vector and the specified vector.
- [var length: Double](vector3d/length.md)
  The length of the vector.
- [var lengthSquared: Double](vector3d/lengthsquared.md)
  The square of the length of the vector.
- [func normalize()](vector3d/normalize.md)
  Normalizes the mutable vector.
- [var normalized: Vector3D](vector3d/normalized.md)
  A new vector that represents the normalized copy of the current vector.
- [func projected(Vector3D) -> Vector3D](vector3d/projected(_:).md)
  Returns the vector projected onto the specified vector.
- [func reflected(Vector3D) -> Vector3D](vector3d/reflected(_:).md)
  Returns the reflection direction of the incident vector and a specified unit normal vector.
### Transforming a vector
- [func applying(AffineTransform3D) -> Vector3D](vector3d/applying(_:)-1d0mh.md)
  Returns the vector that results from applying an affine transform to the vector.
- [func applying(ProjectiveTransform3D) -> Vector3D](vector3d/applying(_:)-5y3xb.md)
  Returns the vector that results from applying a projective transform to the vector.
- [func applying(Pose3D) -> Vector3D](vector3d/applying(_:)-4k2qi.md)
  Returns a vector that results from applying the specified pose.
- [func unapplying(AffineTransform3D) -> Vector3D](vector3d/unapplying(_:)-6vl3o.md)
  Returns the vector that results from unapplying an affine transform to the vector.
- [func unapplying(ProjectiveTransform3D) -> Vector3D](vector3d/unapplying(_:)-8ookb.md)
  Returns the vector that results from unapplying a projective transform to the vector.
- [func unapplying(Pose3D) -> Vector3D](vector3d/unapplying(_:)-1gzyd.md)
  Returns a vector that results from unapplying the specified pose.
- [func rotated(by: Rotation3D) -> Vector3D](vector3d/rotated(by:)-2gcq4.md)
  Returns the vector rotated by the specified rotation around the origin.
- [func rotated(by: simd_quatd) -> Vector3D](vector3d/rotated(by:)-8bwna.md)
  Returns the vector rotated by the specified quaternion around the origin.
- [func scaled(by: Size3D) -> Vector3D](vector3d/scaled(by:).md)
  Returns the vector scaled by the specified size.
- [func scaledBy(x: Double, y: Double, z: Double) -> Vector3D](vector3d/scaledby(x:y:z:).md)
  Returns a vector that results from scaling with the specified double-precision values.
- [func uniformlyScaled(by: Double) -> Vector3D](vector3d/uniformlyscaled(by:).md)
  Returns the entity uniformly scaled by the specified scalar value.
- [func sheared(AxisWithFactors) -> Vector3D](vector3d/sheared(_:).md)
  Returns a vector that results from shearing over an axis by shear factors for the other two axes.
- [func applying(ScaledPose3D) -> Vector3D](vector3d/applying(_:)-8fn6a.md)
  Returns a vector that’s transformed by the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Vector3D](vector3d/unapplying(_:)-4uxr2.md)
  Returns a vector that’s transformed by the inverse of the specified scaled pose.
### Comparing values
- [static func == (Vector3D, Vector3D) -> Bool](vector3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Encoding and decoding a vector
- [init(from: any Decoder) throws](vector3d/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](vector3d/encode(to:).md)
  Encodes this value into the given encoder.
### Type properties
- [static let forward: Vector3D](vector3d/forward.md)
  A vector that contains the values 0, 0, 1.
- [static let right: Vector3D](vector3d/right.md)
  A vector that contains the values 1, 0, 0.
- [static let up: Vector3D](vector3d/up.md)
  A vector that contains the values 0, 1, 0.
### Applying arithmetic operations
- [static func * (Vector3D, Double) -> Vector3D](vector3d/*(_:_:)-dcwn.md)
  Returns a vector that’s the product of a vector and a scalar value.
- [static func * (Double, Vector3D) -> Vector3D](vector3d/*(_:_:)-64lzt.md)
  Returns a vector that’s the product of a scalar value and a vector.
- [static func * (AffineTransform3D, Vector3D) -> Vector3D](vector3d/*(_:_:)-6rxsr.md)
  Returns the vector that results from applying the affine transform to the vector.
- [static func * (ProjectiveTransform3D, Vector3D) -> Vector3D](vector3d/*(_:_:)-3dpli.md)
  Returns the vector that results from applying the projective transform to the vector.
- [static func * (Pose3D, Vector3D) -> Vector3D](vector3d/*(_:_:)-8y7xq.md)
  Returns a new vector after applying the pose to the vector.
- [static func + (Vector3D, Vector3D) -> Vector3D](vector3d/+(_:_:)-7gbcj.md)
  Returns a vector that’s the element-wise sum of two sizes.
- [static func + (Vector3D, Size3D) -> Size3D](vector3d/+(_:_:)-9xfxv.md)
  Returns a vector that’s the element-wise sum of a vector and a size.
- [static func + (Size3D, Vector3D) -> Size3D](vector3d/+(_:_:)-1xufx.md)
  Returns a vector that’s the element-wise sum of a size and a vector.
- [static func + (Vector3D, Point3D) -> Point3D](vector3d/+(_:_:)-1bq1m.md)
  Returns a vector that’s the element-wise sum of a vector and a point.
- [static func + (Point3D, Vector3D) -> Point3D](vector3d/+(_:_:)-4rsou.md)
  Returns a vector that’s the element-wise sum of a point and a vector.
- [static func - (Vector3D) -> Vector3D](vector3d/-(_:).md)
  Returns a vector that’s the element-wise negation of the vector.
- [static func - (Vector3D, Vector3D) -> Vector3D](vector3d/-(_:_:)-6zam.md)
  Returns a size that’s the element-wise difference of two vectors.
- [static func - (Vector3D, Size3D) -> Size3D](vector3d/-(_:_:)-6lui1.md)
  Returns a size that’s the element-wise difference of a vector and a size.
- [static func - (Size3D, Vector3D) -> Size3D](vector3d/-(_:_:)-3qpww.md)
  Returns a size that’s the element-wise difference of a size and a vector.
- [static func - (Vector3D, Point3D) -> Point3D](vector3d/-(_:_:)-1nz82.md)
  Returns a size that’s the element-wise difference of a vector and a point.
- [static func - (Point3D, Vector3D) -> Point3D](vector3d/-(_:_:)-8sgai.md)
  Returns a size that’s the element-wise difference of a point and a vector.
- [static func *= (inout Vector3D, Double)](vector3d/*=(_:_:).md)
  Multiplies a vector and a double-precision value, and stores the result in the left-hand-side variable.
- [static func += (inout Vector3D, Vector3D)](vector3d/+=(_:_:).md)
  Adds two vectors and stores the result in the left-hand-side variable.
- [static func -= (inout Vector3D, Vector3D)](vector3d/-=(_:_:).md)
  Subtracts a vector from a vector and stores the difference in the left-hand-side variable.
- [static func / (Vector3D, Double) -> Vector3D](vector3d/_(_:_:).md)
  Returns a vector with each element divided by a scalar value.
- [static func /= (inout Vector3D, Double)](vector3d/_=(_:_:).md)
  Divides a vector by a scalar value and stores the result in the left-hand-side variable.
### Initializers
- [init(simd_packed_double4)](vector3d/init(_:)-23qst.md)
  Creates a Spatial vector from a simd packed vector.
- [init(Vector3DFloat)](vector3d/init(_:)-272sg.md)
  Returns a double-precision vector from a single-precision vector.
### Type Methods
- [static func lerp(from: Vector3D, to: Vector3D, t: Vector3D) -> Vector3D](vector3d/lerp(from:to:t:).md)
  Returns a Spatial vector that represents the linear interpolation at `t` between two vectors.
- [static func smoothstep(edge0: Vector3D, edge1: Vector3D, x: Vector3D) -> Vector3D](vector3d/smoothstep(edge0:edge1:x:).md)
  Returns a Spatial vector that represents the smooth interpolation at `x` between two vectors.
### Default Implementations
- [AdditiveArithmetic Implementations](vector3d/additivearithmetic-implementations.md)
- [CustomReflectable Implementations](vector3d/customreflectable-implementations.md)
- [Decodable Implementations](vector3d/decodable-implementations.md)
- [Encodable Implementations](vector3d/encodable-implementations.md)
- [Equatable Implementations](vector3d/equatable-implementations.md)
- [Hashable Implementations](vector3d/hashable-implementations.md)
- [Primitive3DProtocol Implementations](vector3d/primitive3dprotocol-implementations.md)
- [ProjectiveTransformable3D Implementations](vector3d/projectivetransformable3d-implementations.md)
- [Rotatable3DProtocol Implementations](vector3d/rotatable3dprotocol-implementations.md)
- [Scalable3DProtocol Implementations](vector3d/scalable3dprotocol-implementations.md)
- [Shearable3D Implementations](vector3d/shearable3d-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Animatable](../SwiftUI/Animatable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Primitive3D](primitive3d.md)
- [Primitive3DProtocol](primitive3dprotocol.md)
- [ProjectiveTransformable3D](projectivetransformable3d.md)
- [Rotatable3D](rotatable3d.md)
- [Rotatable3DProtocol](rotatable3dprotocol.md)
- [Scalable3D](scalable3d.md)
- [Scalable3DProtocol](scalable3dprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Shearable3D](shearable3d.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
- [VectorArithmetic](../SwiftUI/VectorArithmetic.md)

## See Also

- [struct Vector3DFloat](vector3dfloat.md)
  A single-precision structure that defines a three-element vector
- [struct Axis3D](axis3d.md)
  Constants that describe an axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3d)*