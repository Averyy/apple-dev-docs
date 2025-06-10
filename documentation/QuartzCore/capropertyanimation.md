# CAPropertyAnimation

**Framework**: Core Animation  
**Kind**: class

An abstract subclass for creating animations that manipulate the value of layer properties.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAPropertyAnimation
```

#### Overview

The property to animate is specified using a key path that is relative to the layer using the animation.

You do not create instances of [`CAPropertyAnimation`](capropertyanimation.md): to animate the properties of a Core Animation layer, create instance of the concrete subclasses [`CABasicAnimation`](cabasicanimation.md) or [`CAKeyframeAnimation`](cakeyframeanimation.md).

## Topics

### Animated Key Path
- [var keyPath: String?](capropertyanimation/keypath.md)
  Specifies the key path the receiver animates.
### Property Value Calculation Behavior
- [var isCumulative: Bool](capropertyanimation/iscumulative.md)
  Determines if the value of the property is the value at the end of the previous repeat cycle, plus the value of the current repeat cycle.
- [var isAdditive: Bool](capropertyanimation/isadditive.md)
  Determines if the value specified by the animation is added to the current render tree value to produce the new render tree value.
- [var valueFunction: CAValueFunction?](capropertyanimation/valuefunction.md)
  An optional value function that is applied to interpolated values.
### Creating an Animation
- [convenience init(keyPath: String?)](capropertyanimation/init(keypath:).md)
  Creates and returns an `CAPropertyAnimation` instance for the specified key path.

## Relationships

### Inherits From
- [CAAnimation](caanimation.md)
### Inherited By
- [CABasicAnimation](cabasicanimation.md)
- [CAKeyframeAnimation](cakeyframeanimation.md)
### Conforms To
- [CAAction](caaction.md)
- [CAMediaTiming](camediatiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CAAnimation](caanimation.md)
  The abstract superclass for animations in Core Animation.
- [protocol CAAnimationDelegate](caanimationdelegate.md)
  Methods your app can implement to respond when animations start and stop.
- [class CABasicAnimation](cabasicanimation.md)
  An object that provides basic, single-keyframe animation capabilities for a layer property.
- [class CAKeyframeAnimation](cakeyframeanimation.md)
  An object that provides keyframe animation capabilities for a layer object.
- [class CASpringAnimation](caspringanimation.md)
  An animation that applies a spring-like force to a layer’s properties.
- [class CATransition](catransition.md)
  An object that provides an animated transition between a layer’s states.
- [class CAValueFunction](cavaluefunction.md)
  An object that provides a flexible method of defining animated transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/capropertyanimation)*