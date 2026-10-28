# init(tileSet:columns:rows:tileSize:fillWith:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.

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
init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWith tileGroup: SKTileGroup)
```

```objc
- (instancetype) initWithTileSet:(SKTileSet *) tileSet columns:(NSUInteger) columns rows:(NSUInteger) rows tileSize:(CGSize) tileSize fillWithTileGroup:(SKTileGroup *) tileGroup;
```

## Return Value

A new tile map node.

## Discussion

For a grid set type, the overall size, in points, of the node will be `numberOfColumns` * `tileSize.width` wide and `numberOfRows` * `tileSize.height` high. This initializer fills each tile with a texture defined by the descriptors in the final `SKTileGroup` argument.

## Parameters

- `tileSet`: The tile set that is used to render the tiles.
- `columns`: The number of columns in the map.
- `rows`: The number of rows in the map.
- `tileSize`: The size of each tile in points.
- `tileGroup`: The tile group to fill the tile map with.

## See Also

### Creating a Tile Map
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize)](./init%28tileset,columns,rows,tilesize%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, tileGroupLayout: [SKTileGroup])](./init%28tileset,columns,rows,tilesize,tilegrouplayout%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows. For a grid set type, the overall size, in points, of the node will be `numberOfColumns * tileSize.width` wide and `numberOfRows * tileSize.height` high.
- [class func tileMapNodes(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, from: GKNoiseMap, tileTypeNoiseMapThresholds: [NSNumber]) -> [SKTileMapNode]](./tilemapnodes%28tileset,columns,rows,tilesize,from,tiletypenoisemapthresholds%29.md)
  Creates a tile map node by allowing a [`GKNoiseMap`](../../GameplayKit/gknoisemap.md) to choose its tiles.
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:](./tilemapnodewithtileset_columns_rows_tilesize_.md)
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:fillWithTileGroup:](./tilemapnodewithtileset_columns_rows_tilesize_fillwithtilegroup_.md)
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:tileGroupLayout:](./tilemapnodewithtileset_columns_rows_tilesize_tilegrouplayout_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/init(tileset:columns:rows:tilesize:fillwith:))*