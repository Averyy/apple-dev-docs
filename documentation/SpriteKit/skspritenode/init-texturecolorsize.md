# init(texture:color:size:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a textured sprite in color using an existing texture object.

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
init(texture: SKTexture?, color: NSColor, size: CGSize)
```

#### Return Value

A newly initialized sprite object.

#### Discussion

To colorize your texture, you also need to set the [`colorBlendFactor`](skspritenode/colorblendfactor.md) property of the sprite.

## Parameters

- `texture`: A texture to apply to the sprite.
- `color`: The color for the new sprite.
- `size`: The size for the new sprite.

## See Also

- [convenience init(texture: SKTexture?)](skspritenode/init(texture:).md)
  Initializes a textured sprite using an existing texture object.
- [convenience init(texture: SKTexture?, size: CGSize)](skspritenode/init(texture:size:).md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [convenience init(texture: SKTexture?, normalMap: SKTexture?)](skspritenode/init(texture:normalmap:).md)
  Initializes a textured sprite with a normal map to simulate 3D lighting.
- [var texture: SKTexture?](skspritenode/texture.md)
  The texture used to draw the sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(texture:color:size:))*