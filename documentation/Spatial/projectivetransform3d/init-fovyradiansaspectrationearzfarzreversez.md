# init(fovyRadians:aspectRatio:nearZ:farZ:reverseZ:)

**Framework**: Spatial  
**Kind**: init

Returns a projective transform with right-hand-side perspective and optional reverse-z.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)
```

## Parameters

- `fovyRadians`: The field-of-view angle along the y-axis.
- `aspectRatio`: The aspect ratio.
- `nearZ`: The distance to the near clipping plane.
- `farZ`: The distance to the far clipping plane.
- `reverseZ`: A Boolean value that specifies whether the matrix uses reverse z.

## See Also

- [var offset: Vector3D](projectivetransform3d/offset.md)
  The projective transform’s translation.
- [var scale: Size3D?](projectivetransform3d/scale.md)
  The projective transform’s scale.
- [func inverted() -> ProjectiveTransform3D?](projectivetransform3d/inverted.md)
  Returns a new transform that results from inverting an existing projective transform.
- [init(matrix: simd_float4x4)](projectivetransform3d/init(matrix:)-zfb.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(scale: Size3D, rotation: Rotation3D, translation: Size3D)](projectivetransform3d/init(scale:rotation:translation:)-8qxxq.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(translation: Size3D)](projectivetransform3d/init(translation:)-4oiao.md)
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:reversez:))*