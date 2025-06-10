# RotationAxis3DFloat

**Framework**: Spatial  
**Kind**: struct

A 3D axis.

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
struct RotationAxis3DFloat
```

## Topics

### Initializers
- [init()](rotationaxis3dfloat/init.md)
- [init(simd_float3)](rotationaxis3dfloat/init(_:)-3r5wd.md)
  Returns a new rotation axis from a single-precision vector.
- [init(simd_double3)](rotationaxis3dfloat/init(_:)-4n1ej.md)
  Returns a new rotation axis from a double-precision vector.
- [init(Vector3DFloat)](rotationaxis3dfloat/init(_:)-4q4aa.md)
  Returns a new rotation axis from a Spatial vector.
- [init(RotationAxis3D)](rotationaxis3dfloat/init(_:)-6c919.md)
  Returns a single-precision rotation axis from a double-precision rotation axis.
- [init(simd_packed_float4)](rotationaxis3dfloat/init(_:)-72zxm.md)
  Creates a Spatial rotation axis from a simd packed vector.
- [init(vector: simd_float3)](rotationaxis3dfloat/init(vector:).md)
- [init(x: Float, y: Float, z: Float)](rotationaxis3dfloat/init(x:y:z:)-273jp.md)
  Returns a rotation axis from the specified values.
- [init<T>(x: T, y: T, z: T)](rotationaxis3dfloat/init(x:y:z:)-hx2.md)
  Returns a new rotation axis from the floating-point values.
### Instance Properties
- [var vector: simd_float3](rotationaxis3dfloat/vector.md)
- [var x: Float](rotationaxis3dfloat/x-swift.property.md)
  The x-axis value.
- [var y: Float](rotationaxis3dfloat/y-swift.property.md)
  The y-axis value.
- [var z: Float](rotationaxis3dfloat/z-swift.property.md)
  The z-axis value.
### Type Properties
- [static let x: RotationAxis3DFloat](rotationaxis3dfloat/x-swift.type.property.md)
  The x-axis, expressed in unit coordinates.
- [static let xy: RotationAxis3DFloat](rotationaxis3dfloat/xy.md)
  The xy-axis, expressed in unit coordinates.
- [static let xyz: RotationAxis3DFloat](rotationaxis3dfloat/xyz.md)
  The xyz-axis, expressed in unit coordinates.
- [static let xz: RotationAxis3DFloat](rotationaxis3dfloat/xz.md)
  The xz-axis, expressed in unit coordinates.
- [static let y: RotationAxis3DFloat](rotationaxis3dfloat/y-swift.type.property.md)
  The y-axis, expressed in unit coordinates.
- [static let yz: RotationAxis3DFloat](rotationaxis3dfloat/yz.md)
  The yz-axis, expressed in unit coordinates.
- [static let z: RotationAxis3DFloat](rotationaxis3dfloat/z-swift.type.property.md)
  The z-axis, expressed in unit coordinates.
- [static let zero: RotationAxis3DFloat](rotationaxis3dfloat/zero.md)
  A 3D axis.
### Default Implementations
- [CustomReflectable Implementations](rotationaxis3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](rotationaxis3dfloat/decodable-implementations.md)
- [Encodable Implementations](rotationaxis3dfloat/encodable-implementations.md)
- [Equatable Implementations](rotationaxis3dfloat/equatable-implementations.md)
- [Hashable Implementations](rotationaxis3dfloat/hashable-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotationaxis3dfloat)*