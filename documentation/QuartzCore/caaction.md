# CAAction

**Framework**: Core Animation  
**Kind**: protocol

An interface that allows instances to respond to actions triggered by a Core Animation layer change.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol CAAction
```

#### Overview

When queried with an action identifier (a key path, an external action name, or a predefined action identifier) a layer returns the appropriate action object–which must implement the [`CAAction`](caaction.md) protocol–and sends it a [`run(forKey:object:arguments:)`](caaction/run(forkey:object:arguments:).md) message.

## Topics

### Responding to an action
- [func run(forKey: String, object: Any, arguments: [AnyHashable : Any]?)](caaction/run(forkey:object:arguments:).md)
  Called to trigger the action specified by the identifier.

## Relationships

### Conforming Types
- [CAAnimation](caanimation.md)
- [CAAnimationGroup](caanimationgroup.md)
- [CABasicAnimation](cabasicanimation.md)
- [CAKeyframeAnimation](cakeyframeanimation.md)
- [CAPropertyAnimation](capropertyanimation.md)
- [CASpringAnimation](caspringanimation.md)
- [CATransition](catransition.md)

## See Also

- [class CALayer](calayer.md)
  An object that manages image-based content and allows you to perform animations on that content.
- [protocol CALayerDelegate](calayerdelegate.md)
  Methods your app can implement to respond to layer-related events.
- [class CAConstraint](caconstraint.md)
  A representation of a single layout constraint between two layers.
- [protocol CALayoutManager](calayoutmanager.md)
  Methods that allow an object to manage the layout of a layer and its sublayers.
- [class CAConstraintLayoutManager](caconstraintlayoutmanager.md)
  An object that provides a constraint-based layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caaction)*