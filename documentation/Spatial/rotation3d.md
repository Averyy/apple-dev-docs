# Rotation3D

**Framework**: Spatial  
**Kind**: struct  
**Role**: Structure

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

```c
typedef union { ... } SPRotation3D;
```

## Topics

### Creating a 3D rotation structure
- [init()](./rotation3d/init%28%29-2uz53.md)
  Creates a rotation.
- [init()](./rotation3d/init%28%29-krpj.md)
  Creates a rotation structure.
- [init(eulerAngles: EulerAngles)](./rotation3d/init%28eulerangles%29.md)
  Creates a rotation structure with the specified Euler angles.
- [init(eulerAngles: EulerAngles)](./rotation3d/init%28eulerangles%29.md)
  Creates a rotation structure with the specified Euler angles.
- [struct EulerAngles](./eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [init(quaternion: simd_quatd)](./rotation3d/init%28quaternion%29-2c79y.md)
  Creates a rotation axis from the specified double-precision quaternion.
- [init(simd_quatd)](./rotation3d/init%28_%29-8z2bn.md)
  Creates a rotation from the specified double-precision quaternion.
- [init(simd_quatf)](./rotation3d/init%28_%29-829qb.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [init(angle: Angle2D, axis: RotationAxis3D)](./rotation3d/init%28angle,axis%29.md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(position: Point3D, target: Point3D, up: Vector3D)](./rotation3d/init%28position,target,up%29.md)
  Creates a rotation structure that represents the look-at direction from a position to a target.
- [init(forward: Vector3D)](./rotation3d/init%28forward%29.md)
  Creates a rotation with the specified forward vector.
- [init(forward: Vector3D, up: Vector3D)](./rotation3d/init%28forward,up%29.md)
  Creates a rotation with the specified forward and up vectors.
- [init(forward: Vector3D, up: Vector3D)](./rotation3d/init%28forward,up%29.md)
  Creates a rotation with the specified forward and up vectors.
- [SPRotation3DMakeWithQuaternion](./sprotation3dmakewithquaternion.md)
- [SPRotation3DMake](./sprotation3dmake-2i9jt.md)
  Creates a rotation structure.
- [SPRotation3DMakeLookAt](./sprotation3dmakelookat-6ypo8.md)
  Creates a rotation structure that’s the look-at direction from a position to a target.
- [SPRotation3DMakeLookAt](./sprotation3dmakelookat-4xrh6.md)
- [SPRotationAxis3DMakeWithVector](./sprotationaxis3dmakewithvector-1n9ib.md)
  Creates a rotation axis from the specified double-precision vector.
- [SPRotationAxis3DMakeWithVector](./sprotationaxis3dmakewithvector-kk1p.md)
### Inspecting a 3D rotation’s properties
- [var angle: Angle2D](./rotation3d/angle.md)
  The angle of the rotation.
- [var axis: RotationAxis3D](./rotation3d/axis.md)
  The axis of the rotation.
- [func eulerAngles(order: __SPEulerAngleOrder) -> EulerAngles](./rotation3d/eulerangles%28order%29.md)
  Returns a rotation’s Euler angles.
- [struct EulerAngles](./eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [var quaternion: simd_quatd](./rotation3d/quaternion.md)
  A quaternion that represents the rotation.
- [var vector: simd_double4](./rotation3d/vector.md)
  The underlying vector of the rotation.
- [SPRotation3DGetAngle](./sprotation3dgetangle.md)
  The angle of the rotation.
- [SPRotation3DGetAxis](./sprotation3dgetaxis.md)
  The axis of the rotation.
- [vector](./sprotation3d/vector.md)
  The underlying vector of the rotation.
- [SPRotation3DGetQuaternion](./sprotation3dgetquaternion.md)
  A quaternion that represents the rotation.
- [SPRotationAxis3DGetVector](./sprotationaxis3dgetvector.md)
  A simd three-element vector that contains the x-, y-, and z-coordinate values.
### Transforming a 3D rotation structure
- [static func slerp(from: Rotation3D, to: Rotation3D, t: Double, along: Rotation3D.SlerpPath) -> Rotation3D](./rotation3d/slerp%28from,to,t,along%29.md)
  Returns the spherical linear interpolation along either the shortest or the longest arc between two rotations.
- [Rotation3D.SlerpPath](./rotation3d/slerppath.md)
  Constants that define the arc that a slerp operation takes.
- [var inverse: Rotation3D](./rotation3d/inverse.md)
  The inverse of the rotation.
- [static let identity: Rotation3D](./rotation3d/identity.md)
  The identity rotation.
- [SPRotation3DSlerp](./sprotation3dslerp.md)
  Returns the spherical linear interpolation along the shortest arc between two rotations.
- [SPRotation3DSlerpLongest](./sprotation3dslerplongest.md)
  Returns the spherical linear interpolation along the longest arc between two rotations.
### Decomposing a 3D rotation structure
- [func swing(twistAxis: RotationAxis3D) -> Rotation3D](./rotation3d/swing%28twistaxis%29.md)
  Returns the swing component of the rotation’s swing-twist decomposition for a given twist axis.
- [func twist(twistAxis: RotationAxis3D) -> Rotation3D](./rotation3d/twist%28twistaxis%29.md)
  Returns the twist component of the rotation’s swing-twist decomposition for a given twist axis.
- [func swingTwist(twistAxis: RotationAxis3D) -> (swing: Rotation3D, twist: Rotation3D)](./rotation3d/swingtwist%28twistaxis%29.md)
  Returns the rotation’s swing-twist decomposition for a given twist axis.
- [func swing(twistAxis: RotationAxis3D) -> Rotation3D](./rotation3d/swing%28twistaxis%29.md)
  Returns the swing component of the rotation’s swing-twist decomposition for a given twist axis.
- [func twist(twistAxis: RotationAxis3D) -> Rotation3D](./rotation3d/twist%28twistaxis%29.md)
  Returns the twist component of the rotation’s swing-twist decomposition for a given twist axis.
### Checking characteristics
- [var isIdentity: Bool](./rotation3d/isidentity.md)
  A Boolean value that indicates whether the rotation is the identity rotation.
- [var isIdentity: Bool](./rotation3d/isidentity.md)
  A Boolean value that indicates whether the rotation is the identity rotation.
- [SPRotation3DIsValid](./sprotation3disvalid.md)
  A Boolean value that indicates whether the rotation represents a valid value.
- [SPRotation3DInvalid](./sprotation3dinvalid.md)
  The null rotation that represents an invalid value.
### Comparing values
- [func isApproximatelyEqual(to: Rotation3D, tolerance: Double) -> Bool](./rotation3d/isapproximatelyequal%28to,tolerance%29.md)
- [static func == (Rotation3D, Rotation3D) -> Bool](./rotation3d/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two values are equal.
- [SPRotation3DEqualToRotation](./sprotation3dequaltorotation.md)
  Returns a Boolean value that indicates whether two values are equal.
- [SPRotation3DAlmostEqualToRotation](./sprotation3dalmostequaltorotation-53c20.md)
- [SPRotation3DAlmostEqualToRotation](./sprotation3dalmostequaltorotation-3deix.md)
### Applying arithmetic operations
- [static func * (Rotation3D, Rotation3D) -> Rotation3D](./rotation3d/star%28_,_%29-1tc8f.md)
  Returns the product of two rotations.
- [static func * (Rotation3D, Double) -> Rotation3D](./rotation3d/star%28_,_%29-5dxqv.md)
  Returns the spherical linear interpolation between the identity rotation and the left-hand-side rotation at the right-hand-side interpolation parameter.
- [static func * (Double, Rotation3D) -> Rotation3D](./rotation3d/star%28_,_%29-9t389.md)
  Returns the spherical linear interpolation between the identity rotation and the right-hand-side rotation at the left-hand-side interpolation parameter.
- [func * <T>(Rotation3D, T) -> T](./star%28_,_%29.md)
  Returns the rotatable entity that results from applying the rotatable entity.
- [static func *= (inout Rotation3D, Rotation3D)](./rotation3d/stareq%28_,_%29.md)
  Computes the product of two rotations and stores the result in the left-hand-side variable.
### Interpolating a 3D rotation structure
- [static func spline(leftEndpoint: Rotation3D, from: Rotation3D, to: Rotation3D, rightEndpoint: Rotation3D, t: Double) -> Rotation3D](./rotation3d/spline%28leftendpoint,from,to,rightendpoint,t%29.md)
  Returns an interpolated value between two rotations along a spherical cubic spline.
- [SPRotation3DSpline](./sprotation3dspline.md)
  Returns an interpolated value between two rotations along a spherical cubic spline.
### Deprecated symbols
- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](./eulerangles/init%28_,_,_,order%29.md)
  Creates a new Euler angles structure from the specified angle structures and order.
- [init(eye: Point3D, target: Point3D, up: Vector3D)](./rotation3d/init%28eye,target,up%29.md)
  Creates a rotation structure that’s the look-at direction from a position to a target.
- [init(axis: RotationAxis3D, angle: Angle2D)](./rotation3d/init%28axis,angle%29.md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(quaternion: simd_quatf)](./rotation3d/init%28quaternion%29-6ajmn.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [static let zero: Rotation3D](./rotation3d/zero.md)
  The rotation with the zero value.
- [var isZero: Bool](./rotation3d/iszero.md)
  A Boolean value that indicates whether the rotation is zero.
- [SPEulerAngleOrder](./speulerangleorder.md)
  Constants that describe the order of Euler angles.
### Initializers
- [init(Rotation3DFloat)](./rotation3d/init%28_%29-1r1iq.md)
  Returns a double-precision rotation from a single-precision rotation.
- [init(simd_packed_double4)](./rotation3d/init%28_%29-9yxln.md)
  Creates a Spatial rotation from a simd packed vector.
- [init(quaternion: simd_quatd)](./rotation3d/init%28quaternion%29-500aq.md)
### Default Implementations
- [CustomReflectable Implementations](./rotation3d/customreflectable-implementations.md)
- [Decodable Implementations](./rotation3d/decodable-implementations.md)
- [Encodable Implementations](./rotation3d/encodable-implementations.md)
- [Equatable Implementations](./rotation3d/equatable-implementations.md)
- [Hashable Implementations](./rotation3d/hashable-implementations.md)
- [ProjectiveTransformable3D Implementations](./rotation3d/projectivetransformable3d-implementations.md)
### Setting a 3D rotation’s properties
- [SPRotation3DSetAngle](./sprotation3dsetangle.md)
  Sets a rotation’s angle.
- [SPRotation3DSetAxis](./sprotation3dsetaxis.md)
  Sets a rotation’s axis.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [ProjectiveTransformable3D](./projectivetransformable3d.md)
- [Rotatable3D](./rotatable3d.md)
- [Rotatable3DProtocol](./rotatable3dprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SpatialTypeProtocol](./spatialtypeprotocol.md)

## See Also

### 3D primitives
- [struct Point3D](./point3d.md)
  A point in a 3D coordinate system.
- [struct Point3DFloat](./point3dfloat.md)
  A single-precision structure that contains a point in a three-dimensional coordinate system.
- [struct Size3D](./size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
- [struct Size3DFloat](./size3dfloat.md)
  A single-precision structure that contains width, height, and depth values.
- [struct Rect3D](./rect3d.md)
  A rectangle in a 3D coordinate system.
- [struct Rect3DFloat](./rect3dfloat.md)
  A single-precision structure that contains the location and dimensions of a 3D rectangle.
- [struct Rotation3DFloat](./rotation3dfloat.md)
  A single-precision structure that represents a rotation in three dimensions.
- [struct RotationAxis3D](./rotationaxis3d.md)
  A 3D rotation axis.
- [struct RotationAxis3DFloat](./rotationaxis3dfloat.md)
  A 3D axis.
- [struct Pose3D](./pose3d.md)
  A structure that contains a 3D position and a 3D rotation.
- [struct Pose3DFloat](./pose3dfloat.md)
  A single-precision structure that contains a position and rotation.
- [struct ScaledPose3D](./scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct ScaledPose3DFloat](./scaledpose3dfloat.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](./sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct SphericalCoordinates3DFloat](./sphericalcoordinates3dfloat.md)
  A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d)*