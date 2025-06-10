# SphericalCoordinates3D

**Framework**: Spatial  
**Kind**: struct

A structure that defines spherical coordinates in radial, inclination, azimuthal order.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct SphericalCoordinates3D
```

## Topics

### Creating a spherical coordinates structure
- [init()](sphericalcoordinates3d/init.md)
  Creates a spherical coordinates structure.
- [init(Vector3D)](sphericalcoordinates3d/init(_:)-2eoox.md)
  Creates a spherical coordinates structure from the Cartesian coordinates represented by the specified simd vector.
- [init(Point3D)](sphericalcoordinates3d/init(_:)-45qdy.md)
  Creates a spherical coordinates structure from the Cartesian coordinates represented by the specified Spatial point.
- [init(simd_double3)](sphericalcoordinates3d/init(_:)-1xzjz.md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates represented by a simd vector.
- [init(radius: Double, inclination: Angle2D, azimuth: Angle2D)](sphericalcoordinates3d/init(radius:inclination:azimuth:).md)
  Creates a new spherical coordinates structure with the specified radius, inclination, and azimuth.
- [init(vector: simd_double3)](sphericalcoordinates3d/init(vector:).md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates represented by a simd vector.
- [init(x: Double, y: Double, z: Double)](sphericalcoordinates3d/init(x:y:z:).md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates.
### Inspecting a spherical coordinates structure’s properties
- [var azimuth: Angle2D](sphericalcoordinates3d/azimuth.md)
  The azimuthal angle, in radians.
- [var inclination: Angle2D](sphericalcoordinates3d/inclination.md)
  The inclination angle, in radians.
- [var radius: Double](sphericalcoordinates3d/radius.md)
  The distance to the origin.
- [var vector: simd_double3](sphericalcoordinates3d/vector.md)
  A simd three-element vector that contains the radius, inclination, and azimuth values.
- [var customMirror: Mirror](sphericalcoordinates3d/custommirror.md)
  The custom mirror for this instance.
### Initializers
- [init(SphericalCoordinates3DFloat)](sphericalcoordinates3d/init(_:)-1hxjg.md)
  Returns a double-precision spherical coordinates structure from a single-precision spherical coordinates structure.
- [init(simd_packed_double4)](sphericalcoordinates3d/init(_:)-91oq0.md)
  Creates a Spatial spherical coordinates structure from a simd packed vector.
### Default Implementations
- [CustomReflectable Implementations](sphericalcoordinates3d/customreflectable-implementations.md)
- [Decodable Implementations](sphericalcoordinates3d/decodable-implementations.md)
- [Encodable Implementations](sphericalcoordinates3d/encodable-implementations.md)
- [Equatable Implementations](sphericalcoordinates3d/equatable-implementations.md)
- [Hashable Implementations](sphericalcoordinates3d/hashable-implementations.md)

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
- [struct SphericalCoordinates3DFloat](sphericalcoordinates3dfloat.md)
  A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sphericalcoordinates3d)*