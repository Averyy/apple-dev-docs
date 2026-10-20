# scale

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

The projective transform’s scale.

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
var scale: Size3D? { get }
```

## See Also

### Deprecated symbols
- [var offset: Vector3D](./offset.md)
  The projective transform’s translation.
- [func inverted() -> ProjectiveTransform3D?](./inverted%28%29.md)
  Returns a new transform that results from inverting an existing projective transform.
- [init(matrix: simd_float4x4)](./init%28matrix%29-zfb.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(scale: Size3D, rotation: Rotation3D, translation: Size3D)](./init%28scale,rotation,translation%29-8qxxq.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./init%28fovyradians,aspectratio,nearz,farz,reversez%29.md)
  Returns a projective transform with right-hand-side perspective and optional reverse-z.
- [init(translation: Size3D)](./init%28translation%29.md)
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](./init%28fovyradians,aspectratio,nearz,farz%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/scale)*