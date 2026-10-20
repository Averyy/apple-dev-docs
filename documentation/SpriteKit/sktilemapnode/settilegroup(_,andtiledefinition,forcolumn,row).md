# setTileGroup(_:andTileDefinition:forColumn:row:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Set the tile group and tile definition at the specified tile index.

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
func setTileGroup(_ tileGroup: SKTileGroup, andTileDefinition tileDefinition: SKTileDefinition, forColumn column: Int, row: Int)
```

```objc
- (void) setTileGroup:(SKTileGroup *) tileGroup andTileDefinition:(SKTileDefinition *) tileDefinition forColumn:(NSUInteger) column row:(NSUInteger) row;
```

#### Discussion

This function is for use when you’re creating a tile map programmatically, versus creating it ahead of time with the scene editor.

When [`enableAutomapping`](./enableautomapping.md) is set to `true`, the surrounding tiles of a painted area will be controlled by the tile group, too. When automapping is disabled, just the tile definition will be placed without modify any of the neighboring tiles.

## Parameters

- `tileGroup`: The tile group to place in the map.
- `tileDefinition`: The tile definition to place in the map.
- `column`: The column index of the tile.
- `row`: The row index of the tile.

## See Also

### Defining a Tile Map’s Contents
- [var enableAutomapping: Bool](./enableautomapping.md)
  When creating a tile map node programmatically, specifies whether the tile map uses automapping behavior like the scene editor.
- [func fill(with: SKTileGroup?)](./fill%28with%29.md)
  When creating a tile map node programmatically, this function performs a fill operation with the specified tile group.
- [func setTileGroup(SKTileGroup?, forColumn: Int, row: Int)](./settilegroup%28_,forcolumn,row%29.md)
  Set the tile group at the specified tile index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/settilegroup(_:andtiledefinition:forcolumn:row:))*