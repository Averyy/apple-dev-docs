# init(tileGroups:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a new tile set with an array of tile groups and rectangular grid layout.

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
init(tileGroups: [SKTileGroup])
```

```objc
- (instancetype) initWithTileGroups:(NSArray<SKTileGroup *> *) tileGroups;
```

#### Return Value

A new tile set.

## Parameters

- `tileGroups`: An array of [`SKTileGroup`](../sktilegroup.md) objects from which to create the tile set from.

## See Also

### Creating a Tile Set Programmatically
- [init(tileGroups: [SKTileGroup], tileSetType: SKTileSetType)](./init%28tilegroups,tilesettype%29.md)
  Initializes a new tile set with an array of tile groups and specified layout.
- [+ tileSetWithTileGroups:](./tilesetwithtilegroups_.md)
- [+ tileSetWithTileGroups:tileSetType:](./tilesetwithtilegroups_tilesettype_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktileset/init(tilegroups:))*