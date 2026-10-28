# elasticity

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The amount of elasticity applied to collisions for the behavior’s dynamic items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var elasticity: CGFloat { get set }
```

```objc
@property (nonatomic, readwrite) CGFloat elasticity;
```

## Discussion

Default value is `0.0`. Valid range is from `0.0` for no bounce upon collision, to `1.0` for completely elastic collisions.

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
- [var friction: CGFloat](./friction.md)
  The linear resistance for the behavior’s dynamic items when two slide against each other.
- [var resistance: CGFloat](./resistance.md)
  The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [var charge: CGFloat](./charge.md)
  The charge associated with the item.
- [var isAnchored: Bool](./isanchored.md)
  A Boolean value indicating whether the item is anchored to its current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/elasticity)*