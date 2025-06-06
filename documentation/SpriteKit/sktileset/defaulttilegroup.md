# defaultTileGroup

**Framework**: SpriteKit  
**Kind**: property

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

#### Discussion

With auto-mapping enabled, it is possible for some tiles to be removed because there is either no valid rule or a missing tile group for the required adjacency rule. In this situation, those tiles are replaced by the tile group specified by [`defaultTileGroup`](sktileset/defaulttilegroup.md).

## See Also

- [var defaultTileSize: CGSize](sktileset/defaulttilesize.md)
  The tile set’s default tile size.
- [var name: String?](sktileset/name.md)
  A name associated with the tile set.
- [var tileGroups: [SKTileGroup]](sktileset/tilegroups.md)
  The tile set’s array of tile group objects.
- [var type: SKTileSetType](sktileset/type.md)
  The tile set’s type.
- [enum SKTileSetType](sktilesettype.md)
  An enumeration defining how tiles are arranged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktileset/defaulttilegroup)*