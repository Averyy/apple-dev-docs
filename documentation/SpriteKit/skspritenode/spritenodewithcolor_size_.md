# spriteNodeWithColor:size:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Initializes a single-color sprite.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
+ (instancetype) spriteNodeWithColor:(UIColor *) color size:(CGSize) size;
```

*macOS*

```objc
+ (instancetype) spriteNodeWithColor:(NSColor *) color size:(CGSize) size;
```

#### Return Value

A newly initialized sprite object.

## Parameters

- `color`: The color for the resulting sprite.
- `size`: The size of the sprite in points.

## See Also

### Creating a Sprite from a Texture
- [convenience init(texture: SKTexture?)](./init%28texture%29.md)
  Initializes a textured sprite using an existing texture object.
- [init(texture: SKTexture?, color: UIColor, size: CGSize)](./init%28texture,color,size%29.md)
  Initializes a textured sprite in color using an existing texture object.
- [+ spriteNodeWithImageNamed:](./spritenodewithimagenamed_.md)
  Initializes a textured sprite using an image file.
- [+ spriteNodeWithTexture:](./spritenodewithtexture_.md)
  Initializes a textured sprite using an existing texture object.
- [convenience init(texture: SKTexture?, size: CGSize)](./init%28texture,size%29.md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [convenience init(texture: SKTexture?, normalMap: SKTexture?)](./init%28texture,normalmap%29.md)
  Initializes a textured sprite with a normal map to simulate 3D lighting.
- [var texture: SKTexture?](./texture.md)
  The texture used to draw the sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/spritenodewithcolor:size:)*