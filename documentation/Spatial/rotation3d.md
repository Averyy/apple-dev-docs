# Rotation3D

**Framework**: Spatial  
**Kind**: struct

A rotation in three dimensions.

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
struct Rotation3D
```

## Topics

### Creating a 3D rotation structure
- [init()](rotation3d/init-2uz53.md)
  Creates a rotation.
- [init()](rotation3d/init-krpj.md)
  Creates a rotation structure.
- [init(eulerAngles: EulerAngles)](rotation3d/init(eulerangles:).md)
  Creates a rotation structure with the specified Euler angles.
- [init(eulerAngles: EulerAngles)](rotation3d/init(eulerangles:).md)
  Creates a rotation structure with the specified Euler angles.
- [struct EulerAngles](eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [init(quaternion: simd_quatd)](rotation3d/init(quaternion:)-2c79y.md)
  Creates a rotation axis from the specified double-precision quaternion.
- [init(simd_quatd)](rotation3d/init(_:)-8z2bn.md)
  Creates a rotation from the specified double-precision quaternion.
- [init(simd_quatf)](rotation3d/init(_:)-829qb.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [init(angle: Angle2D, axis: RotationAxis3D)](rotation3d/init(angle:axis:).md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(position: Point3D, target: Point3D, up: Vector3D)](rotation3d/init(position:target:up:).md)
  Creates a rotation structure that represents the look-at direction from a position to a target.
- [init(forward: Vector3D)](rotation3d/init(forward:).md)
  Creates a rotation with the specified forward vector.
- [init(forward: Vector3D, up: Vector3D)](rotation3d/init(forward:up:).md)
  Creates a rotation with the specified forward and up vectors.
- [init(forward: Vector3D, up: Vector3D)](rotation3d/init(forward:up:).md)
  Creates a rotation with the specified forward and up vectors.
### Inspecting a 3D rotation’s properties
- [var angle: Angle2D](rotation3d/angle.md)
  The angle of the rotation.
- [var axis: RotationAxis3D](rotation3d/axis.md)
  The axis of the rotation.
- [func eulerAngles(order: __SPEulerAngleOrder) -> EulerAngles](rotation3d/eulerangles(order:).md)
  Returns a rotation’s Euler angles.
- [struct EulerAngles](eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [var quaternion: simd_quatd](rotation3d/quaternion.md)
  A quaternion that represents the rotation.
- [var vector: simd_double4](rotation3d/vector.md)
  The underlying vector of the rotation.
### Transforming a 3D rotation structure
- [static func slerp(from: Rotation3D, to: Rotation3D, t: Double, along: Rotation3D.SlerpPath) -> Rotation3D](rotation3d/slerp(from:to:t:along:).md)
  Returns the spherical linear interpolation along either the shortest or the longest arc between two rotations.
- [Rotation3D.SlerpPath](rotation3d/slerppath.md)
  Constants that define the arc that a slerp operation takes.
- [var inverse: Rotation3D](rotation3d/inverse.md)
  The inverse of the rotation.
- [static let identity: Rotation3D](rotation3d/identity.md)
  The identity rotation.
### Decomposing a 3D rotation structure
- [func swing(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/swing(twistaxis:).md)
  Returns the swing component of the rotation’s swing-twist decomposition for a given twist axis.
- [func twist(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/twist(twistaxis:).md)
  Returns the twist component of the rotation’s swing-twist decomposition for a given twist axis.
- [func swingTwist(twistAxis: RotationAxis3D) -> (swing: Rotation3D, twist: Rotation3D)](rotation3d/swingtwist(twistaxis:).md)
  Returns the rotation’s swing-twist decomposition for a given twist axis.
- [func swing(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/swing(twistaxis:).md)
  Returns the swing component of the rotation’s swing-twist decomposition for a given twist axis.
- [func twist(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/twist(twistaxis:).md)
  Returns the twist component of the rotation’s swing-twist decomposition for a given twist axis.
### Checking characteristics
- [var isIdentity: Bool](rotation3d/isidentity.md)
  A Boolean value that indicates whether the rotation is the identity rotation.
- [var isIdentity: Bool](rotation3d/isidentity.md)
  A Boolean value that indicates whether the rotation is the identity rotation.
### Comparing values
- [func isApproximatelyEqual(to: Rotation3D, tolerance: Double) -> Bool](rotation3d/isapproximatelyequal(to:tolerance:).md)
- [static func == (Rotation3D, Rotation3D) -> Bool](rotation3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Applying arithmetic operations
- [static func * (Rotation3D, Rotation3D) -> Rotation3D](rotation3d/*(_:_:)-1tc8f.md)
  Returns the product of two rotations.
- [static func * (Rotation3D, Double) -> Rotation3D](rotation3d/*(_:_:)-5dxqv.md)
  Returns the spherical linear interpolation between the identity rotation and the left-hand-side rotation at the right-hand-side interpolation parameter.
- [static func * (Double, Rotation3D) -> Rotation3D](rotation3d/*(_:_:)-9t389.md)
  Returns the spherical linear interpolation between the identity rotation and the right-hand-side rotation at the left-hand-side interpolation parameter.
- [func * <T>(Rotation3D, T) -> T](*(_:_:).md)
  Returns the rotatable entity that results from applying the rotatable entity.
- [static func *= (inout Rotation3D, Rotation3D)](rotation3d/*=(_:_:).md)
  Computes the product of two rotations and stores the result in the left-hand-side variable.
### Interpolating a 3D rotation structure
- [static func spline(leftEndpoint: Rotation3D, from: Rotation3D, to: Rotation3D, rightEndpoint: Rotation3D, t: Double) -> Rotation3D](rotation3d/spline(leftendpoint:from:to:rightendpoint:t:).md)
  Returns an interpolated value between two rotations along a spherical cubic spline.
### Deprecated symbols
- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](eulerangles/init(_:_:_:order:).md)
  Creates a new Euler angles structure from the specified angle structures and order.
- [init(eye: Point3D, target: Point3D, up: Vector3D)](rotation3d/init(eye:target:up:).md)
  Creates a rotation structure that’s the look-at direction from a position to a target.
- [init(axis: RotationAxis3D, angle: Angle2D)](rotation3d/init(axis:angle:).md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(quaternion: simd_quatf)](rotation3d/init(quaternion:)-6ajmn.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [static let zero: Rotation3D](rotation3d/zero.md)
  The rotation with the zero value.
- [var isZero: Bool](rotation3d/iszero.md)
  A Boolean value that indicates whether the rotation is zero.
### Initializers
- [init(Rotation3DFloat)](rotation3d/init(_:)-1r1iq.md)
  Returns a double-precision rotation from a single-precision rotation.
- [init(simd_packed_double4)](rotation3d/init(_:)-9yxln.md)
  Creates a Spatial rotation from a simd packed vector.
- [init(quaternion: simd_quatd)](rotation3d/init(quaternion:)-500aq.md)
### Default Implementations
- [CustomReflectable Implementations](rotation3d/customreflectable-implementations.md)
- [Decodable Implementations](rotation3d/decodable-implementations.md)
- [Encodable Implementations](rotation3d/encodable-implementations.md)
- [Equatable Implementations](rotation3d/equatable-implementations.md)
- [Hashable Implementations](rotation3d/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Rotatable3D](rotatable3d.md)
- [Rotatable3DProtocol](rotatable3dprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d)*