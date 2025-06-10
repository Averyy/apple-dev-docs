# mapSize

**Framework**: SpriteKit  
**Kind**: property

The overall size of the tile map.

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
@MainActor
var mapSize: CGSize { get }
```

#### Discussion

For a grid set type, the overall size, in points, of the node will be [`numberOfColumns`](sktilemapnode/numberofcolumns.md) `*` [`tileSize`](sktilemapnode/tilesize.md) `.` [`width`](https://developer.apple.com/documentation/CoreFoundation/CGSize/width) wide and [`numberOfRows`](skwarpgeometrygrid/numberofrows.md) `*` [`tileSize`](sktilemapnode/tilesize.md) `.` [`height`](https://developer.apple.com/documentation/CoreFoundation/CGSize/height) high.

## See Also

- [func centerOfTile(atColumn: Int, row: Int) -> CGPoint](sktilemapnode/centeroftile(atcolumn:row:).md)
- [func tileColumnIndex(fromPosition: CGPoint) -> Int](sktilemapnode/tilecolumnindex(fromposition:).md)
- [func tileDefinition(atColumn: Int, row: Int) -> SKTileDefinition?](sktilemapnode/tiledefinition(atcolumn:row:).md)
- [func tileGroup(atColumn: Int, row: Int) -> SKTileGroup?](sktilemapnode/tilegroup(atcolumn:row:).md)
- [func tileRowIndex(fromPosition: CGPoint) -> Int](sktilemapnode/tilerowindex(fromposition:).md)
  Returns the tile map node object’s tile row index for the specified position in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/mapsize)*