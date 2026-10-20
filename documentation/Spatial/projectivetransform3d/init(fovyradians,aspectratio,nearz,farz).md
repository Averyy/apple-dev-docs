# init(fovyRadians:aspectRatio:nearZ:farZ:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

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
init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)
```

```c
static SPProjectiveTransform3D SPProjectiveTransform3DMakeWithRightHandPerspective(double fovyRadians, double aspectRatio, double nearZ, double farZ);
```

#### Return Value

A projective transform with right-hand side perspective.

#### Discussion

Returns a projective transform with right-hand side perspective.

## Parameters

- `fovyRadians`: The field of view angle on the @p y axis.
- `aspectRatio`: The aspect ratio.
- `nearZ`: The near @p z .
- `farZ`: The far @p z .

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
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./init%28fovyradians,aspectratio,nearz,farz,reversez%29.md)
  Returns a projective transform with right-hand-side perspective and optional reverse-z.
- [init(translation: Size3D)](./init%28translation%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:))*