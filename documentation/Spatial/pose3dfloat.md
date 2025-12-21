# Pose3DFloat

**Framework**: Spatial  
**Kind**: struct

A single-precision structure that contains a position and rotation.

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
struct Pose3DFloat
```

## Topics

### Operators
- [static func * (Pose3DFloat, Pose3DFloat) -> Pose3DFloat](pose3dfloat/*(_:_:).md)
  Returns a new pose that’s constructed by concatenating two existing  poses.
- [static func *= (inout Pose3DFloat, Pose3DFloat)](pose3dfloat/*=(_:_:).md)
  Calculates the concatenation of poses and stores the result in the left-hand-side variable.
### Initializers
- [init()](pose3dfloat/init.md)
- [init?(simd_float4x4)](pose3dfloat/init(_:)-6yai5.md)
  Creates a pose with the specified double-precision 4 x 4 matrix
- [init(Pose3D)](pose3dfloat/init(_:)-91dxh.md)
  Returns a single-precision pose from a double-precision pose.
- [init(forward: Vector3DFloat, up: Vector3DFloat)](pose3dfloat/init(forward:up:).md)
  Creates a pose with the specified forward and up vectors.
- [init(position: simd_float3, rotation: simd_quatf)](pose3dfloat/init(position:rotation:)-1r25j.md)
  Creates a pose from double-precision simd primitives that describe the position and rotation.
- [init(position: Point3DFloat, rotation: Rotation3DFloat)](pose3dfloat/init(position:rotation:)-6979c.md)
  Creates a pose from Spatial primitives that describe the position and rotation.
- [init(position: Point3DFloat, rotation: Rotation3DFloat)](pose3dfloat/init(position:rotation:)-9nvnb.md)
  Creates a pose from Spatial primitives that describe the position and rotation.
- [init(position: Point3DFloat, target: Point3DFloat, up: Vector3DFloat)](pose3dfloat/init(position:target:up:).md)
  Creates a pose at the specified position that’s oriented towards a look at target.
- [init?(transform: AffineTransform3DFloat)](pose3dfloat/init(transform:)-7bffd.md)
  Creates a pose with with a position and rotation that are defined by an affine transform.
- [init?(transform: ProjectiveTransform3DFloat)](pose3dfloat/init(transform:)-94kwr.md)
  Creates a pose with with a position and rotation that are defined by a projective transform.
### Instance Properties
- [var inverse: Pose3DFloat](pose3dfloat/inverse.md)
  The inverse of the pose’s underlying matrix.
- [var isIdentity: Bool](pose3dfloat/isidentity.md)
  Returns `true` if the pose is the identity transform.
- [var matrix: simd_float4x4](pose3dfloat/matrix.md)
  A 4 x 4 matrix that represents the pose’s translation and rotation.
- [var position: Point3DFloat](pose3dfloat/position.md)
  The position
- [var rotation: Rotation3DFloat](pose3dfloat/rotation.md)
  The rotation
### Instance Methods
- [func concatenating(Pose3DFloat) -> Pose3DFloat](pose3dfloat/concatenating(_:)-2kbxs.md)
  Returns a transform that’s constructed by concatenating two existing poses.
- [func concatenating(ScaledPose3DFloat) -> ScaledPose3DFloat](pose3dfloat/concatenating(_:)-3anuw.md)
  Returns a transform that’s constructed by concatenating two a pose and a scaled pose.
- [func flip(along: Axis3D)](pose3dfloat/flip(along:).md)
  Flips the pose along the specified axis.
- [func flipped(along: Axis3D) -> Pose3DFloat](pose3dfloat/flipped(along:).md)
  Returns the pose flipped along the specified axis.
- [func isApproximatelyEqual(to: Pose3DFloat, tolerance: Float) -> Bool](pose3dfloat/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two poses are equal within a specified tolerance.
### Type Properties
- [static var identity: Pose3DFloat](pose3dfloat/identity.md)
  The identity pose.
### Default Implementations
- [CustomReflectable Implementations](pose3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](pose3dfloat/decodable-implementations.md)
- [Encodable Implementations](pose3dfloat/encodable-implementations.md)
- [Equatable Implementations](pose3dfloat/equatable-implementations.md)
- [Hashable Implementations](pose3dfloat/hashable-implementations.md)
- [Rotatable3DProtocol Implementations](pose3dfloat/rotatable3dprotocol-implementations.md)

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
- [struct ScaledPose3D](scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct ScaledPose3DFloat](scaledpose3dfloat.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct SphericalCoordinates3DFloat](sphericalcoordinates3dfloat.md)
  A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3dfloat)*