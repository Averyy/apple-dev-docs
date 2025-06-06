# fill(with:)

**Framework**: SpriteKit  
**Kind**: method

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

## Mentions

- [Creating Tile Groups Programmatically](creating-tile-groups-programmatically.md)

#### Discussion

This function is for use when you’re creating a tile map programmatically, versus creating it ahead of time with the scene editor.

## Parameters

- `tileGroup`: The tile group that will be used to fill the map.

## See Also

- [var enableAutomapping: Bool](sktilemapnode/enableautomapping.md)
  When creating a tile map node programmatically, specifies whether the tile map uses automapping behavior like the scene editor.
- [func setTileGroup(SKTileGroup, andTileDefinition: SKTileDefinition, forColumn: Int, row: Int)](sktilemapnode/settilegroup(_:andtiledefinition:forcolumn:row:).md)
  Set the tile group and tile definition at the specified tile index.
- [func setTileGroup(SKTileGroup?, forColumn: Int, row: Int)](sktilemapnode/settilegroup(_:forcolumn:row:).md)
  Set the tile group at the specified tile index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/fill(with:))*