# tileMapNodes(tileSet:columns:rows:tileSize:from:tileTypeNoiseMapThresholds:)

**Framework**: SpriteKit  
**Kind**: method

Creates a tile map node by allowing a [`GKNoiseMap`](https://developer.apple.com/documentation/GameplayKit/GKNoiseMap) to choose its tiles.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
class func tileMapNodes(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, from noiseMap: GKNoiseMap, tileTypeNoiseMapThresholds thresholds: [NSNumber]) -> [SKTileMapNode]
```

## See Also

- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize)](sktilemapnode/init(tileset:columns:rows:tilesize:).md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWith: SKTileGroup)](sktilemapnode/init(tileset:columns:rows:tilesize:fillwith:).md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows.
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, tileGroupLayout: [SKTileGroup])](sktilemapnode/init(tileset:columns:rows:tilesize:tilegrouplayout:).md)
  Creates and initializes a tile map node using the provided tile set with a specified number of columns and rows. For a grid set type, the overall size, in points, of the node will be `numberOfColumns * tileSize.width` wide and `numberOfRows * tileSize.height` high.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/tilemapnodes(tileset:columns:rows:tilesize:from:tiletypenoisemapthresholds:))*