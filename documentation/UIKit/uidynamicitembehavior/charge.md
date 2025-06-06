# charge

**Framework**: UIKit  
**Kind**: property

The charge associated with the item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var charge: CGFloat { get set }
```

#### Discussion

Charge determines the degree to which the item interacts with electric and magnetic fields. The value in this property has no units, so it is up to you to set the charge and field strengths to appropriate values for your interface. The default value of this property is `0.0`.

## See Also

- [func addAngularVelocity(CGFloat, for: any UIDynamicItem)](uidynamicitembehavior/addangularvelocity(_:for:).md)
  Adds a specified angular velocity to a dynamic item.
- [func addLinearVelocity(CGPoint, for: any UIDynamicItem)](uidynamicitembehavior/addlinearvelocity(_:for:).md)
  Adds a specified linear velocity to a dynamic item.
- [var allowsRotation: Bool](uidynamicitembehavior/allowsrotation.md)
  Specifies whether rotation is allowed for the behavior’s dynamic items.
- [var angularResistance: CGFloat](uidynamicitembehavior/angularresistance.md)
  The angular resistance for the behavior’s dynamic items.
- [func angularVelocity(for: any UIDynamicItem) -> CGFloat](uidynamicitembehavior/angularvelocity(for:).md)
  Returns the angular velocity for a specified dynamic item.
- [func linearVelocity(for: any UIDynamicItem) -> CGPoint](uidynamicitembehavior/linearvelocity(for:).md)
  Returns the linear velocity for a specified dynamic item.
- [var density: CGFloat](uidynamicitembehavior/density.md)
  The relative mass density of the behavior’s dynamic items.
- [var elasticity: CGFloat](uidynamicitembehavior/elasticity.md)
  The amount of elasticity applied to collisions for the behavior’s dynamic items.
- [var friction: CGFloat](uidynamicitembehavior/friction.md)
  The linear resistance for the behavior’s dynamic items when two slide against each other.
- [var resistance: CGFloat](uidynamicitembehavior/resistance.md)
  The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [var isAnchored: Bool](uidynamicitembehavior/isanchored.md)
  A Boolean value indicating whether the item is anchored to its current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/charge)*