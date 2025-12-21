# fieldBitMask

**Framework**: SpriteKit  
**Kind**: property

A mask that defines which categories of physics fields can exert forces on the particles.

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
var fieldBitMask: UInt32 { get set }
```

#### Discussion

When a particle is inside the region of a [`SKFieldNode`](skfieldnode.md) object, that field node’s [`categoryBitMask`](skfieldnode/categorybitmask.md) property is compared to the emitter’s [`fieldBitMask`](skemitternode/fieldbitmask.md) property by performing a logical AND operation. If the result is a non-zero value, then the field node’s effect is applied to the particle as if it had a physics body. The physics body is assumed to have a [`mass`](skphysicsbody/mass.md) of `1.0` and a [`charge`](skphysicsbody/charge.md) of `1.0`

The default value is `0x00000000` (all bits cleared).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/fieldbitmask)*