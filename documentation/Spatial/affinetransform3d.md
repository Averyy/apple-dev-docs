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
- [init(rotation: Rotation3D)](affinetransform3d/init(rotation:).md)
  Creates an affine transform from the specified rotate transform.
- [init(scale: Size3D)](affinetransform3d/init(scale:).md)
  Creates an affine transform from the specified scale transform.
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](affinetransform3d/init(scale:rotation:translation:)-3somu.md)
  Creates an affine transform from the specified scale, rotate, and translate transforms.
- [init(scaledPose: ScaledPose3D)](affinetransform3d/init(scaledpose:).md)
  Creates an affine transform from the specified scale pose structure.
- [init(shear: AxisWithFactors)](affinetransform3d/init(shear:).md)
  Creates an affine transform from the specified shear transform.
- [init(translation: Vector3D)](affinetransform3d/init(translation:)-9czpj.md)
  Creates an affine transform from the specified translate transform.
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
- [func concatenating(AffineTransform3D) -> AffineTransform3D](affinetransform3d/concatenating(_:).md)
  Returns an affine transformation matrix that results from concatenating two existing affine transforms.
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
- [static let identity: AffineTransform3D](affinetransform3d/identity.md)
  The identity transform.
- [var rotation: Rotation3D?](affinetransform3d/rotation.md)
  The affine transform’s rotation.
- [var scale: Size3D](affinetransform3d/scale.md)
  The affine transform’s scale.
- [var translation: Vector3D](affinetransform3d/translation.md)
  The translation component of the affine transform.
### Checking characteristics
- [struct Dimension3DSet](dimension3dset.md)
  A set of dimensions.
- [var isIdentity: Bool](affinetransform3d/isidentity.md)
  A Boolean value that indicates whether the transform is the identity transform.
- [var isInvertible: Bool](affinetransform3d/isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.
- [var isRectilinear: Bool](affinetransform3d/isrectilinear.md)
  A Boolean value that indicates whether the transform is rectilinear.
- [var isTranslation: Bool](affinetransform3d/istranslation.md)
  A Boolean value that indicates whether the transform contains only a translation.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](affinetransform3d/isuniform(overdimensions:).md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [var isUniform: Bool](affinetransform3d/isuniform.md)
  A Boolean value that indicates whether the transform scales equally over all dimensions.
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
- [init(translation: Size3D)](affinetransform3d/init(translation:)-2fbl8.md)
- [func inverted() -> AffineTransform3D?](affinetransform3d/inverted.md)
  Returns a new transform that results from inverting an existing affine transform.
- [var offset: Vector3D](affinetransform3d/offset.md)
  The affine transform’s translation.
### Default Implementations
- [CustomReflectable Implementations](affinetransform3d/customreflectable-implementations.md)
- [Decodable Implementations](affinetransform3d/decodable-implementations.md)
- [Encodable Implementations](affinetransform3d/encodable-implementations.md)
- [Equatable Implementations](affinetransform3d/equatable-implementations.md)
- [Hashable Implementations](affinetransform3d/hashable-implementations.md)
- [Scalable3D Implementations](affinetransform3d/scalable3d-implementations.md)
- [Shearable3D Implementations](affinetransform3d/shearable3d-implementations.md)

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
- [Scalable3D](scalable3d.md)
- [Sendable](../Swift/Sendable.md)
- [Shearable3D](shearable3d.md)
- [Translatable3D](translatable3d.md)

## See Also

- [struct ProjectiveTransform3D](projectivetransform3d.md)
  A 3D projective transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d)*