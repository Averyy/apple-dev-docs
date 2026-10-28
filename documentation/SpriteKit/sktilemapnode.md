# SKTileMapNode

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A two-dimensional array of images.

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
class SKTileMapNode
```

```objc
@interface SKTileMapNode : SKNode
```

## Overview

`SKTileMapNode` does the work of laying out predefined tiles in a grid of any size. Typically, you configure 9-slice images (tile groups) in Xcode’s SpriteKit scene editor and paint the look of your tile map ahead of time versus configuring the tile map in code.

As with sprite nodes, you can layer tile maps with different blend modes or control it with actions and physics, for example, for the purpose of parallax scrolling. The rendered tile map can be post processed with an [`SKShader`](./skshader.md) to add effects such as motion blur or atmospheric perspective.

> **Note**:  A tile map can only render tile definitions that exist within the [`SKTileSet`](./sktileset.md) you have provided it.

> ❗ **Important**:  A tile map does not expose its tiles as nodes, and therefore you cannot assign individual tiles with a different [`zPosition`](./sknode/zposition.md) or [`physicsBody`](./sknode/physicsbody.md). Instead, layer tile map nodes on top of each other at the varying zPositions, and layer invisible `SKNodes` on top of the tile map node to attach physicsBodies to your tile map node.

To work with a tile map programmatically, you supply `SKTileMapNode` with a tile set that defines the tile definitions it can render. Then, fill each tile in the tile map with the [`fill(with:)`](./sktilemapnode/fill%28with%29.md) method and set individual tiles with [`setTileGroup(_:andTileDefinition:forColumn:row:)`](./sktilemapnode/settilegroup%28_,andtiledefinition,forcolumn,row%29.md).

## Topics

### Creating a Tile Map Programmatically
- [Creating a Tile Map Programmatically](./creating-a-tile-map-programmatically.md)
### Controlling a Tile Map’s On-Screen Position Relative to its Origin
- [var anchorPoint: CGPoint](./sktilemapnode/anchorpoint.md)
  Defines the point in the tile map that corresponds to its [`position`](./sknode/position.md).
### Reading or Manually Configuring the Tile Map’s Size
- [var tileSize: CGSize](./sktilemapnode/tilesize.md)
  The size of each tile in points.
- [var tileSet: SKTileSet](./sktilemapnode/tileset.md)
  The tile set being used by this tile map. The tile map object can only display tiles that exist in this set.
- [var numberOfColumns: Int](./sktilemapnode/numberofcolumns.md)
  The number of columns in the tile map
- [var numberOfRows: Int](./sktilemapnode/numberofrows.md)
  The number of rows in the tile map.
### Querying the Tile Map’s Properties
- [func centerOfTile(atColumn: Int, row: Int) -> CGPoint](./sktilemapnode/centeroftile%28atcolumn,row%29.md)
- [func tileColumnIndex(fromPosition: CGPoint) -> Int](./sktilemapnode/tilecolumnindex%28fromposition%29.md)
- [func tileDefinition(atColumn: Int, row: Int) -> SKTileDefinition?](./sktilemapnode/tiledefinition%28atcolumn,row%29.md)
- [func tileGroup(atColumn: Int, row: Int) -> SKTileGroup?](./sktilemapnode/tilegroup%28atcolumn,row%29.md)
- [func tileRowIndex(fromPosition: CGPoint) -> Int](./sktilemapnode/tilerowindex%28fromposition%29.md)
  Returns the tile map node object’s tile row index for the specified position in points.
- [var mapSize: CGSize](./sktilemapnode/mapsize.md)
  The overall size of the tile map.
### Tinting a Tile Map
- [var color: UIColor](./sktilemapnode/color.md)
  The base color for the tile map. The influence of the color over the tile map node’s textures is controlled by [`colorBlendFactor`](./sktilemapnode/colorblendfactor.md).
- [var colorBlendFactor: CGFloat](./sktilemapnode/colorblendfactor.md)
  Controls the blending between the texture and the tile map object’s [`color`](./sktilemapnode/color.md). Values are clamped between zero and one where zero has no color blending and one has the maximum color blending.
### Lighting a Tile Map
- [var lightingBitMask: UInt32](./sktilemapnode/lightingbitmask.md)
  A mask that defines how the tile map is lit by light nodes in the scene.
### Configuring How Alpha Values Blend the Sprite
- [var blendMode: SKBlendMode](./sktilemapnode/blendmode.md)
  Defines the blend mode to use when compositing the tile map over other nodes.
### Working with Custom Shaders
- [var shader: SKShader?](./sktilemapnode/shader.md)
  Defines a shader which is applied to each tile of the tile map.
- [var attributeValues: [String : SKAttributeValue]](./sktilemapnode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](./sktilemapnode/setvalue%28_,forattribute%29.md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](./sktilemapnode/value%28forattributenamed%29.md)
  The value of a shader attribute.
### Initializers
- [init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWithTileGroup: SKTileGroup)](./sktilemapnode/init%28tileset,columns,rows,tilesize,fillwithtilegroup%29-58e45.md)
- [convenience init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWithTileGroup: SKTileGroup)](./sktilemapnode/init%28tileset,columns,rows,tilesize,fillwithtilegroup%29-86yc2.md)

## Relationships

### Inherits From
- [SKNode](./sknode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Tiling
- [class SKTileDefinition](./sktiledefinition.md)
  A single tile that can be repeated in a tile map.
- [class SKTileGroup](./sktilegroup.md)
  A set of tiles that collectively define one type of terrain.
- [class SKTileGroupRule](./sktilegrouprule.md)
  Rules that describe how various tiles should be placed in a map.
- [class SKTileSet](./sktileset.md)
  A container for related tile groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode)*