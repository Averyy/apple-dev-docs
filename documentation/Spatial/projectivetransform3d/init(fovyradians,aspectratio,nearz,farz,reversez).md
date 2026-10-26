# init(fovyRadians:aspectRatio:nearZ:farZ:reverseZ:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Returns a projective transform with right-hand-side perspective and optional reverse-z.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use `SPAngle` variant of `SPProjectiveTransform3DMakeWithRightHandPerspective`.

## Declaration

```swift
init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)
```

```c
static SPProjectiveTransform3D SPProjectiveTransform3DMakeWithRightHandPerspective(double fovyRadians, double aspectRatio, double nearZ, double farZ, bool reverseZ);
```

## Parameters

- `fovyRadians`: The field-of-view angle along the y-axis.
- `aspectRatio`: The aspect ratio.
- `nearZ`: The distance to the near clipping plane.
- `farZ`: The distance to the far clipping plane.
- `reverseZ`: A Boolean value that specifies whether the matrix uses reverse z.

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
- [init(scale: Size3D, rotation: Rotation3D, translation: Size3D)](./init%28scale,rotation,translation%29-8qxxq.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(translation: Size3D)](./init%28translation%29.md)
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](./init%28fovyradians,aspectratio,nearz,farz%29.md)
- [SPProjectiveTransform3DSetOffset](../spprojectivetransform3dsetoffset.md)
  Sets the translation of a projective transform.
- [SPProjectiveTransform3DMakeTranslation](../spprojectivetransform3dmaketranslation-5hc37.md)
  Creates a projective transform from the specified translate transform.
- [SPProjectiveTransform3DMakeWithRHPerspective](../spprojectivetransform3dmakewithrhperspective-97qwp.md)
  Returns a projective transform with right-hand side perspective.
- [SPProjectiveTransform3DTranslate](../spprojectivetransform3dtranslate-4tynj.md)
  Returns a transform with an origin that’s offset by the specified size.
- [SPProjectiveTransform3DGetTranslation](../spprojectivetransform3dgettranslation.md)
  The projective transform’s translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:reversez:))*