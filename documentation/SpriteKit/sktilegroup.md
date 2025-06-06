# SKTileGroup

**Framework**: SpriteKit  
**Kind**: class

A set of tiles that collectively define one type of terrain.

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
class SKTileGroup
```

#### Overview

An `SKTileGroup` object contains either the definition of a single tile or an array of [`SKTileGroupRule`](sktilegrouprule.md) objects that define adjacency rules.

You supply a tile group with either:

- The definition of a single tile that can be used to populate a tile map node with a single texture.
- An array of one or more tile group rules that allow for the automatic placement of textures dependent on their adjacency and the placement weights of their definitions. For example, a tile group may contain nine tile group rules containing the definitions of the central tile and eight edge tiles that, when placed adjacently, appear as a single object.

The preferred method to create tile groups is to use the editor tools in Xcode. However, to work with SpriteKit’s tile support programmatically, see the following articles.

## Topics

### Creating Tile Groups
- [Creating Tile Groups Programmatically](creating-tile-groups-programmatically.md)
  Paint tiles on a map by putting tile definitions in a group that you create in code.
- [init(tileDefinition: SKTileDefinition)](sktilegroup/init(tiledefinition:).md)
  Creates and initializes a simple tile group with a single tile definition.
- [init(rules: [SKTileGroupRule])](sktilegroup/init(rules:).md)
  Creates and initializes a tile group with the specified tile group rules.
### Accessing or Setting a Tile Group’s Properties
- [var name: String?](sktilegroup/name.md)
  The receiver’s name.
- [var rules: [SKTileGroupRule]](sktilegroup/rules.md)
  An array of [`SKTileGroupRule`](sktilegrouprule.md) objects that the tile group uses to determine tile placement.
### Creating an Empty Tile Group
- [class func empty() -> Self](sktilegroup/empty.md)
  Creates an empty tile that erases the existing tile at that location on a tile map.

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
- [class SKTileGroupRule](sktilegrouprule.md)
  Rules that describe how various tiles should be placed in a map.
- [class SKTileSet](sktileset.md)
  A container for related tile groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilegroup)*