# lightingBitMask

**Framework**: SpriteKit  
**Kind**: property

A mask that defines how this sprite is lit by light nodes in the scene.

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
@MainActor
var lightingBitMask: UInt32 { get set }
```

## Mentions

- [Lighting a Sprite with Light Nodes](lighting-a-sprite-with-light-nodes.md)

#### Discussion

To determine whether this sprite is lit by a light node, the sprite’s [`lightingBitMask`](skspritenode/lightingbitmask.md) property is tested against the light’s [`categoryBitMask`](https://developer.apple.com/documentation/SceneKit/SCNLight/categoryBitMask) property by performing a logical AND operation. If the comparison results in a nonzero value, the sprite is lit by this light.

The default value is 0x00000000 (all bits cleared).

## See Also

- [Lighting a Sprite with Light Nodes](lighting-a-sprite-with-light-nodes.md)
  Add lighting and shadows to your scene with light nodes.
- [var shadowedBitMask: UInt32](skspritenode/shadowedbitmask.md)
  A mask that defines which lights add shadows to the sprite.
- [var shadowCastBitMask: UInt32](skspritenode/shadowcastbitmask.md)
  A mask that defines which lights are occluded by this sprite.
- [var normalTexture: SKTexture?](skspritenode/normaltexture.md)
  A texture that specifies the normal map for the sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/lightingbitmask)*