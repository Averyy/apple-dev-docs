# defaultTileSize

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The tile set’s default tile size.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var defaultTileSize: CGSize { get set }
```

```objc
@property (nonatomic) CGSize defaultTileSize;
```

#### Discussion

The default tile size an [`SKTileMapNode`](../sktilemapnode.md) will use for its tiles

## See Also

### Accessing or Reading a Tile Set’s Properties
- [var defaultTileGroup: SKTileGroup?](./defaulttilegroup.md)
  The tile set’s default tile group.
- [var name: String?](./name.md)
  A name associated with the tile set.
- [var tileGroups: [SKTileGroup]](./tilegroups.md)
  The tile set’s array of tile group objects.
- [var type: SKTileSetType](./type.md)
  The tile set’s type.
- [enum SKTileSetType](../sktilesettype.md)
  An enumeration defining how tiles are arranged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktileset/defaulttilesize)*