# Creating a Tile Map Programmatically

**Framework**: SpriteKit  
**Role**: API Collection

#### Overview

The collection of functions you use to create a tile map node programmatically.

> 💡 **Tip**:  You can create a tile map node much quicker by using Xcode’s SpriteKit Scene Editor.

## Topics

### Creating a Tile Map
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize)](./sktilemapnode/init%28tileset,columns,rows,tilesize%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWith: SKTileGroup)](./sktilemapnode/init%28tileset,columns,rows,tilesize,fillwith%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, tileGroupLayout: [SKTileGroup])](./sktilemapnode/init%28tileset,columns,rows,tilesize,tilegrouplayout%29.md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows. For a grid set type, the overall size, in points, of the node will be `numberOfColumns * tileSize.width` wide and `numberOfRows * tileSize.height` high.
- [class func tileMapNodes(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, from: GKNoiseMap, tileTypeNoiseMapThresholds: [NSNumber]) -> [SKTileMapNode]](./sktilemapnode/tilemapnodes%28tileset,columns,rows,tilesize,from,tiletypenoisemapthresholds%29.md)
  Creates a tile map node by allowing a [`GKNoiseMap`](../GameplayKit/gknoisemap.md) to choose its tiles.
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:](./sktilemapnode/tilemapnodewithtileset_columns_rows_tilesize_.md)
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:fillWithTileGroup:](./sktilemapnode/tilemapnodewithtileset_columns_rows_tilesize_fillwithtilegroup_.md)
- [+ tileMapNodeWithTileSet:columns:rows:tileSize:tileGroupLayout:](./sktilemapnode/tilemapnodewithtileset_columns_rows_tilesize_tilegrouplayout_.md)
### Defining a Tile Map’s Contents
- [var enableAutomapping: Bool](./sktilemapnode/enableautomapping.md)
  When creating a tile map node programmatically, specifies whether the tile map uses automapping behavior like the scene editor.
- [func fill(with: SKTileGroup?)](./sktilemapnode/fill%28with%29.md)
  When creating a tile map node programmatically, this function performs a fill operation with the specified tile group.
- [func setTileGroup(SKTileGroup, andTileDefinition: SKTileDefinition, forColumn: Int, row: Int)](./sktilemapnode/settilegroup%28_,andtiledefinition,forcolumn,row%29.md)
  Set the tile group and tile definition at the specified tile index.
- [func setTileGroup(SKTileGroup?, forColumn: Int, row: Int)](./sktilemapnode/settilegroup%28_,forcolumn,row%29.md)
  Set the tile group at the specified tile index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/creating-a-tile-map-programmatically)*