# fieldBitMask

**Framework**: SpriteKit  
**Kind**: property

A mask that defines which categories of physics fields can exert forces on this physics body.

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
var fieldBitMask: UInt32 { get set }
```

#### Discussion

When a physics body is inside the region of an [`SKFieldNode`](skfieldnode.md) object, that field node’s [`categoryBitMask`](skfieldnode/categorybitmask.md) property is compared to this physics body’s [`fieldBitMask`](skphysicsbody/fieldbitmask.md) property by performing a logical AND operation. If the result is a nonzero value, the field node’s effect is applied to the physics body.

The default value is `0xFFFFFFFF` (all bits set).

## See Also

- [var charge: CGFloat](skphysicsbody/charge.md)
  The electrical charge of the physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/fieldbitmask)*