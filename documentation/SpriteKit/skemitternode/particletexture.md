# particleTexture

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The texture to use to render a particle.

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
var particleTexture: SKTexture? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKTexture * particleTexture;
```

## Discussion

A particle is rendered as if it were a [`SKSpriteNode`](../skspritenode.md) object. The default value is `nil`, which means a single-color rectangle is used to draw the particle. If a non-`nil` value is specified, then the texture is colorized and used to draw particles.

## See Also

### Changing a Particle’s Source Image and Size
- [var particleSize: CGSize](./particlesize.md)
  The starting size of each particle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particletexture)*