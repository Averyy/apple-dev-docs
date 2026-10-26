# texture

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The texture used to draw the sprite.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var texture: SKTexture? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKTexture * texture;
```

#### Discussion

If the value is `nil`, the sprite is drawn as a single-color rectangle using its [`color`](./color.md) property. Otherwise, the texture is used to draw the sprite. The related properties affect how the texture is applied.

SpriteKit automatically generates a texture for sprites when they are initialized with [`init(imageNamed:)`](./init%28imagenamed%29.md).

## See Also

### Creating a Sprite from a Texture
- [convenience init(texture: SKTexture?)](./init%28texture%29.md)
  Initializes a textured sprite using an existing texture object.
- [init(texture: SKTexture?, color: UIColor, size: CGSize)](./init%28texture,color,size%29.md)
  Initializes a textured sprite in color using an existing texture object.
- [convenience init(texture: SKTexture?, size: CGSize)](./init%28texture,size%29.md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [convenience init(texture: SKTexture?, normalMap: SKTexture?)](./init%28texture,normalmap%29.md)
  Initializes a textured sprite with a normal map to simulate 3D lighting.
- [+ spriteNodeWithColor:size:](./spritenodewithcolor_size_.md)
  Initializes a single-color sprite.
- [+ spriteNodeWithImageNamed:](./spritenodewithimagenamed_.md)
  Initializes a textured sprite using an image file.
- [+ spriteNodeWithTexture:](./spritenodewithtexture_.md)
  Initializes a textured sprite using an existing texture object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/texture)*