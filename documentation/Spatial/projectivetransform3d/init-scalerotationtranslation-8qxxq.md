# init(scale:rotation:translation:)

**Framework**: Spatial  
**Kind**: init

Creates a projective transform from the specified scale, rotate, and translate transforms.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(scale: Size3D = Size3D(width: 1.0, height: 1, depth: 1), rotation: Rotation3D = .zero, translation: Size3D)
```

## Parameters

- `scale`: A size structure that specifies the scale.
- `rotation`: A rotation structure that specifies the rotation.
- `translation`: A size structure that specifies the translation.

## See Also

- [var offset: Vector3D](projectivetransform3d/offset.md)
  The projective transform’s translation.
- [var scale: Size3D?](projectivetransform3d/scale.md)
  The projective transform’s scale.
- [func inverted() -> ProjectiveTransform3D?](projectivetransform3d/inverted.md)
  Returns a new transform that results from inverting an existing projective transform.
- [init(matrix: simd_float4x4)](projectivetransform3d/init(matrix:)-zfb.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:reversez:).md)
  Returns a projective transform with right-hand-side perspective and optional reverse-z.
- [init(translation: Size3D)](projectivetransform3d/init(translation:).md)
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/init(scale:rotation:translation:)-8qxxq)*