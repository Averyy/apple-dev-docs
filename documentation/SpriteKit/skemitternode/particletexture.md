# particleTexture

**Framework**: SpriteKit  
**Kind**: property

The texture to use to render a particle.

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
var particleTexture: SKTexture? { get set }
```

#### Discussion

A particle is rendered as if it were a [`SKSpriteNode`](skspritenode.md) object. The default value is `nil`, which means a single-color rectangle is used to draw the particle. If a non-`nil` value is specified, then the texture is colorized and used to draw particles.

## See Also

- [var particleSize: CGSize](skemitternode/particlesize.md)
  The starting size of each particle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particletexture)*