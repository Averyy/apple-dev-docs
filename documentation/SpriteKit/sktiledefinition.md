# SKTileDefinition

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A single tile that can be repeated in a tile map.

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
class SKTileDefinition
```

```objc
@interface SKTileDefinition : NSObject
```

#### Overview

To define the visual representation of a single tile, you create an [`SKTileDefinition`](./sktiledefinition.md) object with texture and size information. Tile definitions support separate normal textures, for simulating 3D lighting, and arrays of textures for animation with speed controlled by the [`timePerFrame`](./sktiledefinition/timeperframe.md) property. Textures can be rotated in 90˚ increments or flipped either vertically or horizontally.

Once a tile definition has been created, you encapsulate it in a [`SKTileGroup`](./sktilegroup.md) which is added to a [`SKTileSet`](./sktileset.md) which, in turn, is displayed in the scene with a [`SKTileMapNode`](./sktilemapnode.md).

## Topics

### Creating a Tile with a Texture
- [init(texture: SKTexture)](./sktiledefinition/init%28texture%29.md)
  Initializes a new tile definition with a single texture.
### Creating a Tile with a Normal Texture
- [init(texture: SKTexture, normalTexture: SKTexture, size: CGSize)](./sktiledefinition/init%28texture,normaltexture,size%29.md)
  Initializes a new tile definition with a single texture and separate normal texture for simulating 3D lighting.
### Creating a Tile with a Size
- [init(texture: SKTexture, size: CGSize)](./sktiledefinition/init%28texture,size%29.md)
  Initializes a new tile definition of a specified size with a single texture.
### Creating an Animated Tile
- [init(textures: [SKTexture], normalTextures: [SKTexture], size: CGSize, timePerFrame: CGFloat)](./sktiledefinition/init%28textures,normaltextures,size,timeperframe%29.md)
  Initializes a new tile definition with arrays of textures and normal textures for animation.
- [init(textures: [SKTexture], size: CGSize, timePerFrame: CGFloat)](./sktiledefinition/init%28textures,size,timeperframe%29.md)
  Initializes a new tile definition with an array of textures for animation.
### Flipping a Tile Vertically or Horizontally
- [var flipHorizontally: Bool](./sktiledefinition/fliphorizontally.md)
  A Boolean that flips the definition’s image vertically.
- [var flipVertically: Bool](./sktiledefinition/flipvertically.md)
  A Boolean that flips the definition’s image horizontally.
### Rotating a Tile
- [var rotation: SKTileDefinitionRotation](./sktiledefinition/rotation.md)
  The rotation of the tile definition in 90˚ increments.
- [enum SKTileDefinitionRotation](./sktiledefinitionrotation.md)
  The allowed rotations for a given tile.
### Configure Animated Tile Properties
- [var textures: [SKTexture]](./sktiledefinition/textures.md)
  An array of [`SKTexture`](./sktexture.md) objects that defines the tile definition object’s content.
- [var normalTextures: [SKTexture]](./sktiledefinition/normaltextures.md)
  An array of [`SKTexture`](./sktexture.md) objects used to generate the normals for the tile to simulate 3D lighting.
- [var timePerFrame: CGFloat](./sktiledefinition/timeperframe.md)
  The duration, in seconds, that each texture in the textures array is displayed before switching to the next texture in the sequence.
### Reading or Adding a Tile’s Custom Data
- [var userData: NSMutableDictionary?](./sktiledefinition/userdata.md)
  A dictionary containing arbitrary data.
### Reading or Adjusting a Tile’s Instance Properties
- [var name: String?](./sktiledefinition/name.md)
  A name associated with the tile definition.
- [var placementWeight: Int](./sktiledefinition/placementweight.md)
  The placement weight of the tile definition.
- [var size: CGSize](./sktiledefinition/size.md)
  The size of the tile definition in points.
### Initializers
- [init?(coder: NSCoder)](./sktiledefinition/init%28coder%29.md)

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
- [class SKTileGroup](./sktilegroup.md)
  A set of tiles that collectively define one type of terrain.
- [class SKTileGroupRule](./sktilegrouprule.md)
  Rules that describe how various tiles should be placed in a map.
- [class SKTileSet](./sktileset.md)
  A container for related tile groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktiledefinition)*