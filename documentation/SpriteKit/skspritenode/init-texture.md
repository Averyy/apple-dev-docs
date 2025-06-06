# init(texture:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a textured sprite using an existing texture object.

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
@MainActor
convenience init(texture: SKTexture?)
```

#### Return Value

A newly initialized sprite object.

#### Discussion

The [`size`](skspritenode/size.md) property of the sprite is set to the dimensions of the texture. The [`color`](skspritenode/color.md) property is set to white with an alpha of zero `(1.0,1.0,1.0,0.0)`.

## Parameters

- `texture`: A SpriteKit texture.

## See Also

- [init(texture: SKTexture?, color: UIColor, size: CGSize)](skspritenode/init(texture:color:size:).md)
  Initializes a textured sprite in color using an existing texture object.
- [convenience init(texture: SKTexture?, size: CGSize)](skspritenode/init(texture:size:).md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [convenience init(texture: SKTexture?, normalMap: SKTexture?)](skspritenode/init(texture:normalmap:).md)
  Initializes a textured sprite with a normal map to simulate 3D lighting.
- [var texture: SKTexture?](skspritenode/texture.md)
  The texture used to draw the sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(texture:))*