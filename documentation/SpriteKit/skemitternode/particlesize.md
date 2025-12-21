# particleSize

**Framework**: SpriteKit  
**Kind**: property

The starting size of each particle.

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
var particleSize: CGSize { get set }
```

#### Discussion

The default value is [`CGSizeZero`](https://developer.apple.com/documentation/CoreGraphics/CGSizeZero). If set to the default, the size of the texture stored in the [`particleTexture`](skemitternode/particletexture.md) property is used to determine the size of a particle. If a texture has not been assigned, you must set this property to a non-empty size.

## See Also

- [var particleTexture: SKTexture?](skemitternode/particletexture.md)
  The texture to use to render a particle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlesize)*