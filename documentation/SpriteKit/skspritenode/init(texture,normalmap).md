# init(texture:normalMap:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a textured sprite with a normal map to simulate 3D lighting.

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
convenience init(texture: SKTexture?, normalMap: SKTexture?)
```

```objc
+ (instancetype) spriteNodeWithTexture:(SKTexture *) texture normalMap:(SKTexture *) normalMap;
```

## Return Value

A newly initialized sprite object.

## Parameters

- `texture`: A SpriteKit texture used to draw the sprite.
- `normalMap`: A SpriteKit texture used to add lighting behavior to the sprite.

## See Also

### Creating a Sprite from a Texture
- [convenience init(texture: SKTexture?)](./init%28texture%29.md)
  Initializes a textured sprite using an existing texture object.
- [init(texture: SKTexture?, color: UIColor, size: CGSize)](./init%28texture,color,size%29.md)
  Initializes a textured sprite in color using an existing texture object.
- [convenience init(texture: SKTexture?, size: CGSize)](./init%28texture,size%29.md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [var texture: SKTexture?](./texture.md)
  The texture used to draw the sprite.
- [+ spriteNodeWithColor:size:](./spritenodewithcolor_size_.md)
  Initializes a single-color sprite.
- [+ spriteNodeWithImageNamed:](./spritenodewithimagenamed_.md)
  Initializes a textured sprite using an image file.
- [+ spriteNodeWithTexture:](./spritenodewithtexture_.md)
  Initializes a textured sprite using an existing texture object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(texture:normalmap:))*