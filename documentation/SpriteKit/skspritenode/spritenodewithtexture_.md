# spriteNodeWithTexture:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Initializes a textured sprite using an existing texture object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```objc
+ (instancetype) spriteNodeWithTexture:(SKTexture *) texture;
```

## Return Value

A newly initialized sprite object.

## Parameters

- `texture`: A SpriteKit texture.

## See Also

### Creating a Sprite from a Texture
- [convenience init(texture: SKTexture?)](./init%28texture%29.md)
  Initializes a textured sprite using an existing texture object.
- [init(texture: SKTexture?, color: UIColor, size: CGSize)](./init%28texture,color,size%29.md)
  Initializes a textured sprite in color using an existing texture object.
- [+ spriteNodeWithColor:size:](./spritenodewithcolor_size_.md)
  Initializes a single-color sprite.
- [+ spriteNodeWithImageNamed:](./spritenodewithimagenamed_.md)
  Initializes a textured sprite using an image file.
- [convenience init(texture: SKTexture?, size: CGSize)](./init%28texture,size%29.md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [convenience init(texture: SKTexture?, normalMap: SKTexture?)](./init%28texture,normalmap%29.md)
  Initializes a textured sprite with a normal map to simulate 3D lighting.
- [var texture: SKTexture?](./texture.md)
  The texture used to draw the sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/spritenodewithtexture:)*