# SPAffineTransform3DMakeWithScaledPose

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a new affine transform structure from the specified scaled pose structure.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
static SPAffineTransform3D SPAffineTransform3DMakeWithScaledPose(SPScaledPose3D pose);
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
- [SPAffineTransform3DMakeShear](./spaffinetransform3dmakeshear.md)
  Creates an affine transform from the specified shear transform.
- [SPAffineTransform3DMakeWith4x4Matrix](./spaffinetransform3dmakewith4x4matrix.md)
  Creates an affine transform from the specified 4 x 4 double-precision matrix.
- [SPAffineTransform3DMakeWithPose](./spaffinetransform3dmakewithpose.md)
  Creates an affine transform from the specified pose structure.
- [SPAffineTransform3DMakeWithProjective](./spaffinetransform3dmakewithprojective.md)
  Creates an affine transform from the specified projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dmakewithscaledpose)*