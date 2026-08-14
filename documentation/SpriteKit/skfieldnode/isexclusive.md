# isExclusive

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the field node should override all other field nodes that might otherwise affect physics bodies.

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
var isExclusive: Bool { get set }
```

#### Discussion

If the value is set to [`true`](https://developer.apple.com/documentation/swift/true) and a physics body is within this field’s region, all other field nodes that might otherwise affect this body are ignored. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

If you set this property to [`true`](https://developer.apple.com/documentation/swift/true) on multiple field nodes within a scene, their regions should not overlap. If they do, the results are undefined.

## See Also

- [var isEnabled: Bool](skfieldnode/isenabled.md)
  A Boolean value that indicates whether the field is active.
- [var region: SKRegion?](skfieldnode/region.md)
  The area (relative to the node’s origin) that the field affects.
- [var minimumRadius: Float](skfieldnode/minimumradius.md)
  The minimum value for distance-based effects.
- [var categoryBitMask: UInt32](skfieldnode/categorybitmask.md)
  A mask that defines which categories this field belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/isexclusive)*