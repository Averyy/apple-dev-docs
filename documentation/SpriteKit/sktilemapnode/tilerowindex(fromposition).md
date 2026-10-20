# tileRowIndex(fromPosition:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns the tile map node object’s tile row index for the specified position in points.

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
func tileRowIndex(fromPosition position: CGPoint) -> Int
```

```objc
- (NSUInteger) tileRowIndexFromPosition:(CGPoint) position;
```

#### Return Value

The tile map node object’s tile row index for the specified position.

## Parameters

- `position`: The position in the tile map to check.

## See Also

### Querying the Tile Map’s Properties
- [func centerOfTile(atColumn: Int, row: Int) -> CGPoint](./centeroftile%28atcolumn,row%29.md)
- [func tileColumnIndex(fromPosition: CGPoint) -> Int](./tilecolumnindex%28fromposition%29.md)
- [func tileDefinition(atColumn: Int, row: Int) -> SKTileDefinition?](./tiledefinition%28atcolumn,row%29.md)
- [func tileGroup(atColumn: Int, row: Int) -> SKTileGroup?](./tilegroup%28atcolumn,row%29.md)
- [var mapSize: CGSize](./mapsize.md)
  The overall size of the tile map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/tilerowindex(fromposition:))*