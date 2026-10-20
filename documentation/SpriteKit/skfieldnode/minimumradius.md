# minimumRadius

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The minimum value for distance-based effects.

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
var minimumRadius: Float { get set }
```

```objc
@property (nonatomic) float minimumRadius;
```

#### Discussion

When the distance between the node and a physics body is calculated, any distance shorter than the value stored in the [`minimumRadius`](./minimumradius.md) property is treated as if it is equal to it. The default value is a very small (but nonzero) value.

## See Also

### Determining Which Physics Bodies Are Affected by the Field
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the field is active.
- [var isExclusive: Bool](./isexclusive.md)
  A Boolean value that indicates whether the field node should override all other field nodes that might otherwise affect physics bodies.
- [var region: SKRegion?](./region.md)
  The area (relative to the node’s origin) that the field affects.
- [var categoryBitMask: UInt32](./categorybitmask.md)
  A mask that defines which categories this field belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/minimumradius)*