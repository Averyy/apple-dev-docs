# inverted()

**Framework**: Spatial  
**Kind**: method

Returns a new transform that results from inverting an existing projective transform.

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
func inverted() -> ProjectiveTransform3D?
```

#### Return Value

The transform that results from inverting an existing projective transform. The method returns `nil` if the underlying matrix isn’t invertible.

## See Also

- [var offset: Vector3D](projectivetransform3d/offset.md)
  The projective transform’s translation.
- [var scale: Size3D?](projectivetransform3d/scale.md)
  The projective transform’s scale.
- [init(matrix: simd_float4x4)](projectivetransform3d/init(matrix:)-zfb.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(scale: Size3D, rotation: Rotation3D, translation: Size3D)](projectivetransform3d/init(scale:rotation:translation:)-8qxxq.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:reversez:).md)
  Returns a projective transform with right-hand-side perspective and optional reverse-z.
- [init(translation: Size3D)](projectivetransform3d/init(translation:).md)
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](projectivetransform3d/init(fovyradians:aspectratio:nearz:farz:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/inverted())*