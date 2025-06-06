# offset

**Framework**: Spatial  
**Kind**: property

The affine transform’s translation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
var offset: Vector3D { get set }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/offset)*