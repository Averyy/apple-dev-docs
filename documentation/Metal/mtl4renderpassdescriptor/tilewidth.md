# tileWidth

**Framework**: Metal  
**Kind**: property

The width of the tiles, in pixels, a render pass you create with this descriptor applies to its attachments.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var tileWidth: Int { get set }
```

#### Discussion

For tile-based rendering, Metal divides each render attachment into smaller regions, or . The property’s default is `0`, which tells Metal to select a size that fits in tile memory.

See [`Tailor your apps for Apple GPUs and tile-based deferred rendering`](tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering.md) for more information about tiles, tile memory, and deferred rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/tilewidth)*