# density

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The relative mass density of the behavior’s dynamic items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var density: CGFloat { get set }
```

```objc
@property (nonatomic, readwrite) CGFloat density;
```

## Discussion

A dynamic item’s relative density, along with its size, determines its effective mass when it participates in UIKit Dynamics behaviors—including friction, collisions, pushes, and so on. For example, say you have two dynamic items with the same density but different sizes: item one is `100 x 100` points and item two is `100 x 200` points. In this example, item two has twice the effective mass of item one. In an elastic collision, these items exhibit a natural conservation of momentum according to their relative masses.

A `100 x 100` point dynamic item with a density of `1.0`, to which you apply a force (via a push behavior) of magnitude `1.0`, accelerates at `100` points per second².

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
- [var elasticity: CGFloat](./elasticity.md)
  The amount of elasticity applied to collisions for the behavior’s dynamic items.
- [var friction: CGFloat](./friction.md)
  The linear resistance for the behavior’s dynamic items when two slide against each other.
- [var resistance: CGFloat](./resistance.md)
  The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [var charge: CGFloat](./charge.md)
  The charge associated with the item.
- [var isAnchored: Bool](./isanchored.md)
  A Boolean value indicating whether the item is anchored to its current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/density)*