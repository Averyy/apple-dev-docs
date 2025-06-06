# SKTileSet

**Framework**: SpriteKit  
**Kind**: class

A container for related tile groups.

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
class SKTileSet
```

#### Overview

An [`SKTileSet`](sktileset.md) object contains an array of tile groups that define which tile definitions are available for use in a tile map.

Tile sets also define the arrangement of tiles within a tile map. In addition to the default rectangular grid layout, tile sets can also define hexagonal and isometric layouts.

## Topics

### Creating a Tile Set from a File
- [convenience init?(named: String)](sktileset/init(named:).md)
  Initializes a tile set by searching the app bundle for an archived `.sks` file by name.
- [convenience init?(from: URL)](sktileset/init(from:).md)
  Initializes a tile set from a URL to an archived .sks file.
### Creating a Tile Set Programmatically
- [init(tileGroups: [SKTileGroup])](sktileset/init(tilegroups:).md)
  Initializes a new tile set with an array of tile groups and rectangular grid layout.
- [init(tileGroups: [SKTileGroup], tileSetType: SKTileSetType)](sktileset/init(tilegroups:tilesettype:).md)
  Initializes a new tile set with an array of tile groups and specified layout.
### Accessing or Reading a Tile Set’s Properties
- [var defaultTileGroup: SKTileGroup?](sktileset/defaulttilegroup.md)
  The tile set’s default tile group.
- [var defaultTileSize: CGSize](sktileset/defaulttilesize.md)
  The tile set’s default tile size.
- [var name: String?](sktileset/name.md)
  A name associated with the tile set.
- [var tileGroups: [SKTileGroup]](sktileset/tilegroups.md)
  The tile set’s array of tile group objects.
- [var type: SKTileSetType](sktileset/type.md)
  The tile set’s type.
- [enum SKTileSetType](sktilesettype.md)
  An enumeration defining how tiles are arranged.

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
- [class SKTileGroupRule](sktilegrouprule.md)
  Rules that describe how various tiles should be placed in a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktileset)*