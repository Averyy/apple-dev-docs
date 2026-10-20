# isExclusive

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isExclusive) BOOL exclusive;
```

#### Discussion

If the value is set to [`true`](../../Swift/true.md) and a physics body is within this field’s region, all other field nodes that might otherwise affect this body are ignored. The default value is [`false`](../../Swift/false.md).

If you set this property to [`true`](../../Swift/true.md) on multiple field nodes within a scene, their regions should not overlap. If they do, the results are undefined.

## See Also

### Determining Which Physics Bodies Are Affected by the Field
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the field is active.
- [var region: SKRegion?](./region.md)
  The area (relative to the node’s origin) that the field affects.
- [var minimumRadius: Float](./minimumradius.md)
  The minimum value for distance-based effects.
- [var categoryBitMask: UInt32](./categorybitmask.md)
  A mask that defines which categories this field belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/isexclusive)*