# tileWidth

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Sets the width of a tile for this render pass.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var tileWidth: Int { get }
```

```objc
@property (readonly) NSUInteger tileWidth;
```

## See Also

### Drawing with tile shaders
- [func dispatchThreadsPerTile(MTLSize)](./dispatchthreadspertile%28_%29.md)
  Encodes a command that invokes a tile shader function from the encoder’s current tile render pipeline state.
- [var tileHeight: Int](./tileheight.md)
  Sets the height of a tile for this render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/tilewidth)*