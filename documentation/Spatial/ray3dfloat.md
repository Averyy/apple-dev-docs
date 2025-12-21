# Ray3DFloat

**Framework**: Spatial  
**Kind**: struct

A single-precision structure that contains the origin and direction of a 3D ray.

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
struct Ray3DFloat
```

## Topics

### Operators
- [static func * (Pose3DFloat, Ray3DFloat) -> Ray3DFloat](ray3dfloat/*(_:_:).md)
  Returns the point that results from applying the pose to the ray.
### Initializers
- [init()](ray3dfloat/init.md)
- [init(Ray3D)](ray3dfloat/init(_:).md)
  Returns a single-precision ray from a double-precision ray.
- [init(origin: Point3DFloat, direction: Vector3DFloat)](ray3dfloat/init(origin:direction:)-2oe8j.md)
  Creates a ray from Spatial primitives that describe the origin and direction.
- [init(origin: Point3DFloat, direction: Vector3DFloat)](ray3dfloat/init(origin:direction:)-32dzt.md)
  Creates a ray from Spatial primitives that describe the origin and direction.
- [init(origin: simd_float3, direction: simd_float3)](ray3dfloat/init(origin:direction:)-6g59d.md)
  Creates a ray from single-precision simd vectors that describe the origin and direction.
### Instance Properties
- [var direction: Vector3DFloat](ray3dfloat/direction.md)
  The direction of the ray.
- [var origin: Point3DFloat](ray3dfloat/origin.md)
  The origin of the ray.
### Instance Methods
- [func applying(ScaledPose3DFloat) -> Ray3DFloat](ray3dfloat/applying(_:)-9e23e.md)
  Returns a ray that’s transformed by the specified scaled pose.
- [func intersects(Rect3DFloat) -> Bool](ray3dfloat/intersects(_:).md)
  Returns `true` if the the ray intersects the specified rectangle.
- [func intersects(sphereOrigin: Point3DFloat, sphereRadius: Float) -> Bool](ray3dfloat/intersects(sphereorigin:sphereradius:).md)
- [func rotated(by: simd_quatf, around: Point3DFloat) -> Ray3DFloat](ray3dfloat/rotated(by:around:)-4etjl.md)
  Returns a ray that’s rotated by the specified rotation around a specified pivot.
- [func rotated(by: Rotation3DFloat, around: Point3DFloat) -> Ray3DFloat](ray3dfloat/rotated(by:around:)-7tmtq.md)
  Returns a ray that’s rotated by the specified rotation around a specified pivot.
- [func unapplying(ScaledPose3DFloat) -> Ray3DFloat](ray3dfloat/unapplying(_:)-3zk38.md)
  Returns a ray that’s transformed by the inverse of the specified scaled pose.
### Default Implementations
- [CustomReflectable Implementations](ray3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](ray3dfloat/decodable-implementations.md)
- [Encodable Implementations](ray3dfloat/encodable-implementations.md)
- [Equatable Implementations](ray3dfloat/equatable-implementations.md)
- [Hashable Implementations](ray3dfloat/hashable-implementations.md)
- [Primitive3DProtocol Implementations](ray3dfloat/primitive3dprotocol-implementations.md)
- [Rotatable3DProtocol Implementations](ray3dfloat/rotatable3dprotocol-implementations.md)

## Relationships

### Conforms To
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
- [Translatable3DProtocol](translatable3dprotocol.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat)*