# isEnabled

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the field is active.

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
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

## Mentions

- [Adding Physics Fields to a Scene](../adding-physics-fields-to-a-scene.md)

## See Also

### Determining Which Physics Bodies Are Affected by the Field
- [var isExclusive: Bool](./isexclusive.md)
  A Boolean value that indicates whether the field node should override all other field nodes that might otherwise affect physics bodies.
- [var region: SKRegion?](./region.md)
  The area (relative to the node’s origin) that the field affects.
- [var minimumRadius: Float](./minimumradius.md)
  The minimum value for distance-based effects.
- [var categoryBitMask: UInt32](./categorybitmask.md)
  A mask that defines which categories this field belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/isenabled)*