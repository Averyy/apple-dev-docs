# fill(with:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

When creating a tile map node programmatically, this function performs a fill operation with the specified tile group.

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
func fill(with tileGroup: SKTileGroup?)
```

```objc
- (void) fillWithTileGroup:(SKTileGroup *) tileGroup;
```

## Mentions

- [Creating Tile Groups Programmatically](../creating-tile-groups-programmatically.md)

#### Discussion

This function is for use when you’re creating a tile map programmatically, versus creating it ahead of time with the scene editor.

## Parameters

- `tileGroup`: The tile group that will be used to fill the map.

## See Also

### Defining a Tile Map’s Contents
- [var enableAutomapping: Bool](./enableautomapping.md)
  When creating a tile map node programmatically, specifies whether the tile map uses automapping behavior like the scene editor.
- [func setTileGroup(SKTileGroup, andTileDefinition: SKTileDefinition, forColumn: Int, row: Int)](./settilegroup%28_,andtiledefinition,forcolumn,row%29.md)
  Set the tile group and tile definition at the specified tile index.
- [func setTileGroup(SKTileGroup?, forColumn: Int, row: Int)](./settilegroup%28_,forcolumn,row%29.md)
  Set the tile group at the specified tile index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/fill(with:))*