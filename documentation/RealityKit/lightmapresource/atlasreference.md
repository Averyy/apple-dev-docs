# LightmapResource.AtlasReference

**Framework**: RealityKit  
**Kind**: struct

Specifies an area in a lightmap atlas to fetch data from.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct AtlasReference
```

## Topics

### Locating the atlas texture
- [var atlasTextureIndex: Int](lightmapresource/atlasreference/atlastextureindex.md)
  Index of the atlas within the LightmapResource.
- [var atlasTextureSlice: Int](lightmapresource/atlasreference/atlastextureslice.md)
  Index of the slice within the atlas.
### Mapping texture coordinates
- [var uvScale: SIMD2<Float>](lightmapresource/atlasreference/uvscale.md)
  A scale to apply to lightmap UV attribute before sampling from the slice of the atlas.
- [var uvOffset: SIMD2<Float>](lightmapresource/atlasreference/uvoffset.md)
  An offset to apply to lightmap UV attribute before sampling from the slice of the atlas.
### Initializers
- [init()](lightmapresource/atlasreference/init.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var entityCount: Int](lightmapresource/entitycount.md)
  Total number of entities in this lightmap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/atlasreference)*