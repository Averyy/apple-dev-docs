# UICollisionBehaviorDelegate

**Framework**: UIKit  
**Kind**: protocol

To respond to UIKit dynamic item collisions, configure a custom class to adopt the [`UICollisionBehaviorDelegate`](uicollisionbehaviordelegate.md) protocol. Then, in a collision behavior (an instance of the [`UICollisionBehavior`](uicollisionbehavior.md) class), set the delegate to be an instance of your custom class.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UICollisionBehaviorDelegate : NSObjectProtocol
```

#### Overview

The delegate is notified of collisions that occur between the behavior’s dynamic items, or between a dynamic item and a boundary, depending on the behavior’s mode (as set with its [`collisionMode`](uicollisionbehavior/collisionmode.md) property). In the case of a collision between an item and the boundary defined by a reference view, the identifier passed to the delegate method is `nil`. (For more on the reference view and the different ways to initialize a dynamic animator, read the Overview in [`UIDynamicAnimator`](uidynamicanimator.md).)

## Topics

### Responding to UIKit Dynamics collisions
- [func collisionBehavior(UICollisionBehavior, beganContactFor: any UIDynamicItem, withBoundaryIdentifier: (any NSCopying)?, at: CGPoint)](uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:withboundaryidentifier:at:).md)
  Called when a collision, between a dynamic item and a collision boundary, has begun.
- [func collisionBehavior(UICollisionBehavior, beganContactFor: any UIDynamicItem, with: any UIDynamicItem, at: CGPoint)](uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:with:at:).md)
  Called when a collision between two dynamic items has begun.
- [func collisionBehavior(UICollisionBehavior, endedContactFor: any UIDynamicItem, withBoundaryIdentifier: (any NSCopying)?)](uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:withboundaryidentifier:).md)
  Called when a collision between a dynamic item and a boundary has ended.
- [func collisionBehavior(UICollisionBehavior, endedContactFor: any UIDynamicItem, with: any UIDynamicItem)](uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:with:).md)
  Called when a collision between two dynamic items has ended.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var collisionDelegate: (any UICollisionBehaviorDelegate)?](uicollisionbehavior/collisiondelegate.md)
  The delegate object that you want to respond to collisions for the collision behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate)*