# SKTileGroupRule

**Framework**: SpriteKit  
**Kind**: class

Rules that describe how various tiles should be placed in a map.

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
class SKTileGroupRule
```

#### Overview

When a tile is filled in a tile map, the tile group rule defines how neighboring tiles are populated based on adjacency rules. A rule with multiple definitions uses the placement weights of the definitions to randomly select which to use.

## Topics

### Creating a Tile Group Rule
- [init(adjacency: SKTileAdjacencyMask, tileDefinitions: [SKTileDefinition])](sktilegrouprule/init(adjacency:tiledefinitions:).md)
  Initializes a new tile group rule with adjacency rules and tile definitions.
### Accessing or Setting Tile Group Rule Properties
- [var adjacency: SKTileAdjacencyMask](sktilegrouprule/adjacency.md)
  The adjacency requirement for this rule.
- [struct SKTileAdjacencyMask](sktileadjacencymask.md)
  An enumeration defining how neighboring tiles are automatically placed next to each other.
- [var name: String?](sktilegrouprule/name.md)
  A name associated with the tile group rule.
- [var tileDefinitions: [SKTileDefinition]](sktilegrouprule/tiledefinitions.md)
  The tile definitions used for this rule.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SKTileMapNode](sktilemapnode.md)
  A two-dimensional array of images.
- [class SKTileDefinition](sktiledefinition.md)
  A single tile that can be repeated in a tile map.
- [class SKTileGroup](sktilegroup.md)
  A set of tiles that collectively define one type of terrain.
- [class SKTileSet](sktileset.md)
  A container for related tile groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilegrouprule)*