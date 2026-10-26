# init(_:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates an affine transform from the specified 4 x 3 double-precision matrix.

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
init(_ matrix: simd_double4x3)
```

```c
static SPAffineTransform3D SPAffineTransform3DMakeWith4x3Matrix(simd_double4x3 matrix);
```

## Parameters

- `matrix`: The source single-precision matrix.

## See Also

### Creating a 3D affine transform structure
- [init()](./init%28%29-2uqjl.md)
  Creates an affine transform.
- [init()](./init%28%29-6ntm3.md)
  Returns a new identity affine transform.
- [init(simd_float4x3)](./init%28_%29-52vpb.md)
  Creates an affine transform from the specified single-precision matrix.
- [init(Transform)](./init%28_%29-e2xx.md)
  Creates an affine transform from the specified transform.
- [init(matrix: simd_double4x3)](./init%28matrix%29-2inci.md)
  Creates an affine transform from the specified double-precision matrix.
- [init(pose: Pose3D)](./init%28pose%29.md)
  Creates an affine transform from the specified pose structure.
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](./init%28scale,rotation,translation%29-3somu.md)
  Creates an affine transform from the specified scale, rotate, and translate transforms.
- [init(scaledPose: ScaledPose3D)](./init%28scaledpose%29.md)
  Creates an affine transform from the specified scale pose structure.
- [init(shear: AxisWithFactors)](./init%28shear%29.md)
  Creates an affine transform from the specified shear transform.
- [init(truncating: ProjectiveTransform3D)](./init%28truncating%29-40nzj.md)
  Returns a new affine transform structure from the specified projective transform.
- [init(truncating: simd_float4x4)](./init%28truncating%29-5wjxy.md)
  Returns a new affine transform structure from the specified single-precision 4 x 4 matrix truncated to a  4 x 3 matrix.
- [init(truncating: simd_double4x4)](./init%28truncating%29-9fd9g.md)
  Returns a new affine transform structure from the specified 4 x 4 matrix truncated to a  4 x 3 matrix.
- [SPAffineTransform3DMake](../spaffinetransform3dmake-3a37f.md)
- [SPAffineTransform3DMake](../spaffinetransform3dmake-94le1.md)
  Creates an affine transform from the specified scale, rotate, and translate transforms.
- [SPAffineTransform3DMakeShear](../spaffinetransform3dmakeshear.md)
  Creates an affine transform from the specified shear transform.
- [SPAffineTransform3DMakeWith4x4Matrix](../spaffinetransform3dmakewith4x4matrix.md)
  Creates an affine transform from the specified 4 x 4 double-precision matrix.
- [SPAffineTransform3DMakeWithPose](../spaffinetransform3dmakewithpose.md)
  Creates an affine transform from the specified pose structure.
- [SPAffineTransform3DMakeWithProjective](../spaffinetransform3dmakewithprojective.md)
  Creates an affine transform from the specified projective transform.
- [SPAffineTransform3DMakeWithScaledPose](../spaffinetransform3dmakewithscaledpose.md)
  Returns a new affine transform structure from the specified scaled pose structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/init(_:)-722a2)*