# imageblockSampleLength

**Framework**: Metal  
**Kind**: property

The per-sample size, in bytes, of the largest explicit imageblock layout in the render pass.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var imageblockSampleLength: Int { get set }
```

#### Discussion

If `imageBlockSampleLength` isn’t specified, Metal determines the imageblock sample length from the render pass attachment formats.  If any render pipelines bound to the encoder reference imageblocks with explicit layout, you need to set this property.

## See Also

- [var threadgroupMemoryLength: Int](mtlrenderpassdescriptor/threadgroupmemorylength.md)
  The per-tile size, in bytes, of the persistent threadgroup memory allocation.
- [var tileWidth: Int](mtlrenderpassdescriptor/tilewidth.md)
  The tile width, in pixels.
- [var tileHeight: Int](mtlrenderpassdescriptor/tileheight.md)
  The tile height, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/imageblocksamplelength)*