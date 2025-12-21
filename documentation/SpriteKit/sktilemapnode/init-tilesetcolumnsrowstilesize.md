# init(tileSet:columns:rows:tileSize:)

**Framework**: SpriteKit  
**Kind**: init

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
init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize)
```

#### Return Value

A new tile map node.

#### Discussion

Creates an empty tile map.

For a grid set type, the overall size in points of the node will be `numberOfColumns` * `tileSize.width` wide and `numberOfRows` * `tileSize.height` high.

## Parameters

- `tileSet`: The tile set that is used to render the tiles
- `columns`: The number of columns in the map
- `rows`: The number of rows in the map
- `tileSize`: The size of each tile in points

## See Also

- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWith: SKTileGroup)](sktilemapnode/init(tileset:columns:rows:tilesize:fillwith:).md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, tileGroupLayout: [SKTileGroup])](sktilemapnode/init(tileset:columns:rows:tilesize:tilegrouplayout:).md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows. For a grid set type, the overall size, in points, of the node will be `numberOfColumns * tileSize.width` wide and `numberOfRows * tileSize.height` high.
- [class func tileMapNodes(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, from: GKNoiseMap, tileTypeNoiseMapThresholds: [NSNumber]) -> [SKTileMapNode]](sktilemapnode/tilemapnodes(tileset:columns:rows:tilesize:from:tiletypenoisemapthresholds:).md)
  Creates a tile map node by allowing a [`GKNoiseMap`](https://developer.apple.com/documentation/GameplayKit/GKNoiseMap) to choose its tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/init(tileset:columns:rows:tilesize:))*