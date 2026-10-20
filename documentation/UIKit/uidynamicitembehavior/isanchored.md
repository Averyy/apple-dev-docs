# isAnchored

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the item is anchored to its current position.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isAnchored: Bool { get set }
```

```objc
@property (nonatomic, getter=isAnchored) BOOL anchored;
```

#### Discussion

An anchored item participates in collisions but is not affected by those collisions. Instead, the item behaves like a collision boundary. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring a dynamic item behavior
- [func addAngularVelocity(CGFloat, for: any UIDynamicItem)](./addangularvelocity%28_,for%29.md)
  Adds a specified angular velocity to a dynamic item.
- [func addLinearVelocity(CGPoint, for: any UIDynamicItem)](./addlinearvelocity%28_,for%29.md)
  Adds a specified linear velocity to a dynamic item.
- [var allowsRotation: Bool](./allowsrotation.md)
  Specifies whether rotation is allowed for the behavior’s dynamic items.
- [var angularResistance: CGFloat](./angularresistance.md)
  The angular resistance for the behavior’s dynamic items.
- [func angularVelocity(for: any UIDynamicItem) -> CGFloat](./angularvelocity%28for%29.md)
  Returns the angular velocity for a specified dynamic item.
- [func linearVelocity(for: any UIDynamicItem) -> CGPoint](./linearvelocity%28for%29.md)
  Returns the linear velocity for a specified dynamic item.
- [var density: CGFloat](./density.md)
  The relative mass density of the behavior’s dynamic items.
- [var elasticity: CGFloat](./elasticity.md)
  The amount of elasticity applied to collisions for the behavior’s dynamic items.
- [var friction: CGFloat](./friction.md)
  The linear resistance for the behavior’s dynamic items when two slide against each other.
- [var resistance: CGFloat](./resistance.md)
  The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [var charge: CGFloat](./charge.md)
  The charge associated with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/isanchored)*