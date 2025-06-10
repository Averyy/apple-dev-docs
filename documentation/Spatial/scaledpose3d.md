# ScaledPose3D

**Framework**: Spatial  
**Kind**: struct

A structure that contains a position, rotation, and scale.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct ScaledPose3D
```

## Topics

### Creating a 3D scaled-pose structure
- [init()](scaledpose3d/init.md)
  Creates a scaled pose structure.
- [init?(simd_float4x4)](scaledpose3d/init(_:)-v6ox.md)
  Creates a scaled pose from the specified 4 x 4 single-precision matrix.
- [init?(simd_double4x4)](scaledpose3d/init(_:)-4izkj.md)
  Creates a scaled pose from the specified 4 x 4 double-precision matrix.
- [init(forward: Vector3D, scale: Double, up: Vector3D)](scaledpose3d/init(forward:scale:up:).md)
  Creates a scaled pose with the specified forward and up vectors.
- [init(position: simd_float3, rotation: simd_quatf, scale: Float)](scaledpose3d/init(position:rotation:scale:)-8ndo4.md)
  Creates a scaled pose with the specified single-precision position vector and quaternion.
- [init(position: simd_double3, rotation: simd_quatd, scale: Double)](scaledpose3d/init(position:rotation:scale:)-6fom1.md)
  Creates a scaled pose with the specified double-precision position vector and quaternion.
- [init(position: Point3D, target: Point3D, scale: Double, up: Vector3D)](scaledpose3d/init(position:target:scale:up:).md)
  Returns a scaled pose at the specified position with the rotation toward the target.
- [init(position: Point3D, rotation: Rotation3D, scale: Double)](scaledpose3d/init(position:rotation:scale:)-7ya6f.md)
  Creates a pose with the specified Spatial position, rotation, and scale structures.
- [init(position: Point3D, rotation: Rotation3D, scale: Double)](scaledpose3d/init(position:rotation:scale:)-8fyu0.md)
  Creates a scaled pose with the specified double-precision position vector and quaternion.
- [init?(transform: AffineTransform3D)](scaledpose3d/init(transform:)-oogv.md)
  Returns a scaled pose with a position, rotation, and scale defined by an affine transform.
- [init?(transform: ProjectiveTransform3D)](scaledpose3d/init(transform:)-9s08k.md)
  Returns a scaled pose with a position, rotation, and scale defined by a projective transform.
### Inspecting a 3D scaled pose’s properties
- [var matrix: simd_double4x4](scaledpose3d/matrix.md)
  The scaled pose’s underlying matrix.
- [var position: Point3D](scaledpose3d/position.md)
  The scaled pose’s position.
- [var rotation: Rotation3D](scaledpose3d/rotation.md)
  The scaled pose’s rotation.
- [var scale: Double](scaledpose3d/scale.md)
  The scaled pose’s scale.
- [var inverse: ScaledPose3D](scaledpose3d/inverse.md)
  The scaled pose’s inverse.
- [var customMirror: Mirror](scaledpose3d/custommirror.md)
  A mirror that reflects the notification.
- [static var identity: ScaledPose3D](scaledpose3d/identity.md)
  The identity scaled pose.
### Transforming a 3D scaled-pose structure
- [func flip(along: Axis3D)](scaledpose3d/flip(along:).md)
  Flips a scaled pose along the specified axis.
- [func flipped(along: Axis3D) -> ScaledPose3D](scaledpose3d/flipped(along:).md)
  Returns a scaled pose that results from flipping it along the specified axis.
- [func rotated(by: simd_quatd) -> ScaledPose3D](scaledpose3d/rotated(by:)-5mxbl.md)
  Returns a scaled pose that results from rotating with the specified quaternion.
- [func rotated(by: Rotation3D) -> ScaledPose3D](scaledpose3d/rotated(by:)-x75b.md)
  Returns a scaled pose that results from applying the specified rotation.
- [func concatenating(ScaledPose3D) -> ScaledPose3D](scaledpose3d/concatenating(_:)-c38k.md)
  Returns a scaled pose that represents the concatenation of two scaled poses.
- [func concatenating(Pose3D) -> ScaledPose3D](scaledpose3d/concatenating(_:)-2xzgs.md)
  Returns a scaled pose that represents the concatenation of two poses.
### Checking characteristics
- [var isIdentity: Bool](scaledpose3d/isidentity.md)
  Returns a Boolean value that indicates whether the scaled pose is the identity transform.
### Comparing values
- [func isApproximatelyEqual(to: ScaledPose3D, tolerance: Double) -> Bool](scaledpose3d/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two scaled poses are equal within a specified tolerance.
- [static func == (ScaledPose3D, ScaledPose3D) -> Bool](scaledpose3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Applying arithmetic operations
- [static func * (ScaledPose3D, ScaledPose3D) -> ScaledPose3D](scaledpose3d/*(_:_:)-6nx9h.md)
  Returns the concatenation of two scaled poses.
- [static func * (ScaledPose3D, Pose3D) -> ScaledPose3D](scaledpose3d/*(_:_:)-93yyr.md)
  Returns the concatenation of a scaled pose and a pose.
- [static func * (Pose3D, ScaledPose3D) -> ScaledPose3D](scaledpose3d/*(_:_:)-179zu.md)
  Returns the concatenation of a pose and a scaled pose.
- [static func *= (inout ScaledPose3D, ScaledPose3D)](scaledpose3d/*=(_:_:).md)
  Concatenates two scaled poses and stores the result in the left-hand-side variable.
### Initializers
- [init(ScaledPose3DFloat)](scaledpose3d/init(_:)-3fa9n.md)
  Returns a double-precision scaled pose from a single-precision scaled pose.
### Default Implementations
- [CustomReflectable Implementations](scaledpose3d/customreflectable-implementations.md)
- [Decodable Implementations](scaledpose3d/decodable-implementations.md)
- [Encodable Implementations](scaledpose3d/encodable-implementations.md)
- [Equatable Implementations](scaledpose3d/equatable-implementations.md)
- [Hashable Implementations](scaledpose3d/hashable-implementations.md)
- [Rotatable3D Implementations](scaledpose3d/rotatable3d-implementations.md)

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
- [Translatable3D](translatable3d.md)
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
- [struct ScaledPose3DFloat](scaledpose3dfloat.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct SphericalCoordinates3DFloat](sphericalcoordinates3dfloat.md)
  A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d)*