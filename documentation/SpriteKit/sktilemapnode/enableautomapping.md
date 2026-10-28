# enableAutomapping

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

When creating a tile map node programmatically, specifies whether the tile map uses automapping behavior like the scene editor.

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
var enableAutomapping: Bool { get set }
```

```objc
@property (nonatomic) BOOL enableAutomapping;
```

## Discussion

This function is for use when you’re creating a tile map programmatically, versus creating it ahead of time with the scene editor.

Set this value to `true` when you want automapping behavior (equivalent to using the paint brush in the scene editor) when using the [`fill(with:)`](./fill%28with%29.md), and [`setTileGroup(_:andTileDefinition:forColumn:row:)`](./settilegroup%28_,andtiledefinition,forcolumn,row%29.md) functions.

## See Also

### Defining a Tile Map’s Contents
- [func fill(with: SKTileGroup?)](./fill%28with%29.md)
  When creating a tile map node programmatically, this function performs a fill operation with the specified tile group.
- [func setTileGroup(SKTileGroup, andTileDefinition: SKTileDefinition, forColumn: Int, row: Int)](./settilegroup%28_,andtiledefinition,forcolumn,row%29.md)
  Set the tile group and tile definition at the specified tile index.
- [func setTileGroup(SKTileGroup?, forColumn: Int, row: Int)](./settilegroup%28_,forcolumn,row%29.md)
  Set the tile group at the specified tile index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/enableautomapping)*