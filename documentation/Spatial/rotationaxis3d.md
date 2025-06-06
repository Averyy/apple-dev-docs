# RotationAxis3D

**Framework**: Spatial  
**Kind**: struct

A 3D rotation axis.

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
struct RotationAxis3D
```

## Topics

### Creating a 3D rotation axis structure
- [init()](rotationaxis3d/init.md)
  Creates a rotation axis.
- [init(simd_float3)](rotationaxis3d/init(_:)-96si4.md)
  Creates a rotation axis from the specified single-precision vector.
- [init(simd_double3)](rotationaxis3d/init(_:)-804sx.md)
  Creates a rotation axis from the specified double-precision vector.
- [init(vector: simd_double3)](rotationaxis3d/init(vector:).md)
  Creates a rotation axis from a three-element double-precision vector.
- [init(Vector3D)](rotationaxis3d/init(_:)-2zdal.md)
  Creates a rotation axis from a Spatial vector.
- [init(x: Double, y: Double, z: Double)](rotationaxis3d/init(x:y:z:)-3z5nm.md)
  Creates a rotation axis from the specified double-precision values.
- [init<T>(x: T, y: T, z: T)](rotationaxis3d/init(x:y:z:)-1x93q.md)
  Creates a rotation axis from the specified floating-point values.
### Checking characteristics
- [var x: Double](rotationaxis3d/x-swift.property.md)
  The x-coordinate value.
- [var y: Double](rotationaxis3d/y-swift.property.md)
  The y-coordinate value.
- [var z: Double](rotationaxis3d/z-swift.property.md)
  The z-coordinate value.
- [var vector: simd_double3](rotationaxis3d/vector.md)
  A simd three-element vector that contains the x-, y-, and z-coordinate values.
- [var isZero: Bool](rotationaxis3d/iszero.md)
  A Boolean value that indicates whether the rotation axis is zero.
### Constants
- [static let x: RotationAxis3D](rotationaxis3d/x-swift.type.property.md)
  The x-axis, expressed in unit coordinates.
- [static let y: RotationAxis3D](rotationaxis3d/y-swift.type.property.md)
  The y-axis, expressed in unit coordinates.
- [static let z: RotationAxis3D](rotationaxis3d/z-swift.type.property.md)
  The z-axis, expressed in unit coordinates.
- [static let xy: RotationAxis3D](rotationaxis3d/xy.md)
  The xy-axis, expressed in unit coordinates.
- [static let yz: RotationAxis3D](rotationaxis3d/yz.md)
  The yz-axis, expressed in unit coordinates.
- [static let xz: RotationAxis3D](rotationaxis3d/xz.md)
  The xz-axis, expressed in unit coordinates.
- [static let xyz: RotationAxis3D](rotationaxis3d/xyz.md)
  The xyz-axis, expressed in unit coordinates.
- [static let zero: RotationAxis3D](rotationaxis3d/zero.md)
  The rotation axis with the zero value.
### Deprecated symbols
- [var simd: simd_double3](rotationaxis3d/simd.md)
  A simd three-element vector that contains the x-, y-, and z-coordinate values.
### Default Implementations
- [CustomReflectable Implementations](rotationaxis3d/customreflectable-implementations.md)
- [Decodable Implementations](rotationaxis3d/decodable-implementations.md)
- [Encodable Implementations](rotationaxis3d/encodable-implementations.md)
- [Equatable Implementations](rotationaxis3d/equatable-implementations.md)
- [Hashable Implementations](rotationaxis3d/hashable-implementations.md)

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

## See Also

- [struct Point3D](point3d.md)
  A point in a 3D coordinate system.
- [struct Size3D](size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
- [struct Rect3D](rect3d.md)
  A rectangle in a 3D coordinate system.
- [struct Rotation3D](rotation3d.md)
  A rotation in three dimensions.
- [struct Pose3D](pose3d.md)
  A structure that contains a 3D position and a 3D rotation.
- [struct ScaledPose3D](scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct Ray3D](ray3d.md)
  A ray in a 3D coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotationaxis3d)*