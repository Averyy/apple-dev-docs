# defaultTileGroup

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The tile set’s default tile group.

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
var defaultTileGroup: SKTileGroup? { get set }
```

```objc
@property (nonatomic, nullable) SKTileGroup * defaultTileGroup;
```

#### Discussion

With auto-mapping enabled, it is possible for some tiles to be removed because there is either no valid rule or a missing tile group for the required adjacency rule. In this situation, those tiles are replaced by the tile group specified by [`defaultTileGroup`](./defaulttilegroup.md).

## See Also

### Accessing or Reading a Tile Set’s Properties
- [var defaultTileSize: CGSize](./defaulttilesize.md)
  The tile set’s default tile size.
- [var name: String?](./name.md)
  A name associated with the tile set.
- [var tileGroups: [SKTileGroup]](./tilegroups.md)
  The tile set’s array of tile group objects.
- [var type: SKTileSetType](./type.md)
  The tile set’s type.
- [enum SKTileSetType](../sktilesettype.md)
  An enumeration defining how tiles are arranged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktileset/defaulttilegroup)*