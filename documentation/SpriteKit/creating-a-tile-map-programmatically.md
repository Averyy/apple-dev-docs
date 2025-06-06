# Creating a Tile Map Programmatically

**Framework**: SpriteKit

#### Overview

The collection of functions you use to create a tile map node programmatically.

> 💡 **Tip**:  You can create a tile map node much quicker by using Xcode’s SpriteKit Scene Editor.

 You can create a tile map node much quicker by using Xcode’s SpriteKit Scene Editor.

## Topics

### Creating a Tile Map
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize)](sktilemapnode/init(tileset:columns:rows:tilesize:).md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWith: SKTileGroup)](sktilemapnode/init(tileset:columns:rows:tilesize:fillwith:).md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, tileGroupLayout: [SKTileGroup])](sktilemapnode/init(tileset:columns:rows:tilesize:tilegrouplayout:).md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows. For a grid set type, the overall size, in points, of the node will be `numberOfColumns * tileSize.width` wide and `numberOfRows * tileSize.height` high.
- [class func tileMapNodes(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, from: GKNoiseMap, tileTypeNoiseMapThresholds: [NSNumber]) -> [SKTileMapNode]](sktilemapnode/tilemapnodes(tileset:columns:rows:tilesize:from:tiletypenoisemapthresholds:).md)
  Creates a tile map node by allowing a [`GKNoiseMap`](https://developer.apple.com/documentation/GameplayKit/GKNoiseMap) to choose its tiles.
### Defining a Tile Map’s Contents
- [var enableAutomapping: Bool](sktilemapnode/enableautomapping.md)
  When creating a tile map node programmatically, specifies whether the tile map uses automapping behavior like the scene editor.
- [func fill(with: SKTileGroup?)](sktilemapnode/fill(with:).md)
  When creating a tile map node programmatically, this function performs a fill operation with the specified tile group.
- [func setTileGroup(SKTileGroup, andTileDefinition: SKTileDefinition, forColumn: Int, row: Int)](sktilemapnode/settilegroup(_:andtiledefinition:forcolumn:row:).md)
  Set the tile group and tile definition at the specified tile index.
- [func setTileGroup(SKTileGroup?, forColumn: Int, row: Int)](sktilemapnode/settilegroup(_:forcolumn:row:).md)
  Set the tile group at the specified tile index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/creating-a-tile-map-programmatically)*