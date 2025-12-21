# Size3DFloat

**Framework**: Spatial  
**Kind**: struct

A single-precision structure that contains width, height, and depth values.

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
struct Size3DFloat
```

## Topics

### Operators
- [static func * (Float, Size3DFloat) -> Size3DFloat](size3dfloat/*(_:_:)-124fk.md)
  Returns a size with each element mulitplied by a scalar value.
- [static func * (Size3DFloat, Float) -> Size3DFloat](size3dfloat/*(_:_:)-544n3.md)
  Returns a size with each element mulitplied by a scalar value.
- [static func * (ProjectiveTransform3DFloat, Size3DFloat) -> Size3DFloat](size3dfloat/*(_:_:)-57yj1.md)
  Returns the size that results from applying the transform to the size.
- [static func * (Pose3DFloat, Size3DFloat) -> Size3DFloat](size3dfloat/*(_:_:)-61lpp.md)
  Returns the size that results from applying the pose to the size.
- [static func * (AffineTransform3DFloat, Size3DFloat) -> Size3DFloat](size3dfloat/*(_:_:)-7txph.md)
  Returns the size that results from applying the transform to the size.
- [static func *= (inout Size3DFloat, Float)](size3dfloat/*=(_:_:).md)
  Calculates the element-wise product of a size and a scalar value and stores the result in the left-hand-side variable.
- [static func += (inout Size3DFloat, Vector3DFloat)](size3dfloat/+=(_:_:)-6yxe6.md)
  Calculates the size that’s the element-wise sum of a size and a vector and stores the result in the left-hand-side variable.
- [static func - (Size3DFloat) -> Size3DFloat](size3dfloat/-(_:).md)
  Returns a size that’s the element-wise negation of the size.
- [static func -= (inout Size3DFloat, Vector3DFloat)](size3dfloat/-=(_:_:)-4iec2.md)
  Calculates the size that’s the element-wise difference of a size and a vector and stores the result in the left-hand-side variable.
- [static func / (Size3DFloat, Float) -> Size3DFloat](size3dfloat/_(_:_:).md)
  Returns a size with each element divided by a scalar value.
- [static func /= (inout Size3DFloat, Float)](size3dfloat/_=(_:_:).md)
  Calculates the element-wise division of a size and a scalar value and stores the result in the left-hand-side variable.
### Initializers
- [init()](size3dfloat/init.md)
- [init(simd_float3)](size3dfloat/init(_:)-208lc.md)
  Returns a size structure from the specified 3-element vector.
- [init(Vector3DFloat)](size3dfloat/init(_:)-3z2u6.md)
  Returns a size structure from the specified Spatial vector.
- [init(Point3DFloat)](size3dfloat/init(_:)-4eoby.md)
  Returns a size structure from the specified point.
- [init(Size3D)](size3dfloat/init(_:)-4r1ha.md)
  Returns a single-precision size from a double-precision size.
- [init(simd_double3)](size3dfloat/init(_:)-6y249.md)
  Returns a new point from a single-precision vector.
- [init(simd_packed_float4)](size3dfloat/init(_:)-8nzza.md)
  Creates a Spatial size from a simd packed vector.
- [init(vector: simd_float3)](size3dfloat/init(vector:).md)
- [init<T>(width: T, height: T, depth: T)](size3dfloat/init(width:height:depth:)-8h26f.md)
  Returns a new point from the floating-point values.
- [init(width: Float, height: Float, depth: Float)](size3dfloat/init(width:height:depth:)-9u3g4.md)
  Returns a size structure from the specified values.
### Instance Properties
- [var depth: Float](size3dfloat/depth.md)
- [var height: Float](size3dfloat/height.md)
- [var vector: simd_float3](size3dfloat/vector.md)
- [var width: Float](size3dfloat/width.md)
### Instance Methods
- [func applying(ScaledPose3DFloat) -> Size3DFloat](size3dfloat/applying(_:)-4x5w1.md)
  Returns the primitive that results from applying a scaled pose to the primitive.
- [func sheared(AxisWithFactors) -> Size3DFloat](size3dfloat/sheared(_:).md)
  Returns a sheared size.
- [func unapplying(ScaledPose3DFloat) -> Size3DFloat](size3dfloat/unapplying(_:)-9dyaz.md)
  Returns the primitive that results from applying a scaled pose to the primitive.
### Type Properties
- [static let one: Size3DFloat](size3dfloat/one.md)
  A size with a width, height, and depth of `1`.
### Default Implementations
- [AdditiveArithmetic Implementations](size3dfloat/additivearithmetic-implementations.md)
- [CustomReflectable Implementations](size3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](size3dfloat/decodable-implementations.md)
- [Encodable Implementations](size3dfloat/encodable-implementations.md)
- [Equatable Implementations](size3dfloat/equatable-implementations.md)
- [Hashable Implementations](size3dfloat/hashable-implementations.md)
- [Primitive3DProtocol Implementations](size3dfloat/primitive3dprotocol-implementations.md)
- [Scalable3DProtocol Implementations](size3dfloat/scalable3dprotocol-implementations.md)
- [VolumetricProtocol Implementations](size3dfloat/volumetricprotocol-implementations.md)

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
- [Rotatable3DProtocol](rotatable3dprotocol.md)
- [Scalable3DProtocol](scalable3dprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
- [VolumetricProtocol](volumetricprotocol.md)

## See Also

- [struct Point3D](point3d.md)
  A point in a 3D coordinate system.
- [struct Point3DFloat](point3dfloat.md)
  A single-precision structure that contains a point in a three-dimensional coordinate system.
- [struct Size3D](size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/size3dfloat)*