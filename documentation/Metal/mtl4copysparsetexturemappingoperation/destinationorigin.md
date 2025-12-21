# destinationOrigin

**Framework**: Metal  
**Kind**: property

The origin in the destination texture to copy into, in tiles.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var destinationOrigin: MTLOrigin
```

#### Discussion

The X, Y and Z coordinates of the tiles relative to the origin match the same coordinates in the source region.

When [`destinationLevel`](mtl4copysparsetexturemappingoperation/destinationlevel.md) is equal to the destination texture’s [`firstMipmapInTail`](mtltexture/firstmipmapintail.md), set `destinationOrigin.y` to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation/destinationorigin)*