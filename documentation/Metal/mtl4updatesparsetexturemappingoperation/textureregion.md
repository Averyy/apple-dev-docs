# textureRegion

**Framework**: Metal  
**Kind**: property

The region in the texture to update, in tiles.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var textureRegion: MTLRegion
```

#### Discussion

When [`textureLevel`](mtl4updatesparsetexturemappingoperation/texturelevel.md) is equal to the texture’s [`firstMipmapInTail`](mtltexture/firstmipmapintail.md), set `origin.y` to `0` and `size.height` to `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4updatesparsetexturemappingoperation/textureregion)*