# ProjectiveTransform3D

**Framework**: Spatial  
**Kind**: struct

A 3D projective transformation matrix.

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
struct ProjectiveTransform3D
```

## Topics

### Creating a 3D projective transform structure
- [init()](projectivetransform3d/init-1clia.md)
  Creates a projective transform.
- [init()](projectivetransform3d/init-6c4f4.md)
  Returns a new identity projective transform.
- [init(simd_float4x4)](projectivetransform3d/init(_:)-7b2bq.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(simd_double4x4)](projectivetransform3d/init(_:)-6g88l.md)
  Creates a projective transform from the specified double-precision matrix.
- [init(matrix: simd_double4x4)](projectivetransform3d/init(matrix:)-8eg5x.md)
  Creates a projective transform from the specified 4 x 4 double-precision matrix.
- [init(AffineTransform3D)](projectivetransform3d/init(_:)-9t2jh.md)
  Creates a projective transform from the specified affine transform.
- [init(pose: Pose3D)](projectivetransform3d/init(pose:).md)
  Creates a projective transform from the specified pose structure.
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](projectivetransform3d/init(scale:rotation:translation:)-4h5wm.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(shear: AxisWithFactors)](projectivetransform3d/init(shear:).md)
  Creates a projective transform from the specified shear transform.
- [init(leftTangent: Double, rightTangent: Double, topTangent: Double, bottomTangent: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](projectivetransform3d/init(lefttangent:righttangent:toptangent:bottomtangent:nearz:farz:reversez:).md)
  Returns a projective transform from tangents for each side of its frustum.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double)](projectivetransform3d/init(fovy:aspectratio:nearz:farz:).md)
  Returns a projective transform with right-hand side perspective.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](projectivetransform3d/init(fovy:aspectratio:nearz:farz:reversez:).md)
- [init(scaledPose: ScaledPose3D)](projectivetransform3d/init(scaledpose:).md)
### Inspecting a 3D projective transform’s properties
- [var inverse: ProjectiveTransform3D?](projectivetransform3d/inverse.md)
  The projective transform’s inverse.
- [var scaleComponent: Size3D](projectivetransform3d/scalecomponent.md)
  The scale component of the projective transform.
- [var translation: Vector3D](projectivetransform3d/translation.md)
  The translation component of the projective transform.
- [var matrix: simd_double4x4](projectivetransform3d/matrix.md)
  The projective transform’s underlying matrix.
### Transforming a 3D projective transform structure
- [func sheared(AxisWithFactors) -> ProjectiveTransform3D](projectivetransform3d/sheared(_:).md)
  Returns a projective transform that results from shearing over an axis by shear factors for the other two axes.
- [enum AxisWithFactors](axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
- [func flip(along: Axis3D)](projectivetransform3d/flip(along:).md)
  Flips a projective transform along the specified axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3D](projectivetransform3d/flipped(along:).md)
  Returns a projective transform that results from flipping it along the specified axis.
### Decomposing a 3D projective transform
- [var rotation: Rotation3D?](projectivetransform3d/rotation.md)
  The projective transform’s rotation.
### Checking characteristics
- [func is3DProjection() -> Bool](projectivetransform3d/is3dprojection.md)
  Returns a Boolean value that indicates whether the transform is a 3D projection.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](projectivetransform3d/isuniform(overdimensions:).md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [var isAffine: Bool](projectivetransform3d/isaffine.md)
  A Boolean value that indicates whether the transform is affine.
- [var isInvertible: Bool](projectivetransform3d/isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.
### Comparing values
- [func isApproximatelyEqual(to: ProjectiveTransform3D, tolerance: Double) -> Bool](projectivetransform3d/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
### Applying arithmetic operations
- [static func * (ProjectiveTransform3D, ProjectiveTransform3D) -> ProjectiveTransform3D](projectivetransform3d/*(_:_:).md)
  Returns the concatenation of two projective transforms.
- [static func *= (inout ProjectiveTransform3D, ProjectiveTransform3D)](projectivetransform3d/*=(_:_:).md)
  Concatenates two projective transforms and stores the result in the left-hand-side variable.
### Deprecated symbols
- [var offset: Vector3D](projectivetransform3d/offset.md)
  The projective transform’s translation.
- [var scale: Size3D?](projectivetransform3d/scale.md)
  The projective transform’s scale.
- [func inverted() -> ProjectiveTransform3D?](projectivetransform3d/inverted.md)
  Returns a new transform that results from inverting an existing projective transform.
- [init(matrix: simd_float4x4)](projectivetransform3d/init(matrix:)-zfb.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(scale: Size3D, rotation: Rotation3D, translation: Size3D)](projectivetransform3d/init(scale:rotation:translation:)-8qxxq.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:reversez:).md)
  Returns a projective transform with right-hand-side perspective and optional reverse-z.
- [init(translation: Size3D)](projectivetransform3d/init(translation:).md)
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:).md)
### Initializers
- [init(ProjectiveTransform3DFloat)](projectivetransform3d/init(_:)-7nv9f.md)
  Returns a double-precision projective transformation from a single-precision projective transformation.
### Default Implementations
- [CustomReflectable Implementations](projectivetransform3d/customreflectable-implementations.md)
- [Scalable3DProtocol Implementations](projectivetransform3d/scalable3dprotocol-implementations.md)
- [Shearable3DProtocol Implementations](projectivetransform3d/shearable3dprotocol-implementations.md)
- [Transform3DProtocol Implementations](projectivetransform3d/transform3dprotocol-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Rotatable3D](rotatable3d.md)
- [Rotatable3DProtocol](rotatable3dprotocol.md)
- [Scalable3D](scalable3d.md)
- [Scalable3DProtocol](scalable3dprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Shearable3D](shearable3d.md)
- [Shearable3DProtocol](shearable3dprotocol.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
- [Transform3DProtocol](transform3dprotocol.md)
- [Translatable3D](translatable3d.md)
- [Translatable3DProtocol](translatable3dprotocol.md)

## See Also

- [struct AffineTransform3D](affinetransform3d.md)
  A 3D affine transformation matrix.
- [struct AffineTransform3DFloat](affinetransform3dfloat.md)
- [struct ProjectiveTransform3DFloat](projectivetransform3dfloat.md)
  A single-precision 3D projective transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d)*