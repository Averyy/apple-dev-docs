# UICollisionBehavior

**Framework**: UIKit  
**Kind**: class

An object that confers to a specified array of dynamic items the ability to engage in collisions with each other and with the behavior’s specified boundaries.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollisionBehavior
```

#### Overview

A collision behavior also specifies some characteristics of its items’ collisions, with other characteristics optionally specified by a [`UIDynamicItemBehavior`](uidynamicitembehavior.md) object. A  is any iOS or custom object that conforms to the [`UIDynamicItem`](uidynamicitem.md) protocol. The [`UIView`](uiview.md) and [`UICollectionViewLayoutAttributes`](uicollectionviewlayoutattributes.md) classes implement this protocol starting in iOS 7.0. You can use a custom object as a dynamic item for such purposes as reacting to rotation or position changes computed by a dynamic animator—an instance of the [`UIDynamicAnimator`](uidynamicanimator.md) class.

To use a collision behavior with a dynamic item, perform these two steps:

1. Associate the item with the behavior using the [`addItem(_:)`](uicollisionbehavior/additem(_:).md) method, or initialize a new collision behavior with an array of items using the [`init(items:)`](uicollisionbehavior/init(items:).md) method.
2. Enable the behavior by adding it to an animator using the [`addBehavior(_:)`](uidynamicanimator/addbehavior(_:).md) method

The coordinate system that pertains to a collision behavior, and the types of dynamic items you can use with the behavior, depend on how you initialized the associated animator. For details, read the Overview of [`UIDynamicAnimator`](uidynamicanimator.md).

You can add multiple collision behaviors to a dynamic animator. A dynamic item can be part of any number of collision behaviors, provided those behaviors belong to the same animator. For example, you can specify a collision behavior for a set of say, blue, items and another for, say, pink items. When you add both behaviors to a dynamic animator, blue items can collide with each other and pink items can collide with each other, but a blue item and a pink item would not collide—they would ignore each other.

By default, a collision behavior’s items can collide with each other  with any boundaries you’ve specified for the behavior. If you want to specify that a behavior’s items collide only with each other, or only with boundaries, explicitly set the [`collisionMode`](uicollisionbehavior/collisionmode.md) property.

You can define a collision boundary with a bezier path (see the [`addBoundary(withIdentifier:for:)`](uicollisionbehavior/addboundary(withidentifier:for:).md) method) or with a line segment (see the [`addBoundary(withIdentifier:from:to:)`](uicollisionbehavior/addboundary(withidentifier:from:to:).md) method). When you use a collision behavior with a dynamic animator you’ve initialized with a reference view or a collection view layout, you can also specify a collision boundary according to the bounds of the dynamic animator’s coordinate system (see the [`setTranslatesReferenceBoundsIntoBoundary(with:)`](uicollisionbehavior/settranslatesreferenceboundsintoboundary(with:).md) method).

> ❗ **Important**:  When setting the initial position for a dynamic item, you must ensure that its bounds do not intersect any collision boundaries. The animation behavior for such a misplaced item is undefined.

To respond to collisions, implement a delegate object that adopts the [`UICollisionBehaviorDelegate`](uicollisionbehaviordelegate.md) protocol. Add the delegate to the behavior using the [`collisionDelegate`](uicollisionbehavior/collisiondelegate.md) property.

You can include a collision behavior in a custom, composite behavior by starting with a [`UIDynamicBehavior`](uidynamicbehavior.md) object and adding a collision behavior with the [`addChildBehavior(_:)`](uidynamicbehavior/addchildbehavior(_:).md) method.  If you want to influence a collision behavior at each step of a dynamic animation, implement the inherited [`action`](uidynamicbehavior/action.md) method.

## Topics

### Initializing and managing a collision behavior
- [func addItem(any UIDynamicItem)](uicollisionbehavior/additem(_:).md)
  Adds a dynamic item to the collision behavior’s item array.
- [init(items: [any UIDynamicItem])](uicollisionbehavior/init(items:).md)
  Initializes a collision behavior with an array of dynamic items.
- [func removeItem(any UIDynamicItem)](uicollisionbehavior/removeitem(_:).md)
  Removes a specific dynamic item from the collision behavior.
- [var items: [any UIDynamicItem]](uicollisionbehavior/items.md)
  Returns the set of dynamic items you’ve added to the collision behavior.
### Customizing the collision behavior
- [var collisionDelegate: (any UICollisionBehaviorDelegate)?](uicollisionbehavior/collisiondelegate.md)
  The delegate object that you want to respond to collisions for the collision behavior.
- [protocol UICollisionBehaviorDelegate](uicollisionbehaviordelegate.md)
  To respond to UIKit dynamic item collisions, configure a custom class to adopt the [`UICollisionBehaviorDelegate`](uicollisionbehaviordelegate.md) protocol. Then, in a collision behavior (an instance of the [`UICollisionBehavior`](uicollisionbehavior.md) class), set the delegate to be an instance of your custom class.
### Configuring a collision behavior
- [func addBoundary(withIdentifier: any NSCopying, for: UIBezierPath)](uicollisionbehavior/addboundary(withidentifier:for:).md)
  Adds a collision boundary, specified as a Bezier path, to the collision behavior.
- [func addBoundary(withIdentifier: any NSCopying, from: CGPoint, to: CGPoint)](uicollisionbehavior/addboundary(withidentifier:from:to:).md)
  Adds a collision boundary, specified as a line segment, to the collision behavior.
- [var boundaryIdentifiers: [any NSCopying]?](uicollisionbehavior/boundaryidentifiers.md)
  The set of boundary identifiers that you’ve added to the collision behavior.
- [func boundary(withIdentifier: any NSCopying) -> UIBezierPath?](uicollisionbehavior/boundary(withidentifier:).md)
  Returns a specified Bezier-path boundary.
- [var collisionMode: UICollisionBehavior.Mode](uicollisionbehavior/collisionmode.md)
  The type of edges that participate in collisions for the collision behavior.
- [func removeAllBoundaries()](uicollisionbehavior/removeallboundaries.md)
  Removes all previously-specified collision boundaries from the collision behavior.
- [func removeBoundary(withIdentifier: any NSCopying)](uicollisionbehavior/removeboundary(withidentifier:).md)
  Removes a specific collision boundary from the collision behavior.
- [func setTranslatesReferenceBoundsIntoBoundary(with: UIEdgeInsets)](uicollisionbehavior/settranslatesreferenceboundsintoboundary(with:).md)
  Specifies a collision boundary based on the bounds of the animation reference system, with optional insets.
- [var translatesReferenceBoundsIntoBoundary: Bool](uicollisionbehavior/translatesreferenceboundsintoboundary.md)
  Specifies whether a boundary based on the reference system is active.
### Constants
- [UICollisionBehavior.Mode](uicollisionbehavior/mode.md)
  The types of edges that participate in collisions for a collision behavior.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIDynamicBehavior](uidynamicbehavior.md)
  An object that confers a behavioral configuration on one or more dynamic items, for their participation in 2D animation.
- [class UIAttachmentBehavior](uiattachmentbehavior.md)
  A relationship between two dynamic items, or between a dynamic item and an anchor point.
- [class UIFieldBehavior](uifieldbehavior.md)
  An object that applies field-based physics to dynamic items.
- [class UIGravityBehavior](uigravitybehavior.md)
  An object that applies a gravity-like force to all of its associated dynamic items.
- [class UIPushBehavior](uipushbehavior.md)
  A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.
- [class UISnapBehavior](uisnapbehavior.md)
  A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior)*