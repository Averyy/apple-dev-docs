# SphericalCoordinates3DFloat

**Framework**: Spatial  
**Kind**: struct

A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct SphericalCoordinates3DFloat
```

## Topics

### Initializers
- [init()](sphericalcoordinates3dfloat/init.md)
- [init(Vector3DFloat)](sphericalcoordinates3dfloat/init(_:)-4t1io.md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates represented by a Spatial vector.
- [init(simd_float3)](sphericalcoordinates3dfloat/init(_:)-6dp94.md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates.
- [init(SphericalCoordinates3D)](sphericalcoordinates3dfloat/init(_:)-6lfdm.md)
  Returns a single-precision spherical coordinates structure from a double-precision spherical coordinates structure.
- [init(Point3DFloat)](sphericalcoordinates3dfloat/init(_:)-8zaur.md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates represented by a Spatial point.
- [init(simd_packed_float4)](sphericalcoordinates3dfloat/init(_:)-99axl.md)
  Creates a Spatial spherical coordinates structure from a simd packed vector.
- [init(radius: Float, inclination: Angle2DFloat, azimuth: Angle2DFloat)](sphericalcoordinates3dfloat/init(radius:inclination:azimuth:).md)
- [init(vector: simd_float3)](sphericalcoordinates3dfloat/init(vector:).md)
- [init(x: Float, y: Float, z: Float)](sphericalcoordinates3dfloat/init(x:y:z:).md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates.
### Instance Properties
- [var azimuth: Angle2DFloat](sphericalcoordinates3dfloat/azimuth.md)
- [var inclination: Angle2DFloat](sphericalcoordinates3dfloat/inclination.md)
- [var radius: Float](sphericalcoordinates3dfloat/radius.md)
- [var vector: simd_float3](sphericalcoordinates3dfloat/vector.md)
### Default Implementations
- [CustomReflectable Implementations](sphericalcoordinates3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](sphericalcoordinates3dfloat/decodable-implementations.md)
- [Encodable Implementations](sphericalcoordinates3dfloat/encodable-implementations.md)
- [Equatable Implementations](sphericalcoordinates3dfloat/equatable-implementations.md)
- [Hashable Implementations](sphericalcoordinates3dfloat/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sphericalcoordinates3dfloat)*