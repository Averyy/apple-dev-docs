# region

**Framework**: SpriteKit  
**Kind**: property

The area (relative to the node’s origin) that the field affects.

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
var region: SKRegion? { get set }
```

#### Discussion

A field node applies its effect to all physics bodies that are partially or completely inside its region. The default value is a region of infinite size.

## See Also

- [var isEnabled: Bool](skfieldnode/isenabled.md)
  A Boolean value that indicates whether the field is active.
- [var isExclusive: Bool](skfieldnode/isexclusive.md)
  A Boolean value that indicates whether the field node should override all other field nodes that might otherwise affect physics bodies.
- [var minimumRadius: Float](skfieldnode/minimumradius.md)
  The minimum value for distance-based effects.
- [var categoryBitMask: UInt32](skfieldnode/categorybitmask.md)
  A mask that defines which categories this field belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/region)*