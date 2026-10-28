# init(texture:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

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

```swift
convenience init(texture: SKTexture?)
```

```objc
- (instancetype) initWithTexture:(SKTexture *) texture;
```

## Return Value

A newly initialized sprite object.

## Discussion

The [`size`](./size.md) property of the sprite is set to the dimensions of the texture. The [`color`](./color.md) property is set to white with an alpha of zero `(1.0,1.0,1.0,0.0)`.

## Parameters

- `texture`: A SpriteKit texture.

## See Also

### Creating a Sprite from a Texture
- [init(texture: SKTexture?, color: UIColor, size: CGSize)](./init%28texture,color,size%29.md)
  Initializes a textured sprite in color using an existing texture object.
- [convenience init(texture: SKTexture?, size: CGSize)](./init%28texture,size%29.md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [convenience init(texture: SKTexture?, normalMap: SKTexture?)](./init%28texture,normalmap%29.md)
  Initializes a textured sprite with a normal map to simulate 3D lighting.
- [var texture: SKTexture?](./texture.md)
  The texture used to draw the sprite.
- [+ spriteNodeWithColor:size:](./spritenodewithcolor_size_.md)
  Initializes a single-color sprite.
- [+ spriteNodeWithImageNamed:](./spritenodewithimagenamed_.md)
  Initializes a textured sprite using an image file.
- [+ spriteNodeWithTexture:](./spritenodewithtexture_.md)
  Initializes a textured sprite using an existing texture object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(texture:))*