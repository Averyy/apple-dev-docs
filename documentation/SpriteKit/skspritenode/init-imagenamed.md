# init(imageNamed:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a textured sprite using an image file.

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
convenience init(imageNamed name: String)
```

## Mentions

- [Resizing a Sprite in Nine Parts](resizing-a-sprite-in-nine-parts.md)

#### Return Value

A newly initialized sprite object.

#### Discussion

This method creates a new texture object from the image file and assigns that texture to the [`texture`](skspritenode/texture.md) property, the [`normalTexture`](skspritenode/normaltexture.md) properties is set to `nil`. The [`size`](skspritenode/size.md) property of the sprite is set to the dimensions of the image. The [`color`](skspritenode/color.md) property is set to white with an alpha of zero `(1.0,1.0,1.0,0.0)`.

## Parameters

- `name`: The name of an image file stored in the app bundle.

## See Also

- [Getting Started with Sprite Nodes](getting-started-with-sprite-nodes.md)
  Learn the basics about using images, also known as sprites, with SpriteKit.
- [convenience init(imageNamed: String, normalMapped: Bool)](skspritenode/init(imagenamed:normalmapped:).md)
  Initializes a textured sprite using an image file, optionally adding a normal map to simulate 3D lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(imagenamed:))*