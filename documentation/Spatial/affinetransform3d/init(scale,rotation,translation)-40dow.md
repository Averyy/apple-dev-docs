# init(scale:rotation:translation:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates an affine transform from the specified scale, rotate, and translate transforms.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Use `Vector3D` variant.

## Declaration

```swift
init(scale: Size3D = Size3D(width: 1.0, height: 1, depth: 1), rotation: Rotation3D = .zero, translation: Size3D)
```

## Parameters

- `scale`: A size structure that specifies the scale.
- `rotation`: A rotation structure that specifies the rotation.
- `translation`: A size structure that specifies the translation.

## See Also

### Deprecated symbols
- [init?(simd_float4x4)](./init%28_%29-41dx7.md)
  Creates an affine transform from the specified 4 x 4 single-precision matrix.
- [init?(simd_double4x4)](./init%28_%29-6bm4k.md)
  Creates an affine transform from the specified 4 x 4 double-precision matrix.
- [init?(matrix: simd_double4x4)](./init%28matrix%29-2tgp8.md)
  Creates an affine transform from the specified 4 x 4 double-precision matrix.
- [init(matrix: simd_float4x3)](./init%28matrix%29-6icxq.md)
  Creates an affine transform from the specified single-precision matrix.
- [init?(matrix: simd_float4x4)](./init%28matrix%29-82rxz.md)
  Creates an affine transform from the specified 4 x 4 single-precision matrix.
- [init?(projectiveTransform: ProjectiveTransform3D)](./init%28projectivetransform%29.md)
  Creates an affine transform from the specified projective transform.
- [init(translation: Size3D)](./init%28translation%29.md)
- [func inverted() -> AffineTransform3D?](./inverted%28%29.md)
  Returns a new transform that results from inverting an existing affine transform.
- [var offset: Vector3D](./offset.md)
  The affine transform’s translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/init(scale:rotation:translation:)-40dow)*