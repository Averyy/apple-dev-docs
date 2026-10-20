# charge

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The electrical charge of the physics body.

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
var charge: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat charge;
```

#### Discussion

The electrical charge is used by electromagnetic fields to calculate electromagnetic force effects on the physics body. See [`SKFieldNode`](../skfieldnode.md).

## See Also

### Interacting with Physics Fields
- [var fieldBitMask: UInt32](./fieldbitmask.md)
  A mask that defines which categories of physics fields can exert forces on this physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/charge)*