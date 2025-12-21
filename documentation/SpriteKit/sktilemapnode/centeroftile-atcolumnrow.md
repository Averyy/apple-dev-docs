# centerOfTile(atColumn:row:)

**Framework**: SpriteKit  
**Kind**: method

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
func centerOfTile(atColumn column: Int, row: Int) -> CGPoint
```

#### Return Value

The coordinates in points of the center of the tile for a given column and row.

## Parameters

- `column`: The column index of the tile.
- `row`: The row index of the tile.

## See Also

- [func tileColumnIndex(fromPosition: CGPoint) -> Int](sktilemapnode/tilecolumnindex(fromposition:).md)
- [func tileDefinition(atColumn: Int, row: Int) -> SKTileDefinition?](sktilemapnode/tiledefinition(atcolumn:row:).md)
- [func tileGroup(atColumn: Int, row: Int) -> SKTileGroup?](sktilemapnode/tilegroup(atcolumn:row:).md)
- [func tileRowIndex(fromPosition: CGPoint) -> Int](sktilemapnode/tilerowindex(fromposition:).md)
  Returns the tile map node object’s tile row index for the specified position in points.
- [var mapSize: CGSize](sktilemapnode/mapsize.md)
  The overall size of the tile map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/centeroftile(atcolumn:row:))*