# Pose3D

**Framework**: Spatial  
**Kind**: struct

A structure that contains a 3D position and a 3D rotation.

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
struct Pose3D
```

## Topics

### Creating a 3D pose structure
- [init()](pose3d/init.md)
  Creates a pose structure.
- [init?(simd_float4x4)](pose3d/init(_:)-8njy6.md)
  Creates a pose from the specified 4 x 4 single-precision matrix.
- [init?(simd_double4x4)](pose3d/init(_:)-9xspz.md)
  Creates a pose from the specified 4 x 4 double-precision matrix.
- [init(forward: Vector3D, up: Vector3D)](pose3d/init(forward:up:).md)
  Creates a pose with the specified forward and up vectors.
- [init(position: simd_float3, rotation: simd_quatf)](pose3d/init(position:rotation:)-1gu7k.md)
  Creates a pose with the specified single-precision position vector and quaternion.
- [init(position: Point3D, rotation: Rotation3D)](pose3d/init(position:rotation:)-5afaf.md)
  Creates a pose with the specified Spatial position and rotation structures.
- [init(position: Point3D, rotation: Rotation3D)](pose3d/init(position:rotation:)-5vswy.md)
  Creates a pose with the specified single-precision position vector and quaternion.
- [init(position: simd_double3, rotation: simd_quatd)](pose3d/init(position:rotation:)-zc2j.md)
  Creates a pose with the specified double-precision position vector and quaternion.
- [init(position: Point3D, target: Point3D, up: Vector3D)](pose3d/init(position:target:up:).md)
  Returns a pose at the specified position with the rotation towards the target.
- [init?(transform: AffineTransform3D)](pose3d/init(transform:)-2sey4.md)
  Returns a pose with a position and rotation defined by an affine transform.
- [init?(transform: ProjectiveTransform3D)](pose3d/init(transform:)-4go9c.md)
  Returns a pose with a position and rotation defined by a projective transform.
### Constants
- [static var identity: Pose3D](pose3d/identity.md)
  The identity pose.
### Inspecting a 3D pose’s properties
- [var matrix: simd_double4x4](pose3d/matrix.md)
  The pose’s underlying matrix.
- [var position: Point3D](pose3d/position.md)
  The pose’s position.
- [var rotation: Rotation3D](pose3d/rotation.md)
  The pose’s rotation.
- [var inverse: Pose3D](pose3d/inverse.md)
  The pose’s inverse.
### Transforming a 3D pose structure
- [func concatenating(ScaledPose3D) -> ScaledPose3D](pose3d/concatenating(_:)-4esra.md)
  Returns a pose that represents the concatenation of a scaled pose and a pose.
- [func concatenating(Pose3D) -> Pose3D](pose3d/concatenating(_:)-6dd2s.md)
  Returns a pose that represents the concatenation of two poses.
- [func flip(along: Axis3D)](pose3d/flip(along:).md)
  Flips a pose along the specified axis.
- [func flipped(along: Axis3D) -> Pose3D](pose3d/flipped(along:).md)
  Returns a pose that results from flipping it along the specified axis.
- [func rotated(by: simd_quatd) -> Pose3D](pose3d/rotated(by:)-10k2a.md)
  Returns a pose that results from rotating with the specified quaternion.
- [func rotated(by: Rotation3D) -> Pose3D](pose3d/rotated(by:)-377u.md)
  Returns a pose that results from applying the specified rotation.
### Checking characteristics
- [var isIdentity: Bool](pose3d/isidentity.md)
  A Boolean value that indicates whether the pose is the identity pose.
### Comparing values
- [func isApproximatelyEqual(to: Pose3D, tolerance: Double) -> Bool](pose3d/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two poses are equal within a specified tolerance.
- [static func == (Pose3D, Pose3D) -> Bool](pose3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Applying arithmetic operations
- [static func * (Pose3D, Pose3D) -> Pose3D](pose3d/*(_:_:).md)
  Returns the concatenation of two poses.
- [static func *= (inout Pose3D, Pose3D)](pose3d/*=(_:_:).md)
  Concatenates two poses and stores the result in the left-hand-side variable.
### Deprecated symbols
- [init?(matrix: simd_float4x4)](pose3d/init(matrix:)-63uwf.md)
- [init?(matrix: simd_double4x4)](pose3d/init(matrix:)-6698w.md)
### Default Implementations
- [CustomReflectable Implementations](pose3d/customreflectable-implementations.md)
- [Decodable Implementations](pose3d/decodable-implementations.md)
- [Encodable Implementations](pose3d/encodable-implementations.md)
- [Equatable Implementations](pose3d/equatable-implementations.md)
- [Hashable Implementations](pose3d/hashable-implementations.md)
- [Rotatable3D Implementations](pose3d/rotatable3d-implementations.md)

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
- [Sendable](../Swift/Sendable.md)
- [Translatable3D](translatable3d.md)

## See Also

- [struct Point3D](point3d.md)
  A point in a 3D coordinate system.
- [struct Size3D](size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
- [struct Rect3D](rect3d.md)
  A rectangle in a 3D coordinate system.
- [struct Rotation3D](rotation3d.md)
  A rotation in three dimensions.
- [struct RotationAxis3D](rotationaxis3d.md)
  A 3D rotation axis.
- [struct ScaledPose3D](scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct Ray3D](ray3d.md)
  A ray in a 3D coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3d)*