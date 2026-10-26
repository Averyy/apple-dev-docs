# tileMapNodes(tileSet:columns:rows:tileSize:from:tileTypeNoiseMapThresholds:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates a tile map node by allowing a [`GKNoiseMap`](../../GameplayKit/gknoisemap.md) to choose its tiles.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
class func tileMapNodes(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, from noiseMap: GKNoiseMap, tileTypeNoiseMapThresholds thresholds: [NSNumber]) -> [SKTileMapNode]
```

```objc
+ (NSArray<SKTileMapNode *> *) tileMapNodesWithTileSet:(SKTileSet *) tileSet columns:(NSUInteger) columns rows:(NSUInteger) rows tileSize:(CGSize) tileSize fromNoiseMap:(GKNoiseMap *) noiseMap tileTypeNoiseMapThresholds:(NSArray<NSNumber *> *) thresholds;
```

## See Also

### Creating a Tile Map
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize)](./init%28tileset,columns,rows,tilesize%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWith: SKTileGroup)](./init%28tileset,columns,rows,tilesize,fillwith%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, tileGroupLayout: [SKTileGroup])](./init%28tileset,columns,rows,tilesize,tilegrouplayout%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows. For a grid set type, the overall size, in points, of the node will be `numberOfColumns * tileSize.width` wide and `numberOfRows * tileSize.height` high.
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:](./tilemapnodewithtileset_columns_rows_tilesize_.md)
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:fillWithTileGroup:](./tilemapnodewithtileset_columns_rows_tilesize_fillwithtilegroup_.md)
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:tileGroupLayout:](./tilemapnodewithtileset_columns_rows_tilesize_tilegrouplayout_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/tilemapnodes(tileset:columns:rows:tilesize:from:tiletypenoisemapthresholds:))*