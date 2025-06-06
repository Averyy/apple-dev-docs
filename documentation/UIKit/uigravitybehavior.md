# UIGravityBehavior

**Framework**: Uikit  
**Kind**: class

An object that applies a gravity-like force to all of its associated dynamic items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIGravityBehavior
```

#### Overview

The magnitude and direction of the gravity force are configurable and are applied equally to all associated items. Use this behavior to modify the position of views and other dynamic items in your app’s interface.

You specify the magnitude and direction of the gravity force as a two-dimensional vector in the reference view’s coordinate system. A value of `1.0` imparts the standard UIKit gravity, which corresponds to an acceleration of 1000 points / second² in the direction of the given axis. The default vector in the [`gravityDirection`](uigravitybehavior/gravitydirection.md) property is (`0.0`, `1.0`), which causes items to accelerate downward along the positive y axis. If you prefer to set the vector [`angle`](uigravitybehavior/angle.md) and [`magnitude`](uigravitybehavior/magnitude.md) separately, you can do so using the corresponding properties.

> **Note**:  If you want a gravitational force that takes the mass of each object into account, use a [`UIFieldBehavior`](uifieldbehavior.md) object instead. Field behaviors support both linear and radial gravitation fields and take the mass of an object into account, resulting in different amounts of force applied to each object.

If you want to influence a gravity behavior at each step of a dynamic animation, assign an appropriate block to the inherited [`action`](uidynamicbehavior/action.md) property. Use your block to make any needed changes to the dynamic items associated with the gravity behavior.

##### Applying a Gravity Behavior to an Item

To apply a gravity behavior to one or more dynamic items, do the following:

1. Initialize the behavior using the [`init(items:)`](uigravitybehavior/init(items:).md) method, passing in the items you want associated with the behavior. Use the [`addItem(_:)`](uigravitybehavior/additem(_:).md) method to add items after initialization. For more information about dynamic items, see [`UIDynamicItem`](uidynamicitem.md).
2. Enable the gravity behavior by adding it to your [`UIDynamicAnimator`](uidynamicanimator.md) object using the [`addBehavior(_:)`](uidynamicanimator/addbehavior(_:).md) method. (Do not add more than one gravity behavior to an animator.)

The gravity behavior derives its coordinate system from the reference view of its associated dynamic animator object. For more information about the dynamic animator and the reference coordinate system, see [`UIDynamicAnimator`](uidynamicanimator.md).

## Topics

### Initializing a gravity behavior
- [init(items: [any UIDynamicItem])](uigravitybehavior/init(items:).md)
  Initializes a gravity behavior with an array of dynamic items.
### Managing a gravity behavior’s items
- [var items: [any UIDynamicItem]](uigravitybehavior/items.md)
  The set of dynamic items associated with the gravity behavior.
- [func addItem(any UIDynamicItem)](uigravitybehavior/additem(_:).md)
  Associates the specified dynamic item with the gravity behavior.
- [func removeItem(any UIDynamicItem)](uigravitybehavior/removeitem(_:).md)
  Removes the specified dynamic item from the gravity behavior.
### Configuring a gravity behavior
- [var gravityDirection: CGVector](uigravitybehavior/gravitydirection.md)
  The direction and magnitude of the gravitational force, expressed as a vector.
- [var angle: CGFloat](uigravitybehavior/angle.md)
  The direction of the gravity vector, expressed in radians in the reference coordinate system.
- [var magnitude: CGFloat](uigravitybehavior/magnitude.md)
  The magnitude of the gravity vector.
- [func setAngle(CGFloat, magnitude: CGFloat)](uigravitybehavior/setangle(_:magnitude:).md)
  Sets the angle and magnitude of the gravity vector for the behavior.

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

- [class UIDynamicBehavior](uidynamicbehavior.md)
  An object that confers a behavioral configuration on one or more dynamic items, for their participation in 2D animation.
- [class UIAttachmentBehavior](uiattachmentbehavior.md)
  A relationship between two dynamic items, or between a dynamic item and an anchor point.
- [class UICollisionBehavior](uicollisionbehavior.md)
  An object that confers to a specified array of dynamic items the ability to engage in collisions with each other and with the behavior’s specified boundaries.
- [class UIFieldBehavior](uifieldbehavior.md)
  An object that applies field-based physics to dynamic items.
- [class UIPushBehavior](uipushbehavior.md)
  A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.
- [class UISnapBehavior](uisnapbehavior.md)
  A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/uigravitybehavior)*