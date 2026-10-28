# particleSize

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The starting size of each particle.

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
var particleSize: CGSize { get set }
```

```objc
@property (nonatomic) CGSize particleSize;
```

## Discussion

The default value is [`CGSizeZero`](../../CoreGraphics/cgsizezero.md). If set to the default, the size of the texture stored in the [`particleTexture`](./particletexture.md) property is used to determine the size of a particle. If a texture has not been assigned, you must set this property to a non-empty size.

## See Also

### Changing a Particle’s Source Image and Size
- [var particleTexture: SKTexture?](./particletexture.md)
  The texture to use to render a particle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlesize)*