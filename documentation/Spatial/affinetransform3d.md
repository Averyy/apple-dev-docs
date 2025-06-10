# AffineTransform3D

**Framework**: Spatial  
**Kind**: struct

A 3D affine transformation matrix.

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
struct AffineTransform3D
```

## Topics

### Creating a 3D affine transform structure
- [init()](affinetransform3d/init-2uqjl.md)
  Creates an affine transform.
- [init()](affinetransform3d/init-6ntm3.md)
  Returns a new identity affine transform.
- [init(simd_float4x3)](affinetransform3d/init(_:)-52vpb.md)
  Creates an affine transform from the specified single-precision matrix.
- [init(simd_double4x3)](affinetransform3d/init(_:)-722a2.md)
  Creates an affine transform from the specified 4 x 3 double-precision matrix.
- [init(Transform)](affinetransform3d/init(_:)-e2xx.md)
  Creates an affine transform from the specified transform.
- [init(matrix: simd_double4x3)](affinetransform3d/init(matrix:)-2inci.md)
  Creates an affine transform from the specified double-precision matrix.
- [init(pose: Pose3D)](affinetransform3d/init(pose:).md)
  Creates an affine transform from the specified pose structure.
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](affinetransform3d/init(scale:rotation:translation:)-3somu.md)
  Creates an affine transform from the specified scale, rotate, and translate transforms.
- [init(scaledPose: ScaledPose3D)](affinetransform3d/init(scaledpose:).md)
  Creates an affine transform from the specified scale pose structure.
- [init(shear: AxisWithFactors)](affinetransform3d/init(shear:).md)
  Creates an affine transform from the specified shear transform.
- [init(truncating: ProjectiveTransform3D)](affinetransform3d/init(truncating:)-40nzj.md)
  Returns a new affine transform structure from the specified projective transform.
- [init(truncating: simd_float4x4)](affinetransform3d/init(truncating:)-5wjxy.md)
  Returns a new affine transform structure from the specified single-precision 4 x 4 matrix truncated to a  4 x 3 matrix.
- [init(truncating: simd_double4x4)](affinetransform3d/init(truncating:)-9fd9g.md)
  Returns a new affine transform structure from the specified 4 x 4 matrix truncated to a  4 x 3 matrix.
### Transforming a 3D affine transform structure
- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
- [enum AxisWithFactors](axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [func changeBasis(from: AffineTransform3D, to: AffineTransform3D) -> AffineTransform3D?](affinetransform3d/changebasis(from:to:).md)
  Returns a new affine transform structure by applying a change-of-basis.
- [func flip(along: Axis3D)](affinetransform3d/flip(along:).md)
  Flips an affine transform along the specified axis.
- [func flipped(along: Axis3D) -> AffineTransform3D](affinetransform3d/flipped(along:).md)
  Returns an affine transform that results from flipping it along the specified axis.
- [var inverse: AffineTransform3D?](affinetransform3d/inverse.md)
  The affine transform’s inverse.
- [func scaledBy(x: Double, y: Double, z: Double) -> AffineTransform3D](affinetransform3d/scaledby(x:y:z:).md)
  Returns a transform that results from scaling with specified double-precision values.
- [func sheared(AxisWithFactors) -> AffineTransform3D](affinetransform3d/sheared(_:).md)
  Returns an affine transform that results from shearing over an axis by shear factors for the other two axes.
### Decomposing a 3D affine transform
- [var rotation: Rotation3D?](affinetransform3d/rotation.md)
  The affine transform’s rotation.
- [var scale: Size3D](affinetransform3d/scale.md)
  The affine transform’s scale.
- [var translation: Vector3D](affinetransform3d/translation.md)
  The translation component of the affine transform.
### Checking characteristics
- [struct Dimension3DSet](dimension3dset.md)
  A set of dimensions.
- [var isInvertible: Bool](affinetransform3d/isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](affinetransform3d/isuniform(overdimensions:).md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [var matrix: simd_double4x3](affinetransform3d/matrix.md)
  The affine transform’s underlying matrix.
- [var matrix3x3: simd_double3x3](affinetransform3d/matrix3x3.md)
  The first three columns of an affine transform’s underlying matrix.
- [var matrix4x4: simd_double4x4](affinetransform3d/matrix4x4.md)
  A 4 x 4 matrix that results from constructing the affine transform’s underlying matrix.
### Comparing values
- [static func == (AffineTransform3D, AffineTransform3D) -> Bool](affinetransform3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
- [func isApproximatelyEqual(to: AffineTransform3D, tolerance: Double) -> Bool](affinetransform3d/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
### Applying arithmetic operations
- [static func * (AffineTransform3D, AffineTransform3D) -> AffineTransform3D](affinetransform3d/*(_:_:).md)
  Returns the concatenation of two affine transforms.
- [static func *= (inout AffineTransform3D, AffineTransform3D)](affinetransform3d/*=(_:_:).md)
  Concatenates two affine transforms and stores the result in the left-hand-side variable.
### Deprecated symbols
- [init?(simd_float4x4)](affinetransform3d/init(_:)-41dx7.md)
  Creates an affine transform from the specified 4 x 4 single-precision matrix.
- [init?(simd_double4x4)](affinetransform3d/init(_:)-6bm4k.md)
  Creates an affine transform from the specified 4 x 4 double-precision matrix.
- [init?(matrix: simd_double4x4)](affinetransform3d/init(matrix:)-2tgp8.md)
  Creates an affine transform from the specified 4 x 4 double-precision matrix.
- [init(matrix: simd_float4x3)](affinetransform3d/init(matrix:)-6icxq.md)
  Creates an affine transform from the specified single-precision matrix.
- [init?(matrix: simd_float4x4)](affinetransform3d/init(matrix:)-82rxz.md)
  Creates an affine transform from the specified 4 x 4 single-precision matrix.
- [init?(projectiveTransform: ProjectiveTransform3D)](affinetransform3d/init(projectivetransform:).md)
  Creates an affine transform from the specified projective transform.
- [init(scale: Size3D, rotation: Rotation3D, translation: Size3D)](affinetransform3d/init(scale:rotation:translation:)-40dow.md)
  Creates an affine transform from the specified scale, rotate, and translate transforms.
- [init(translation: Size3D)](affinetransform3d/init(translation:).md)
- [func inverted() -> AffineTransform3D?](affinetransform3d/inverted.md)
  Returns a new transform that results from inverting an existing affine transform.
- [var offset: Vector3D](affinetransform3d/offset.md)
  The affine transform’s translation.
### Initializers
- [init(AffineTransform3DFloat)](affinetransform3d/init(_:)-7eksa.md)
  Returns a double-precision affine transformation from a single-precision affine transformation.
### Instance Properties
- [var columns: (Vector3D, Vector3D, Vector3D, Vector3D)](affinetransform3d/columns.md)
  The columns of the underlying matrix.
### Default Implementations
- [CustomReflectable Implementations](affinetransform3d/customreflectable-implementations.md)
- [Decodable Implementations](affinetransform3d/decodable-implementations.md)
- [Encodable Implementations](affinetransform3d/encodable-implementations.md)
- [Equatable Implementations](affinetransform3d/equatable-implementations.md)
- [Hashable Implementations](affinetransform3d/hashable-implementations.md)
- [Scalable3DProtocol Implementations](affinetransform3d/scalable3dprotocol-implementations.md)
- [Shearable3DProtocol Implementations](affinetransform3d/shearable3dprotocol-implementations.md)
- [Transform3DProtocol Implementations](affinetransform3d/transform3dprotocol-implementations.md)

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

- [struct AffineTransform3DFloat](affinetransform3dfloat.md)
- [struct ProjectiveTransform3D](projectivetransform3d.md)
  A 3D projective transformation matrix.
- [struct ProjectiveTransform3DFloat](projectivetransform3dfloat.md)
  A single-precision 3D projective transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d)*