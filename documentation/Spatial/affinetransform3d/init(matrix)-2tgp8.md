# init(matrix:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates an affine transform from the specified 4 x 4 double-precision matrix.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init?(matrix: simd_double4x4)
```

## Parameters

- `matrix`: The source double-precision matrix.

## See Also

### Deprecated symbols
- [init?(simd_float4x4)](./init%28_%29-41dx7.md)
  Creates an affine transform from the specified 4 x 4 single-precision matrix.
- [init?(simd_double4x4)](./init%28_%29-6bm4k.md)
  Creates an affine transform from the specified 4 x 4 double-precision matrix.
- [init(matrix: simd_float4x3)](./init%28matrix%29-6icxq.md)
  Creates an affine transform from the specified single-precision matrix.
- [init?(matrix: simd_float4x4)](./init%28matrix%29-82rxz.md)
  Creates an affine transform from the specified 4 x 4 single-precision matrix.
- [init?(projectiveTransform: ProjectiveTransform3D)](./init%28projectivetransform%29.md)
  Creates an affine transform from the specified projective transform.
- [init(scale: Size3D, rotation: Rotation3D, translation: Size3D)](./init%28scale,rotation,translation%29-40dow.md)
  Creates an affine transform from the specified scale, rotate, and translate transforms.
- [init(translation: Size3D)](./init%28translation%29.md)
- [func inverted() -> AffineTransform3D?](./inverted%28%29.md)
  Returns a new transform that results from inverting an existing affine transform.
- [var offset: Vector3D](./offset.md)
  The affine transform’s translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/init(matrix:)-2tgp8)*