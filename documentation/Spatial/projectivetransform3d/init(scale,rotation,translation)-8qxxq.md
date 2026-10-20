# init(scale:rotation:translation:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a projective transform from the specified scale, rotate, and translate transforms.

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
- [var offset: Vector3D](./offset.md)
  The projective transform’s translation.
- [var scale: Size3D?](./scale.md)
  The projective transform’s scale.
- [func inverted() -> ProjectiveTransform3D?](./inverted%28%29.md)
  Returns a new transform that results from inverting an existing projective transform.
- [init(matrix: simd_float4x4)](./init%28matrix%29-zfb.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./init%28fovyradians,aspectratio,nearz,farz,reversez%29.md)
  Returns a projective transform with right-hand-side perspective and optional reverse-z.
- [init(translation: Size3D)](./init%28translation%29.md)
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](./init%28fovyradians,aspectratio,nearz,farz%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/init(scale:rotation:translation:)-8qxxq)*