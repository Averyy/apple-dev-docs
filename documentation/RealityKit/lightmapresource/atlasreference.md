# LightmapResource.AtlasReference

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Specifies an area in a lightmap atlas to fetch data from.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct AtlasReference
```

## Topics

### Locating the atlas texture
- [var atlasTextureIndex: Int](./atlasreference/atlastextureindex.md)
  Index of the atlas within the LightmapResource.
- [var atlasTextureSlice: Int](./atlasreference/atlastextureslice.md)
  Index of the slice within the atlas.
### Mapping texture coordinates
- [var uvScale: SIMD2<Float>](./atlasreference/uvscale.md)
  A scale to apply to lightmap UV attribute before sampling from the slice of the atlas. Note that lightmap textures use the Metal convention: UV (0,0) corresponds to the top-left corner of the image, while UV (1,1) corresponds to the bottom-right.
- [var uvOffset: SIMD2<Float>](./atlasreference/uvoffset.md)
  An offset to apply to lightmap UV attribute before sampling from the slice of the atlas. Note that lightmap textures use the Metal convention: UV (0,0) corresponds to the top-left corner of the image, while UV (1,1) corresponds to the bottom-right.
### Initializers
- [init()](./atlasreference/init%28%29.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/atlasreference)*