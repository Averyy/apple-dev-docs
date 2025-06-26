# texture

**Framework**: SpriteKit  
**Kind**: property

The texture used to draw the sprite.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var texture: SKTexture? { get set }
```

#### Discussion

If the value is `nil`, the sprite is drawn as a single-color rectangle using its [`color`](skspritenode/color.md) property. Otherwise, the texture is used to draw the sprite. The related properties affect how the texture is applied.

SpriteKit automatically generates a texture for sprites when they are initialized with [`init(imageNamed:)`](skspritenode/init(imagenamed:).md).

## See Also

- [convenience init(texture: SKTexture?)](skspritenode/init(texture:).md)
  Initializes a textured sprite using an existing texture object.
- [init(texture: SKTexture?, color: UIColor, size: CGSize)](skspritenode/init(texture:color:size:).md)
  Initializes a textured sprite in color using an existing texture object.
- [convenience init(texture: SKTexture?, size: CGSize)](skspritenode/init(texture:size:).md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [convenience init(texture: SKTexture?, normalMap: SKTexture?)](skspritenode/init(texture:normalmap:).md)
  Initializes a textured sprite with a normal map to simulate 3D lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/texture)*