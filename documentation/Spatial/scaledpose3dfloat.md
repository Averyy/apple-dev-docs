# ScaledPose3DFloat

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
struct ScaledPose3DFloat
```

## Topics

### Operators
- [static func * (ScaledPose3DFloat, ScaledPose3DFloat) -> ScaledPose3DFloat](scaledpose3dfloat/*(_:_:)-2wclg.md)
  Returns a new scaled pose that’s constructed by concatenating two existing poses.
- [static func * (ScaledPose3DFloat, Pose3DFloat) -> ScaledPose3DFloat](scaledpose3dfloat/*(_:_:)-5qwyl.md)
  Returns a new pose that’s constructed by concatenating two existing poses.
- [static func * (Pose3DFloat, ScaledPose3DFloat) -> ScaledPose3DFloat](scaledpose3dfloat/*(_:_:)-9z6s.md)
  Returns a new scaled pose that’s constructed by concatenating a pose and a scaled pose.
- [static func *= (inout ScaledPose3DFloat, ScaledPose3DFloat)](scaledpose3dfloat/*=(_:_:).md)
  Calculates the concatenation of scaled poses and stores the result in the left-hand-side variable.
### Initializers
- [init()](scaledpose3dfloat/init.md)
- [init?(simd_float4x4)](scaledpose3dfloat/init(_:)-4hh5z.md)
  Creates a scaled pose with the specified single-precision 4 x 4 matrix
- [init(ScaledPose3D)](scaledpose3dfloat/init(_:)-7zqj3.md)
  Returns a single-precision scaled pose from a double-precision scaled pose.
- [init(forward: Vector3DFloat, scale: Float, up: Vector3DFloat)](scaledpose3dfloat/init(forward:scale:up:).md)
  Creates a scaled pose with the specified forward and up vectors.
- [init(position: Point3DFloat, rotation: Rotation3DFloat, scale: Float)](scaledpose3dfloat/init(position:rotation:scale:)-1j1mg.md)
  Creates a  scaled pose from Spatial primitives that describe the position, rotation, and scale.
- [init(position: Point3DFloat, rotation: Rotation3DFloat, scale: Float)](scaledpose3dfloat/init(position:rotation:scale:)-1xgkl.md)
  Creates a  scaled pose from Spatial primitives that describe the position, rotation, and scale.
- [init(position: simd_float3, rotation: simd_quatf, scale: Float)](scaledpose3dfloat/init(position:rotation:scale:)-3l2fe.md)
  Creates a pose from single-precision simd primitives that describe the position, rotation, and scale.
- [init(position: Point3DFloat, target: Point3DFloat, scale: Float, up: Vector3DFloat)](scaledpose3dfloat/init(position:target:scale:up:).md)
  Creates a scaled pose at the specified position that’s oriented towards a look at target.
- [init?(transform: AffineTransform3DFloat)](scaledpose3dfloat/init(transform:)-1m87a.md)
  Creates a scaled pose with with a position, rotation, and scale that are defined by an affine transform.
- [init?(transform: ProjectiveTransform3DFloat)](scaledpose3dfloat/init(transform:)-xeog.md)
  Creates a pose with with a position, rotation, and scale that are defined by a projective transform.
### Instance Properties
- [var inverse: ScaledPose3DFloat](scaledpose3dfloat/inverse.md)
  The inverse of the scaled pose’s underlying matrix.
- [var isIdentity: Bool](scaledpose3dfloat/isidentity.md)
  Returns true if the scaled pose is the identity pose.
- [var matrix: simd_float4x4](scaledpose3dfloat/matrix.md)
  A 4 x 4 matrix that represents the scaled pose’s scale, rotation, and translation.
- [var position: Point3DFloat](scaledpose3dfloat/position.md)
  The position
- [var rotation: Rotation3DFloat](scaledpose3dfloat/rotation.md)
  The rotation
- [var scale: Float](scaledpose3dfloat/scale.md)
  The uniform scale
### Instance Methods
- [func concatenating(ScaledPose3DFloat) -> ScaledPose3DFloat](scaledpose3dfloat/concatenating(_:)-3pywy.md)
  Returns a transform that’s constructed by concatenating two existing scaled poses.
- [func concatenating(Pose3DFloat) -> ScaledPose3DFloat](scaledpose3dfloat/concatenating(_:)-7ol75.md)
  Returns a transform that’s constructed by concatenating two a scaled pose and a pose.
- [func flip(along: Axis3D)](scaledpose3dfloat/flip(along:).md)
  Flips the scaled pose along the specified axis.
- [func flipped(along: Axis3D) -> ScaledPose3DFloat](scaledpose3dfloat/flipped(along:).md)
  Returns the scaled pose flipped along the specified axis.
- [func isApproximatelyEqual(to: ScaledPose3DFloat, tolerance: Float) -> Bool](scaledpose3dfloat/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two scaled poses are equal within a specified tolerance.
### Type Properties
- [static var identity: ScaledPose3DFloat](scaledpose3dfloat/identity.md)
  The identity scaled pose.
### Default Implementations
- [CustomReflectable Implementations](scaledpose3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](scaledpose3dfloat/decodable-implementations.md)
- [Encodable Implementations](scaledpose3dfloat/encodable-implementations.md)
- [Equatable Implementations](scaledpose3dfloat/equatable-implementations.md)
- [Hashable Implementations](scaledpose3dfloat/hashable-implementations.md)
- [Rotatable3DProtocol Implementations](scaledpose3dfloat/rotatable3dprotocol-implementations.md)

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
- [struct Pose3DFloat](pose3dfloat.md)
  A single-precision structure that contains a position and rotation.
- [struct ScaledPose3D](scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct SphericalCoordinates3DFloat](sphericalcoordinates3dfloat.md)
  A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3dfloat)*