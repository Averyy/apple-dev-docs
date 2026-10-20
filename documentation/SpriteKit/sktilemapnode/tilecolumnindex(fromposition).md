# tileColumnIndex(fromPosition:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

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
func tileColumnIndex(fromPosition position: CGPoint) -> Int
```

```objc
- (NSUInteger) tileColumnIndexFromPosition:(CGPoint) position;
```

#### Return Value

The tile map node object’s tile column index for the specified position.

## Parameters

- `position`: The position in the tile map to check.

## See Also

### Querying the Tile Map’s Properties
- [func centerOfTile(atColumn: Int, row: Int) -> CGPoint](./centeroftile%28atcolumn,row%29.md)
- [func tileDefinition(atColumn: Int, row: Int) -> SKTileDefinition?](./tiledefinition%28atcolumn,row%29.md)
- [func tileGroup(atColumn: Int, row: Int) -> SKTileGroup?](./tilegroup%28atcolumn,row%29.md)
- [func tileRowIndex(fromPosition: CGPoint) -> Int](./tilerowindex%28fromposition%29.md)
  Returns the tile map node object’s tile row index for the specified position in points.
- [var mapSize: CGSize](./mapsize.md)
  The overall size of the tile map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/tilecolumnindex(fromposition:))*