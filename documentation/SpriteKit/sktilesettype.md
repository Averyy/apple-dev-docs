# SKTileSetType

**Framework**: SpriteKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration defining how tiles are arranged.

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
enum SKTileSetType
```

```c
enum SKTileSetType : NSUInteger;
```

## Topics

### Enumeration Cases
- [SKTileSetType.grid](./sktilesettype/grid.md)
- [SKTileSetType.hexagonalFlat](./sktilesettype/hexagonalflat.md)
- [SKTileSetType.hexagonalPointy](./sktilesettype/hexagonalpointy.md)
- [SKTileSetType.isometric](./sktilesettype/isometric.md)
### Initializers
- [init?(rawValue: UInt)](./sktilesettype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing or Reading a Tile Set’s Properties
- [var defaultTileGroup: SKTileGroup?](./sktileset/defaulttilegroup.md)
  The tile set’s default tile group.
- [var defaultTileSize: CGSize](./sktileset/defaulttilesize.md)
  The tile set’s default tile size.
- [var name: String?](./sktileset/name.md)
  A name associated with the tile set.
- [var tileGroups: [SKTileGroup]](./sktileset/tilegroups.md)
  The tile set’s array of tile group objects.
- [var type: SKTileSetType](./sktileset/type.md)
  The tile set’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilesettype)*