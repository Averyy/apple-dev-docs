# categoryBitMask

**Framework**: SpriteKit  
**Kind**: property

A mask that defines which categories this field belongs to.

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
var categoryBitMask: UInt32 { get set }
```

#### Discussion

Every field in a scene can be assigned to up to 32 different categories, each corresponding to a bit in the bit mask. The mask values are not predetermined by Sprite Kit. You define the mask values that are used in your game. The field node’s [`categoryBitMask`](skfieldnode/categorybitmask.md) property is compared to a physics body’s [`fieldBitMask`](skphysicsbody/fieldbitmask.md) property using a logical AND operation. If the result is nonzero, the field is applied to the physics body.

The default value is `0xFFFFFFFF` (all bits set).

## See Also

- [var isEnabled: Bool](skfieldnode/isenabled.md)
  A Boolean value that indicates whether the field is active.
- [var isExclusive: Bool](skfieldnode/isexclusive.md)
  A Boolean value that indicates whether the field node should override all other field nodes that might otherwise affect physics bodies.
- [var region: SKRegion?](skfieldnode/region.md)
  The area (relative to the node’s origin) that the field affects.
- [var minimumRadius: Float](skfieldnode/minimumradius.md)
  The minimum value for distance-based effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/categorybitmask)*