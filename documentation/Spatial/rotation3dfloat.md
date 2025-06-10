# Rotation3DFloat

**Framework**: Spatial  
**Kind**: struct

A single-precision structure that represents a rotation in three dimensions.

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
struct Rotation3DFloat
```

## Topics

### Operators
- [static func * (Rotation3DFloat, Float) -> Rotation3DFloat](rotation3dfloat/*(_:_:)-2mmaj.md)
  Calculates the spherical linear interpolation between the identity rotation and the LHS rotation at the RHS interpolation parameter.
- [static func * (Rotation3DFloat, Rotation3DFloat) -> Rotation3DFloat](rotation3dfloat/*(_:_:)-30js8.md)
  Calculates the product of two rotations.
- [static func * (Float, Rotation3DFloat) -> Rotation3DFloat](rotation3dfloat/*(_:_:)-99umr.md)
  Calculates the spherical linear interpolation between the identity rotation and the RHS rotation at the LHS interpolation parameter.
- [static func *= (inout Rotation3DFloat, Rotation3DFloat)](rotation3dfloat/*=(_:_:).md)
  Calculates the product of two rotations and stores the result in the left-hand-side variable.
### Initializers
- [init()](rotation3dfloat/init-4vjiv.md)
- [init()](rotation3dfloat/init-4y09q.md)
- [init(simd_quatf)](rotation3dfloat/init(_:)-140am.md)
- [init(simd_quatd)](rotation3dfloat/init(_:)-20sue.md)
  Returns a new rotation from a double-precision quaternion.
- [init(Rotation3D)](rotation3dfloat/init(_:)-5vfv0.md)
  Returns a single-precision rotation from a double-precision rotation.
- [init(simd_packed_float4)](rotation3dfloat/init(_:)-7mhwz.md)
  Creates a Spatial rotation from a simd packed vector.
- [init(angle: Angle2DFloat, axis: RotationAxis3DFloat)](rotation3dfloat/init(angle:axis:).md)
- [init(eulerAngles: EulerAnglesFloat)](rotation3dfloat/init(eulerangles:).md)
- [init(forward: Vector3DFloat)](rotation3dfloat/init(forward:).md)
  Returns a rotation with the specified forward vector.
- [init(forward: Vector3DFloat, up: Vector3DFloat)](rotation3dfloat/init(forward:up:).md)
- [init(position: Point3DFloat, target: Point3DFloat, up: Vector3DFloat)](rotation3dfloat/init(position:target:up:).md)
  Returns a rotation that’s the look at direction from the eye position to the target.
- [init(quaternion: simd_quatf)](rotation3dfloat/init(quaternion:).md)
### Instance Properties
- [var angle: Angle2DFloat](rotation3dfloat/angle.md)
  The angle of the rotation.
- [var axis: RotationAxis3DFloat](rotation3dfloat/axis.md)
  The axis of the rotation.
- [var inverse: Rotation3DFloat](rotation3dfloat/inverse.md)
- [var isIdentity: Bool](rotation3dfloat/isidentity.md)
- [var quaternion: simd_quatf](rotation3dfloat/quaternion.md)
- [var vector: simd_float4](rotation3dfloat/vector.md)
### Instance Methods
- [func eulerAngles(order: __SPEulerAngleOrder) -> EulerAnglesFloat](rotation3dfloat/eulerangles(order:).md)
- [func isApproximatelyEqual(to: Rotation3DFloat, tolerance: Float) -> Bool](rotation3dfloat/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two rotations are equal within a specified tolerance.
- [func swing(twistAxis: RotationAxis3DFloat) -> Rotation3DFloat](rotation3dfloat/swing(twistaxis:).md)
- [func swingTwist(twistAxis: RotationAxis3DFloat) -> (swing: Rotation3DFloat, twist: Rotation3DFloat)](rotation3dfloat/swingtwist(twistaxis:).md)
  Returns the rotation’s swing-twist decomposition for a given twist axis.
- [func twist(twistAxis: RotationAxis3DFloat) -> Rotation3DFloat](rotation3dfloat/twist(twistaxis:).md)
### Type Properties
- [static let identity: Rotation3DFloat](rotation3dfloat/identity.md)
  A single-precision structure that represents a rotation in three dimensions.
### Type Methods
- [static func slerp(from: Rotation3DFloat, to: Rotation3DFloat, t: Float, along: Rotation3D.SlerpPath) -> Rotation3DFloat](rotation3dfloat/slerp(from:to:t:along:).md)
  Returns the spherical linear interpolation along the either the shortest or longest arc between two rotations.
- [static func spline(leftEndpoint: Rotation3DFloat, from: Rotation3DFloat, to: Rotation3DFloat, rightEndpoint: Rotation3DFloat, t: Float) -> Rotation3DFloat](rotation3dfloat/spline(leftendpoint:from:to:rightendpoint:t:).md)
  Returns an interpolated value between two rotations along a spherical cubic spline.
### Default Implementations
- [CustomReflectable Implementations](rotation3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](rotation3dfloat/decodable-implementations.md)
- [Encodable Implementations](rotation3dfloat/encodable-implementations.md)
- [Equatable Implementations](rotation3dfloat/equatable-implementations.md)
- [Hashable Implementations](rotation3dfloat/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [struct Rotation3D](rotation3d.md)
  A rotation in three dimensions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat)*