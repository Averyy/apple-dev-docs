# ProjectiveTransform3D

**Framework**: Spatial  
**Kind**: struct  
**Role**: Structure

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

```c
typedef struct { ... } SPProjectiveTransform3D;
```

## Topics

### Creating a 3D projective transform structure
- [init()](./projectivetransform3d/init%28%29-1clia.md)
  Creates a projective transform.
- [init()](./projectivetransform3d/init%28%29-6c4f4.md)
  Returns a new identity projective transform.
- [init(simd_float4x4)](./projectivetransform3d/init%28_%29-7b2bq.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(simd_double4x4)](./projectivetransform3d/init%28_%29-6g88l.md)
  Creates a projective transform from the specified double-precision matrix.
- [init(matrix: simd_double4x4)](./projectivetransform3d/init%28matrix%29-8eg5x.md)
  Creates a projective transform from the specified 4 x 4 double-precision matrix.
- [init(AffineTransform3D)](./projectivetransform3d/init%28_%29-9t2jh.md)
  Creates a projective transform from the specified affine transform.
- [init(pose: Pose3D)](./projectivetransform3d/init%28pose%29.md)
  Creates a projective transform from the specified pose structure.
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](./projectivetransform3d/init%28scale,rotation,translation%29-4h5wm.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(shear: AxisWithFactors)](./projectivetransform3d/init%28shear%29.md)
  Creates a projective transform from the specified shear transform.
- [init(leftTangent: Double, rightTangent: Double, topTangent: Double, bottomTangent: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./projectivetransform3d/init%28lefttangent,righttangent,toptangent,bottomtangent,nearz,farz,reversez%29.md)
  Returns a projective transform from tangents for each side of its frustum.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double)](./projectivetransform3d/init%28fovy,aspectratio,nearz,farz%29.md)
  Returns a projective transform with right-hand side perspective.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./projectivetransform3d/init%28fovy,aspectratio,nearz,farz,reversez%29.md)
