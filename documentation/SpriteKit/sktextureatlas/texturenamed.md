# textureNamed(_:)

**Framework**: SpriteKit  
**Kind**: method

Creates a texture from data stored in the texture atlas.

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
func textureNamed(_ name: String) -> SKTexture
```

## Mentions

- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)
- [About Texture Atlases](about-texture-atlases.md)

#### Return Value

The SpriteKit texture associated with the name. If the specified image does not exist in the atlas object, SpriteKit returns a placeholder texture image.

## Parameters

- `name`: The name of a texture stored in the atlas object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktextureatlas/texturenamed(_:))*