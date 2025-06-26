# init(texture:normalMap:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a textured sprite with a normal map to simulate 3D lighting.

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
convenience init(texture: SKTexture?, normalMap: SKTexture?)
```

#### Return Value

A newly initialized sprite object.

## Parameters

- `texture`: A SpriteKit texture used to draw the sprite.
- `normalMap`: A SpriteKit texture used to add lighting behavior to the sprite.

## See Also

- [convenience init(texture: SKTexture?)](skspritenode/init(texture:).md)
  Initializes a textured sprite using an existing texture object.
- [init(texture: SKTexture?, color: UIColor, size: CGSize)](skspritenode/init(texture:color:size:).md)
  Initializes a textured sprite in color using an existing texture object.
- [convenience init(texture: SKTexture?, size: CGSize)](skspritenode/init(texture:size:).md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [var texture: SKTexture?](skspritenode/texture.md)
  The texture used to draw the sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(texture:normalmap:))*