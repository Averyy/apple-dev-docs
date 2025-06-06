# UIDynamicItemBehavior

**Framework**: UIKit  
**Kind**: class

A base dynamic animation configuration for one or more dynamic items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDynamicItemBehavior
```

#### Overview

A  is any iOS or custom object that conforms to the [`UIDynamicItem`](uidynamicitem.md) protocol. The [`UIView`](uiview.md) and [`UICollectionViewLayoutAttributes`](uicollectionviewlayoutattributes.md) classes implement this protocol in iOS 7 and later. You can use a custom object as a dynamic item for such purposes as reacting to rotation or position changes computed by a dynamic animator—an instance of the [`UIDynamicAnimator`](uidynamicanimator.md) class.

One notable and common use of a dynamic item behavior is to confer a velocity to a dynamic item to match the ending velocity of a user gesture.

To use a dynamic item behavior with a dynamic item, perform these two steps:

1. Associate the item with the behavior using the [`addItem(_:)`](uidynamicitembehavior/additem(_:).md) method, or initialize a new dynamic item behavior with an array of items using the [`init(items:)`](uidynamicitembehavior/init(items:).md) method
2. Enable the behavior by adding it to an animator using the [`addBehavior(_:)`](uidynamicanimator/addbehavior(_:).md) method

The coordinate system that pertains to a dynamic item behavior, and the types of dynamic items you can use with the behavior, depend on how you initialized the associated animator. For details, see [`UIDynamicAnimator`](uidynamicanimator.md).

You can disable rotation for a dynamic item behavior’s items by returning [`false`](https://developer.apple.com/documentation/swift/false) from the [`allowsRotation`](uidynamicitembehavior/allowsrotation.md) property. To configure interaction among the behavior’s items, use the [`elasticity`](uidynamicitembehavior/elasticity.md) and [`friction`](uidynamicitembehavior/friction.md) properties.

You can include a dynamic item behavior in a custom, composite behavior by starting with a [`UIDynamicBehavior`](uidynamicbehavior.md) object and adding a dynamic item behavior with the [`addChildBehavior(_:)`](uidynamicbehavior/addchildbehavior(_:).md) method. If you want to influence a dynamic item behavior at each step of a dynamic animation, implement the inherited [`action`](uidynamicbehavior/action.md) method.

If you add more than one dynamic item behavior to an animator, you effectively create a behavior tree. Only one configuration of a given property applies to any given dynamic item. For a property configured in more than one dynamic item behavior, the last one in the behavior tree, starting from the dynamic animator and going depth first toward the dynamic item, wins.

In the case of an animator with exactly one dynamic item behavior, you can restore default values for all dynamic item behavior properties by removing the behavior. In the case of an animator to which you’ve applied multiple dynamic item behaviors, removing one takes its property contribution out of the behavior tree.

## Topics

### Initializing and managing a dynamic item behavior
- [func addItem(any UIDynamicItem)](uidynamicitembehavior/additem(_:).md)
  Adds a dynamic item to the dynamic item behavior’s item array.
- [init(items: [any UIDynamicItem])](uidynamicitembehavior/init(items:).md)
  Initializes a dynamic item behavior with an array of dynamic items.
- [func removeItem(any UIDynamicItem)](uidynamicitembehavior/removeitem(_:).md)
  Removes a specific dynamic item from the dynamic item behavior.
- [var items: [any UIDynamicItem]](uidynamicitembehavior/items.md)
  Returns the set of dynamic items you’ve added to the dynamic item behavior.
### Configuring a dynamic item behavior
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
- [var charge: CGFloat](uidynamicitembehavior/charge.md)
  The charge associated with the item.
- [var isAnchored: Bool](uidynamicitembehavior/isanchored.md)
  A Boolean value indicating whether the item is anchored to its current position.

## Relationships

### Inherits From
- [UIDynamicBehavior](uidynamicbehavior.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UIDynamicItem](uidynamicitem.md)
  A set of methods that can make a custom object eligible to participate in UIKit Dynamics.
- [class UIDynamicItemGroup](uidynamicitemgroup.md)
  A dynamic item that comprises multiple other dynamic items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior)*