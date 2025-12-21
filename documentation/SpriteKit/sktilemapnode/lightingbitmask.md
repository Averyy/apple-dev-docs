# lightingBitMask

**Framework**: SpriteKit  
**Kind**: property

A mask that defines how the tile map is lit by light nodes in the scene.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var lightingBitMask: UInt32 { get set }
```

#### Discussion

To determine whether this sprite is lit by a light node, the sprite’s `lightingBitMask` property is tested against the light’s [`categoryBitMask`](https://developer.apple.com/documentation/SceneKit/SCNLight/categoryBitMask) property by performing a logical AND operation. If the comparison results in a nonzero value, the sprite is lit by this light.

The default value is 0x00000000 (all bits cleared).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/lightingbitmask)*