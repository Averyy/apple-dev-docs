# init(truncating:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Returns a new affine transform structure from the specified projective transform.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(truncating transform: ProjectiveTransform3D)
```

```c
static SPAffineTransform3D SPAffineTransform3DMakeWithTruncatedProjective(SPProjectiveTransform3D transform);
```

## See Also

### Creating a 3D affine transform structure
- [init()](./init%28%29-2uqjl.md)
  Creates an affine transform.
- [init()](./init%28%29-6ntm3.md)
  Returns a new identity affine transform.
- [init(simd_float4x3)](./init%28_%29-52vpb.md)
  Creates an affine transform from the specified single-precision matrix.
- [init(simd_double4x3)](./init%28_%29-722a2.md)
  Creates an affine transform from the specified 4 x 3 double-precision matrix.
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
- [init(truncating: simd_float4x4)](./init%28truncating%29-5wjxy.md)
  Returns a new affine transform structure from the specified single-precision 4 x 4 matrix truncated to a  4 x 3 matrix.
- [init(truncating: simd_double4x4)](./init%28truncating%29-9fd9g.md)
  Returns a new affine transform structure from the specified 4 x 4 matrix truncated to a  4 x 3 matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/init(truncating:)-40nzj)*