# tileWidth

**Framework**: Metal  
**Kind**: property

The tile width, in pixels.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var tileWidth: Int { get set }
```

#### Discussion

The valid tile sizes are `32 x 32`, `32 x 16`, and `16 x 16`.  If you do not set a tile size, Metal device object chooses a default size.

## See Also

- [var imageblockSampleLength: Int](mtlrenderpassdescriptor/imageblocksamplelength.md)
  The per-sample size, in bytes, of the largest explicit imageblock layout in the render pass.
- [var threadgroupMemoryLength: Int](mtlrenderpassdescriptor/threadgroupmemorylength.md)
  The per-tile size, in bytes, of the persistent threadgroup memory allocation.
- [var tileHeight: Int](mtlrenderpassdescriptor/tileheight.md)
  The tile height, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/tilewidth)*