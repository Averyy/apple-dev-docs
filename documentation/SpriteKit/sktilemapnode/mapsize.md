# mapSize

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

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
var mapSize: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize mapSize;
```

## Discussion

For a grid set type, the overall size, in points, of the node will be [`numberOfColumns`](./numberofcolumns.md) `*` [`tileSize`](./tilesize.md) `.` [`width`](../../CoreFoundation/cgsize/width.md) wide and [`numberOfRows`](../skwarpgeometrygrid/numberofrows.md) `*` [`tileSize`](./tilesize.md) `.` [`height`](../../CoreFoundation/cgsize/height.md) high.

## See Also

### Querying the Tile Map’s Properties
- [func centerOfTile(atColumn: Int, row: Int) -> CGPoint](./centeroftile%28atcolumn,row%29.md)
- [func tileColumnIndex(fromPosition: CGPoint) -> Int](./tilecolumnindex%28fromposition%29.md)
- [func tileDefinition(atColumn: Int, row: Int) -> SKTileDefinition?](./tiledefinition%28atcolumn,row%29.md)
- [func tileGroup(atColumn: Int, row: Int) -> SKTileGroup?](./tilegroup%28atcolumn,row%29.md)
- [func tileRowIndex(fromPosition: CGPoint) -> Int](./tilerowindex%28fromposition%29.md)
  Returns the tile map node object’s tile row index for the specified position in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/mapsize)*