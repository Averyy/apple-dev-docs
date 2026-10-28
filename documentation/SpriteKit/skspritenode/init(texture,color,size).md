# init(texture:color:size:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a textured sprite in color using an existing texture object.

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

```swift
init(texture: SKTexture?, color: UIColor, size: CGSize)
```

*macOS*

```swift
init(texture: SKTexture?, color: NSColor, size: CGSize)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (instancetype) initWithTexture:(SKTexture *) texture color:(UIColor *) color size:(CGSize) size;
```

*macOS*

```objc
- (instancetype) initWithTexture:(SKTexture *) texture color:(NSColor *) color size:(CGSize) size;
```

## Return Value

A newly initialized sprite object.

## Discussion

To colorize your texture, you also need to set the [`colorBlendFactor`](./colorblendfactor.md) property of the sprite.

## Parameters

- `texture`: A texture to apply to the sprite.
- `color`: The color for the new sprite.
- `size`: The size for the new sprite.

## See Also

### Creating a Sprite from a Texture
- [convenience init(texture: SKTexture?)](./init%28texture%29.md)
  Initializes a textured sprite using an existing texture object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(texture:color:size:))*