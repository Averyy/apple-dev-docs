# SKTileDefinition

**Framework**: SpriteKit  
**Kind**: class

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

#### Overview

To define the visual representation of a single tile, you create an [`SKTileDefinition`](sktiledefinition.md) object with texture and size information. Tile definitions support separate normal textures, for simulating 3D lighting, and arrays of textures for animation with speed controlled by the [`timePerFrame`](sktiledefinition/timeperframe.md) property. Textures can be rotated in 90˚ increments or flipped either vertically or horizontally.

Once a tile definition has been created, you encapsulate it in a [`SKTileGroup`](sktilegroup.md) which is added to a [`SKTileSet`](sktileset.md) which, in turn, is displayed in the scene with a [`SKTileMapNode`](sktilemapnode.md).

## Topics

### Creating a Tile with a Texture
- [init(texture: SKTexture)](sktiledefinition/init(texture:).md)
  Initializes a new tile definition with a single texture.
### Creating a Tile with a Normal Texture
- [init(texture: SKTexture, normalTexture: SKTexture, size: CGSize)](sktiledefinition/init(texture:normaltexture:size:).md)
  Initializes a new tile definition with a single texture and separate normal texture for simulating 3D lighting.
### Creating a Tile with a Size
- [init(texture: SKTexture, size: CGSize)](sktiledefinition/init(texture:size:).md)
  Initializes a new tile definition of a specified size with a single texture.
### Creating an Animated Tile
- [init(textures: [SKTexture], normalTextures: [SKTexture], size: CGSize, timePerFrame: CGFloat)](sktiledefinition/init(textures:normaltextures:size:timeperframe:).md)
  Initializes a new tile definition with arrays of textures and normal textures for animation.
- [init(textures: [SKTexture], size: CGSize, timePerFrame: CGFloat)](sktiledefinition/init(textures:size:timeperframe:).md)
  Initializes a new tile definition with an array of textures for animation.
### Flipping a Tile Vertically or Horizontally
- [var flipHorizontally: Bool](sktiledefinition/fliphorizontally.md)
  A Boolean that flips the definition’s image vertically.
- [var flipVertically: Bool](sktiledefinition/flipvertically.md)
  A Boolean that flips the definition’s image horizontally.
### Rotating a Tile
- [var rotation: SKTileDefinitionRotation](sktiledefinition/rotation.md)
  The rotation of the tile definition in 90˚ increments.
- [enum SKTileDefinitionRotation](sktiledefinitionrotation.md)
  The allowed rotations for a given tile.
### Configure Animated Tile Properties
- [var textures: [SKTexture]](sktiledefinition/textures.md)
  An array of [`SKTexture`](sktexture.md) objects that defines the tile definition object’s content.
- [var normalTextures: [SKTexture]](sktiledefinition/normaltextures.md)
  An array of [`SKTexture`](sktexture.md) objects used to generate the normals for the tile to simulate 3D lighting.
- [var timePerFrame: CGFloat](sktiledefinition/timeperframe.md)
  The duration, in seconds, that each texture in the textures array is displayed before switching to the next texture in the sequence.
### Reading or Adding a Tile’s Custom Data
- [var userData: NSMutableDictionary?](sktiledefinition/userdata.md)
  A dictionary containing arbitrary data.
### Reading or Adjusting a Tile’s Instance Properties
- [var name: String?](sktiledefinition/name.md)
  A name associated with the tile definition.
- [var placementWeight: Int](sktiledefinition/placementweight.md)
  The placement weight of the tile definition.
- [var size: CGSize](sktiledefinition/size.md)
  The size of the tile definition in points.

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
- [class SKTileGroup](sktilegroup.md)
  A set of tiles that collectively define one type of terrain.
- [class SKTileGroupRule](sktilegrouprule.md)
  Rules that describe how various tiles should be placed in a map.
- [class SKTileSet](sktileset.md)
  A container for related tile groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktiledefinition)*