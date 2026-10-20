# init(texture:size:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a textured sprite using an existing texture object but with a specified size.

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
convenience init(texture: SKTexture?, size: CGSize)
```

```objc
+ (instancetype) spriteNodeWithTexture:(SKTexture *) texture size:(CGSize) size;
```

#### Return Value

A newly initialized sprite object.

#### Discussion

The sprite is initialized using the texture, but the texture’s dimensions are not used. Instead, the size passed into the constructor method is used.

## Parameters

- `texture`: A SpriteKit texture.
- `size`: The size of the sprite in points.

## See Also

### Creating a Sprite from a Texture
- [convenience init(texture: SKTexture?)](./init%28texture%29.md)
  Initializes a textured sprite using an existing texture object.
- [init(texture: SKTexture?, color: UIColor, size: CGSize)](./init%28texture,color,size%29.md)
  Initializes a textured sprite in color using an existing texture object.
- [convenience init(texture: SKTexture?, normalMap: SKTexture?)](./init%28texture,normalmap%29.md)
  Initializes a textured sprite with a normal map to simulate 3D lighting.
- [var texture: SKTexture?](./texture.md)
  The texture used to draw the sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(texture:size:))*