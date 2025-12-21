# sourceRegion

**Framework**: Metal  
**Kind**: property

The region in the source texture, in tiles.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var sourceRegion: MTLRegion
```

#### Discussion

The tiles remain mapped in the source texture.

When [`sourceLevel`](mtl4copysparsetexturemappingoperation/sourcelevel.md) is equal to the source texture’s [`firstMipmapInTail`](mtltexture/firstmipmapintail.md), set `origin.y` to `0` and `size.height` to `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation/sourceregion)*