# SPAffineTransform3DMakeShear

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Creates an affine transform from the specified shear transform.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPAffineTransform3D SPAffineTransform3DMakeShear(SPAxis shearAxis, double shearFactor0, double shearFactor1);
```

## See Also

### Creating a 3D affine transform structure
- [init(simd_double4x3)](./affinetransform3d/init%28_%29-722a2.md)
  Creates an affine transform from the specified 4 x 3 double-precision matrix.
- [init(truncating: ProjectiveTransform3D)](./affinetransform3d/init%28truncating%29-40nzj.md)
  Returns a new affine transform structure from the specified projective transform.
- [init(truncating: simd_double4x4)](./affinetransform3d/init%28truncating%29-9fd9g.md)
  Returns a new affine transform structure from the specified 4 x 4 matrix truncated to a  4 x 3 matrix.
- [SPAffineTransform3DMake](./spaffinetransform3dmake-3a37f.md)
- [SPAffineTransform3DMake](./spaffinetransform3dmake-94le1.md)
  Creates an affine transform from the specified scale, rotate, and translate transforms.
- [SPAffineTransform3DMakeWith4x4Matrix](./spaffinetransform3dmakewith4x4matrix.md)
  Creates an affine transform from the specified 4 x 4 double-precision matrix.
- [SPAffineTransform3DMakeWithPose](./spaffinetransform3dmakewithpose.md)
  Creates an affine transform from the specified pose structure.
- [SPAffineTransform3DMakeWithProjective](./spaffinetransform3dmakewithprojective.md)
  Creates an affine transform from the specified projective transform.
- [SPAffineTransform3DMakeWithScaledPose](./spaffinetransform3dmakewithscaledpose.md)
  Returns a new affine transform structure from the specified scaled pose structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dmakeshear)*