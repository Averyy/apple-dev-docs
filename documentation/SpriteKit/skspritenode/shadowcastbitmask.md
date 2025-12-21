# shadowCastBitMask

**Framework**: SpriteKit  
**Kind**: property

A mask that defines which lights are occluded by this sprite.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var shadowCastBitMask: UInt32 { get set }
```

## Mentions

- [Lighting a Sprite with Light Nodes](lighting-a-sprite-with-light-nodes.md)

#### Discussion

To determine whether this sprite blocks the light (casting a shadow), the sprite’s [`shadowedBitMask`](skspritenode/shadowedbitmask.md) property is tested against the light’s [`categoryBitMask`](https://developer.apple.com/documentation/SceneKit/SCNLight/categoryBitMask) property by performing a logical AND operation. If the comparison results in a nonzero value, the sprite casts a shadow past itself.

## See Also

- [Lighting a Sprite with Light Nodes](lighting-a-sprite-with-light-nodes.md)
  Add lighting and shadows to your scene with light nodes.
- [var lightingBitMask: UInt32](skspritenode/lightingbitmask.md)
  A mask that defines how this sprite is lit by light nodes in the scene.
- [var shadowedBitMask: UInt32](skspritenode/shadowedbitmask.md)
  A mask that defines which lights add shadows to the sprite.
- [var normalTexture: SKTexture?](skspritenode/normaltexture.md)
  A texture that specifies the normal map for the sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/shadowcastbitmask)*