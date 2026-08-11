# uvScale

**Framework**: RealityKit  
**Kind**: property

A scale to apply to lightmap UV attribute before sampling from the slice of the atlas. Note that lightmap textures use the Metal convention: UV (0,0) corresponds to the top-left corner of the image, while UV (1,1) corresponds to the bottom-right.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var uvScale: SIMD2<Float>
```

## See Also

- [var uvOffset: SIMD2<Float>](lightmapresource/atlasreference/uvoffset.md)
  An offset to apply to lightmap UV attribute before sampling from the slice of the atlas. Note that lightmap textures use the Metal convention: UV (0,0) corresponds to the top-left corner of the image, while UV (1,1) corresponds to the bottom-right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/atlasreference/uvscale)*