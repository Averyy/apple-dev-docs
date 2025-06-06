# addAngularVelocity(_:for:)

**Framework**: UIKit  
**Kind**: method

Adds a specified angular velocity to a dynamic item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addAngularVelocity(_ velocity: CGFloat, for item: any UIDynamicItem)
```

## Parameters

- `velocity`: The angular velocity, expressed in radians per second, that you want to add to the specified dynamic item. Default value is  . Applying a negative value reduces the angular velocity by the specified amount.
- `item`: The dynamic item whose angular velocity you want to increase (or decrease).

## See Also

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
- [var charge: CGFloat](uidynamicitembehavior/charge.md)
  The charge associated with the item.
- [var isAnchored: Bool](uidynamicitembehavior/isanchored.md)
  A Boolean value indicating whether the item is anchored to its current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/addangularvelocity(_:for:))*