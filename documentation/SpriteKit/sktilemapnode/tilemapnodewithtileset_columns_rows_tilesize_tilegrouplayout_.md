# tileMapNodeWithTileSet:columns:rows:tileSize:tileGroupLayout:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
+ (instancetype) tileMapNodeWithTileSet:(SKTileSet *) tileSet columns:(NSUInteger) columns rows:(NSUInteger) rows tileSize:(CGSize) tileSize tileGroupLayout:(NSArray<SKTileGroup *> *) tileGroupLayout;
```

## See Also

### Creating a Tile Map
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize)](./init%28tileset,columns,rows,tilesize%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWith: SKTileGroup)](./init%28tileset,columns,rows,tilesize,fillwith%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, tileGroupLayout: [SKTileGroup])](./init%28tileset,columns,rows,tilesize,tilegrouplayout%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows. For a grid set type, the overall size, in points, of the node will be `numberOfColumns * tileSize.width` wide and `numberOfRows * tileSize.height` high.
- [class func tileMapNodes(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, from: GKNoiseMap, tileTypeNoiseMapThresholds: [NSNumber]) -> [SKTileMapNode]](./tilemapnodes%28tileset,columns,rows,tilesize,from,tiletypenoisemapthresholds%29.md)
  Creates a tile map node by allowing a [`GKNoiseMap`](../../GameplayKit/gknoisemap.md) to choose its tiles.
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:](./tilemapnodewithtileset_columns_rows_tilesize_.md)
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:fillWithTileGroup:](./tilemapnodewithtileset_columns_rows_tilesize_fillwithtilegroup_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/tilemapnodewithtileset:columns:rows:tilesize:tilegrouplayout:)*