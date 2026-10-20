# init(matrix:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a projective transform from the specified 4 x 4 single-precision matrix.

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
init(matrix: simd_float4x4)
```

## Parameters

- `matrix`: The source single-precision matrix.

## See Also

### Deprecated symbols
- [var offset: Vector3D](./offset.md)
  The projective transform’s translation.
- [var scale: Size3D?](./scale.md)
  The projective transform’s scale.
- [func inverted() -> ProjectiveTransform3D?](./inverted%28%29.md)
  Returns a new transform that results from inverting an existing projective transform.
- [init(scale: Size3D, rotation: Rotation3D, translation: Size3D)](./init%28scale,rotation,translation%29-8qxxq.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./init%28fovyradians,aspectratio,nearz,farz,reversez%29.md)
  Returns a projective transform with right-hand-side perspective and optional reverse-z.
- [init(translation: Size3D)](./init%28translation%29.md)
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](./init%28fovyradians,aspectratio,nearz,farz%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/init(matrix:)-zfb)*