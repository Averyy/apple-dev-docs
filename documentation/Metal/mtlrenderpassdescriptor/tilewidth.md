# tileWidth

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) NSUInteger tileWidth;
```

#### Discussion

The valid tile sizes are `32 x 32`, `32 x 16`, and `16 x 16`. The Metal driver chooses a default size when your app doesn’t set a tile size.

## See Also

### Specifying tile shading parameters
- [var imageblockSampleLength: Int](./imageblocksamplelength.md)
  The per-sample size, in bytes, of the largest explicit imageblock layout in the render pass.
- [var threadgroupMemoryLength: Int](./threadgroupmemorylength.md)
  The per-tile size, in bytes, of the persistent threadgroup memory allocation.
- [var tileHeight: Int](./tileheight.md)
  The tile height, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/tilewidth)*