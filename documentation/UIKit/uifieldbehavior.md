# UIFieldBehavior

**Framework**: UIKit  
**Kind**: class

An object that applies field-based physics to dynamic items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIFieldBehavior
```

#### Overview

A field behavior defines an area in which forces such as gravity, magnetism, drag, velocity, turbulence, and others can be applied. After creating a field behavior object of the appropriate type, configure the strength of the intended force along with any other field attributes.

After creating a field behavior object, call the [`addItem(_:)`](uifieldbehavior/additem(_:).md) method to associate the field with that item. For many types of fields, you must also configure a [`UIDynamicItemBehavior`](uidynamicitembehavior.md) object for the item to define relevant attributes of the item such as its density (mass) or charge. After configuring the field, add it to the [`UIDynamicAnimator`](uidynamicanimator.md) object associated with your interface to begin the animations.

The [`position`](uifieldbehavior/position.md) of a field defines its location in your interface and the field’s [`region`](uifieldbehavior/region.md) defines its area of influence. The region you specify is centered on the field’s position. Regions can be circular or rectangular, and you can combine regions in different ways to create more complex region shapes.

Most fields use only a subset of the field attributes in their computations. All fields have a [`strength`](uifieldbehavior/strength.md) value that helps define the intensity of the field. Most fields also use the [`falloff`](uifieldbehavior/falloff.md) property to vary the field strength over distance. You configure other attributes only as needed for the type of field.

## Topics

### Getting the field behaviors
- [class func dragField() -> Self](uifieldbehavior/dragfield.md)
  Creates and returns a field behavior for slowing an object’s velocity.
- [class func springField() -> Self](uifieldbehavior/springfield.md)
  Creates and returns a spring field behavior.
- [class func velocityField(direction: CGVector) -> Self](uifieldbehavior/velocityfield(direction:).md)
  Creates and returns a field behavior object that applies a directional velocity to items.
- [class func electricField() -> Self](uifieldbehavior/electricfield.md)
  Creates and returns a field behavior object that interacts with charged items.
- [class func magneticField() -> Self](uifieldbehavior/magneticfield.md)
  Creates and returns a field behavior that interacts with charged items.
- [class func radialGravityField(position: CGPoint) -> Self](uifieldbehavior/radialgravityfield(position:).md)
  Creates and returns a field behavior object that models a radial gravitational force.
- [class func linearGravityField(direction: CGVector) -> Self](uifieldbehavior/lineargravityfield(direction:).md)
  Creates and returns a field behavior object that models a linear gravitational force.
- [class func vortexField() -> Self](uifieldbehavior/vortexfield.md)
  Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [class func noiseField(smoothness: CGFloat, animationSpeed: CGFloat) -> Self](uifieldbehavior/noisefield(smoothness:animationspeed:).md)
  Creates and returns a field behavior object that applies random noise to other forces.
- [class func turbulenceField(smoothness: CGFloat, animationSpeed: CGFloat) -> Self](uifieldbehavior/turbulencefield(smoothness:animationspeed:).md)
  Creates and returns a field behavior object that applies noise to an item in motion.
- [class func field(evaluationBlock: (UIFieldBehavior, CGPoint, CGVector, CGFloat, CGFloat, TimeInterval) -> CGVector) -> Self](uifieldbehavior/field(evaluationblock:).md)
  Creates and returns a field behavior object that applies an app-specified field to items.
### Managing the associated dynamic items
- [func addItem(any UIDynamicItem)](uifieldbehavior/additem(_:).md)
  Associates the field behavior with the specified dynamic item.
- [func removeItem(any UIDynamicItem)](uifieldbehavior/removeitem(_:).md)
  Removes the field behavior from the specified dynamic item.
- [var items: [any UIDynamicItem]](uifieldbehavior/items.md)
  The dynamic items associated with the current field behavior.
### Configuring the field attributes
- [var position: CGPoint](uifieldbehavior/position.md)
  The position of the field in the reference coordinate system.
- [var region: UIRegion](uifieldbehavior/region.md)
  The shape of the field.
- [var strength: CGFloat](uifieldbehavior/strength.md)
  The strength of the field.
- [var falloff: CGFloat](uifieldbehavior/falloff.md)
  The rate of decay for the field strength.
- [var minimumRadius: CGFloat](uifieldbehavior/minimumradius.md)
  The minimum distance at which to start calculating new values for the field.
- [var direction: CGVector](uifieldbehavior/direction.md)
  The direction of motion for a linear field.
- [var smoothness: CGFloat](uifieldbehavior/smoothness.md)
  The smoothness of the noise used to generate the field.
- [var animationSpeed: CGFloat](uifieldbehavior/animationspeed.md)
  The rate at which the animation should proceed.

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
- [class UIGravityBehavior](uigravitybehavior.md)
  An object that applies a gravity-like force to all of its associated dynamic items.
- [class UIPushBehavior](uipushbehavior.md)
  A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.
- [class UISnapBehavior](uisnapbehavior.md)
  A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior)*