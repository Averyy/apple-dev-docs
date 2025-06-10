# init(truncating:)

**Framework**: Spatial  
**Kind**: init

Returns a new affine transform structure from the specified 4 x 4 matrix truncated to a  4 x 3 matrix.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(truncating matrix: simd_double4x4)
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/init(truncating:)-9fd9g)*