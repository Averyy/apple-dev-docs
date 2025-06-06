# tileHeight

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The height of the tiles, in pixels, for the render command encoder.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var tileHeight: Int { get }
```

#### Discussion

The value comes from the [`tileHeight`](mtlrenderpassdescriptor/tileheight.md) property of the [`MTLRenderPassDescriptor`](mtlrenderpassdescriptor.md) at the time you create the render command encoder.

## See Also

- [func dispatchThreadsPerTile(MTLSize)](mtlrendercommandencoder/dispatchthreadspertile(_:).md)
  Encodes a command that invokes GPU functions from the encoder’s current tile render pipeline state.
- [var tileWidth: Int](mtlrendercommandencoder/tilewidth.md)
  The width of the tiles, in pixels, for the render command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/tileheight)*