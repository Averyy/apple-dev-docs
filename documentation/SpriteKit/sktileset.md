# SKTileSet

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface SKTileSet : NSObject
```

#### Overview

An [`SKTileSet`](./sktileset.md) object contains an array of tile groups that define which tile definitions are available for use in a tile map.

Tile sets also define the arrangement of tiles within a tile map. In addition to the default rectangular grid layout, tile sets can also define hexagonal and isometric layouts.

## Topics

### Creating a Tile Set from a File
- [convenience init?(named: String)](./sktileset/init%28named%29.md)
  Initializes a tile set by searching the app bundle for an archived `.sks` file by name.
- [convenience init?(from: URL)](./sktileset/init%28from%29.md)
  Initializes a tile set from a URL to an archived .sks file.
### Creating a Tile Set Programmatically
- [init(tileGroups: [SKTileGroup])](./sktileset/init%28tilegroups%29.md)
  Initializes a new tile set with an array of tile groups and rectangular grid layout.
- [init(tileGroups: [SKTileGroup], tileSetType: SKTileSetType)](./sktileset/init%28tilegroups,tilesettype%29.md)
  Initializes a new tile set with an array of tile groups and specified layout.
- [+ tileSetWithTileGroups:](./sktileset/tilesetwithtilegroups_.md)
- [+ tileSetWithTileGroups:tileSetType:](./sktileset/tilesetwithtilegroups_tilesettype_.md)
### Accessing or Reading a Tile Set’s Properties
- [var defaultTileGroup: SKTileGroup?](./sktileset/defaulttilegroup.md)
  The tile set’s default tile group.
- [var defaultTileSize: CGSize](./sktileset/defaulttilesize.md)
  The tile set’s default tile size.
- [var name: String?](./sktileset/name.md)
  A name associated with the tile set.
- [var tileGroups: [SKTileGroup]](./sktileset/tilegroups.md)
  The tile set’s array of tile group objects.
- [var type: SKTileSetType](./sktileset/type.md)
  The tile set’s type.
- [enum SKTileSetType](./sktilesettype.md)
  An enumeration defining how tiles are arranged.
### Initializers
- [init?(coder: NSCoder)](./sktileset/init%28coder%29.md)
- [convenience init?(fromURL: URL)](./sktileset/init%28fromurl%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

## See Also

### Tiling
- [class SKTileMapNode](./sktilemapnode.md)
  A two-dimensional array of images.
- [class SKTileDefinition](./sktiledefinition.md)
  A single tile that can be repeated in a tile map.
- [class SKTileGroup](./sktilegroup.md)
  A set of tiles that collectively define one type of terrain.
- [class SKTileGroupRule](./sktilegrouprule.md)
  Rules that describe how various tiles should be placed in a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktileset)*