- [init(scaledPose: ScaledPose3D)](./projectivetransform3d/init%28scaledpose%29.md)
- [SPProjectiveTransform3DMake](./spprojectivetransform3dmake-6aldt.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [SPProjectiveTransform3DMake](./spprojectivetransform3dmake-83q47.md)
- [SPProjectiveTransform3DMakeShear](./spprojectivetransform3dmakeshear.md)
  Creates an affine transform from the specified shear transform.
- [SPProjectiveTransform3DMakeWithPose](./spprojectivetransform3dmakewithpose.md)
  Creates a projective transform from the specified pose structure.
- [SPProjectiveTransform3DMakeWithScaledPose](./spprojectivetransform3dmakewithscaledpose.md)
  Returns a new projective transform structure from the specified scaled pose structure.
- [SPProjectiveTransform3DMakeWithRHPerspective](./spprojectivetransform3dmakewithrhperspective-97qwp.md)
  Returns a projective transform with right-hand side perspective.
- [SPProjectiveTransform3DMakeWithRHPerspective](./spprojectivetransform3dmakewithrhperspective-9gl97.md)
### Inspecting a 3D projective transform’s properties
- [var inverse: ProjectiveTransform3D?](./projectivetransform3d/inverse.md)
  The projective transform’s inverse.
- [var scaleComponent: Size3D](./projectivetransform3d/scalecomponent.md)
  The scale component of the projective transform.
- [var translation: Vector3D](./projectivetransform3d/translation.md)
  The translation component of the projective transform.
- [var matrix: simd_double4x4](./projectivetransform3d/matrix.md)
  The projective transform’s underlying matrix.
### Transforming a 3D projective transform structure
- [func sheared(AxisWithFactors) -> ProjectiveTransform3D](./projectivetransform3d/sheared%28_%29.md)
  Returns a projective transform that results from shearing over an axis by shear factors for the other two axes.
- [enum AxisWithFactors](./axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [struct Axis3D](./axis3d.md)
  Constants that describe an axis.
- [func flip(along: Axis3D)](./projectivetransform3d/flip%28along%29.md)
  Flips a projective transform along the specified axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3D](./projectivetransform3d/flipped%28along%29.md)
  Returns a projective transform that results from flipping it along the specified axis.
- [SPProjectiveTransform3DScaleBy](./spprojectivetransform3dscaleby.md)
  Returns a transform that results from scaling with the specified double-precision values.
- [SPProjectiveTransform3DShear](./spprojectivetransform3dshear.md)
  Returns a projective transform that results from shearing over an axis by shear factors for the other two axes.
- [SPProjectiveTransform3DFlip](./spprojectivetransform3dflip.md)
  Returns a projective transform that results from flipping it along the specified axis.
- [SPProjectiveTransform3DInverted](./spprojectivetransform3dinverted.md)
  Returns a new transform that results from inverting an existing projective transform.
- [SPProjectiveTransform3DSetTranslation](./spprojectivetransform3dsettranslation.md)
  Sets the translation of a projective transform.
- [SPProjectiveTransform3DRotate](./spprojectivetransform3drotate.md)
  Returns a transform that results from applying the specified rotation.
- [SPProjectiveTransform3DRotateByQuaternion](./spprojectivetransform3drotatebyquaternion.md)
  Returns a transform that results from rotating with the specified quaternion.
- [SPProjectiveTransform3DScaleBySize](./spprojectivetransform3dscalebysize.md)
  Returns a transform that results from scaling with the specified size structure.
- [SPProjectiveTransform3DScaleUniform](./spprojectivetransform3dscaleuniform.md)
  Returns a transform that results from uniformly scaling with the specified double-precision value.
- [SPProjectiveTransform3DTranslate](./spprojectivetransform3dtranslate-4tynj.md)
  Returns a transform with an origin that’s offset by the specified size.
- [SPProjectiveTransform3DTranslate](./spprojectivetransform3dtranslate-7ecid.md)
  Returns a transform with an origin that’s offset by the specified vector.
### Decomposing a 3D projective transform
- [var rotation: Rotation3D?](./projectivetransform3d/rotation.md)
  The projective transform’s rotation.
- [SPProjectiveTransform3DGetRotation](./spprojectivetransform3dgetrotation.md)
  The projective transform’s rotation.
- [SPProjectiveTransform3DGetScale](./spprojectivetransform3dgetscale.md)
  The projective transform’s scale.
- [SPProjectiveTransform3DGetOffset](./spprojectivetransform3dgetoffset.md)
  The projective transform’s translation.
### Checking characteristics
- [func is3DProjection() -> Bool](./projectivetransform3d/is3dprojection%28%29.md)
  Returns a Boolean value that indicates whether the transform is a 3D projection.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](./projectivetransform3d/isuniform%28overdimensions%29.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [var isAffine: Bool](./projectivetransform3d/isaffine.md)
  A Boolean value that indicates whether the transform is affine.
- [var isInvertible: Bool](./projectivetransform3d/isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.
- [SPProjectiveTransform3DIsUniformOverDimensions](./spprojectivetransform3disuniformoverdimensions.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [SPProjectiveTransform3DIsValid](./spprojectivetransform3disvalid.md)
  A Boolean value that indicates whether the transform is a valid transform.
- [SPProjectiveTransform3DInvalid](./spprojectivetransform3dinvalid.md)
  The null transform that represents an invalid value.
### Comparing values
- [func isApproximatelyEqual(to: ProjectiveTransform3D, tolerance: Double) -> Bool](./projectivetransform3d/isapproximatelyequal%28to,tolerance%29.md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
- [SPProjectiveTransform3DAlmostEqualToTransform](./spprojectivetransform3dalmostequaltotransform-5qqyc.md)
  Returns a Boolean value that indicates whether two transforms are equal within a default tolerance.
- [SPProjectiveTransform3DAlmostEqualToTransform](./spprojectivetransform3dalmostequaltotransform-33crc.md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
### Applying arithmetic operations
- [static func * (ProjectiveTransform3D, ProjectiveTransform3D) -> ProjectiveTransform3D](./projectivetransform3d/star%28_,_%29.md)
  Returns the concatenation of two projective transforms.
- [static func *= (inout ProjectiveTransform3D, ProjectiveTransform3D)](./projectivetransform3d/stareq%28_,_%29.md)
  Concatenates two projective transforms and stores the result in the left-hand-side variable.
### Deprecated symbols
- [var offset: Vector3D](./projectivetransform3d/offset.md)
  The projective transform’s translation.
- [var scale: Size3D?](./projectivetransform3d/scale.md)
  The projective transform’s scale.
- [func inverted() -> ProjectiveTransform3D?](./projectivetransform3d/inverted%28%29.md)
  Returns a new transform that results from inverting an existing projective transform.
- [init(matrix: simd_float4x4)](./projectivetransform3d/init%28matrix%29-zfb.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(scale: Size3D, rotation: Rotation3D, translation: Size3D)](./projectivetransform3d/init%28scale,rotation,translation%29-8qxxq.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./projectivetransform3d/init%28fovyradians,aspectratio,nearz,farz,reversez%29.md)
  Returns a projective transform with right-hand-side perspective and optional reverse-z.
- [init(translation: Size3D)](./projectivetransform3d/init%28translation%29.md)
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](./projectivetransform3d/init%28fovyradians,aspectratio,nearz,farz%29.md)
- [SPProjectiveTransform3DSetOffset](./spprojectivetransform3dsetoffset.md)
  Sets the translation of a projective transform.
- [SPProjectiveTransform3DMakeTranslation](./spprojectivetransform3dmaketranslation-5hc37.md)
  Creates a projective transform from the specified translate transform.
- [SPProjectiveTransform3DGetTranslation](./spprojectivetransform3dgettranslation.md)
  The projective transform’s translation.
### Initializers
- [init(ProjectiveTransform3DFloat)](./projectivetransform3d/init%28_%29-7nv9f.md)
  Returns a double-precision projective transformation from a single-precision projective transformation.
### Default Implementations
- [CustomReflectable Implementations](./projectivetransform3d/customreflectable-implementations.md)
- [Scalable3DProtocol Implementations](./projectivetransform3d/scalable3dprotocol-implementations.md)
- [Shearable3DProtocol Implementations](./projectivetransform3d/shearable3dprotocol-implementations.md)
- [Transform3DProtocol Implementations](./projectivetransform3d/transform3dprotocol-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Rotatable3D](./rotatable3d.md)
- [Rotatable3DProtocol](./rotatable3dprotocol.md)
- [Scalable3D](./scalable3d.md)
- [Scalable3DProtocol](./scalable3dprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Shearable3D](./shearable3d.md)
- [Shearable3DProtocol](./shearable3dprotocol.md)
- [SpatialTypeProtocol](./spatialtypeprotocol.md)
- [Transform3DProtocol](./transform3dprotocol.md)
- [Translatable3D](./translatable3d.md)
- [Translatable3DProtocol](./translatable3dprotocol.md)

## See Also

### Affine and projective transforms
- [struct AffineTransform3D](./affinetransform3d.md)
  A 3D affine transformation matrix.
- [struct AffineTransform3DFloat](./affinetransform3dfloat.md)
- [struct ProjectiveTransform3DFloat](./projectivetransform3dfloat.md)
  A single-precision 3D projective transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d)*