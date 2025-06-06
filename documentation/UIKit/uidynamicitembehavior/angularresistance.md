# angularResistance

**Framework**: UIKit  
**Kind**: property

The angular resistance for the behavior’s dynamic items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var angularResistance: CGFloat { get set }
```

#### Discussion

Valid range is `0` through [`CGFLOAT_MAX`](https://developer.apple.com/documentation/CoreFoundation/CGFLOAT_MAX). The greater the value, the greater the angular damping and the faster rotation slows to a stop.

## See Also

- [func addAngularVelocity(CGFloat, for: any UIDynamicItem)](uidynamicitembehavior/addangularvelocity(_:for:).md)
  Adds a specified angular velocity to a dynamic item.
- [func addLinearVelocity(CGPoint, for: any UIDynamicItem)](uidynamicitembehavior/addlinearvelocity(_:for:).md)
  Adds a specified linear velocity to a dynamic item.
- [var allowsRotation: Bool](uidynamicitembehavior/allowsrotation.md)
  Specifies whether rotation is allowed for the behavior’s dynamic items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/angularresistance)*