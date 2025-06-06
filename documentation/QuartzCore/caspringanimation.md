# CASpringAnimation

**Framework**: Core Animation  
**Kind**: class

An animation that applies a spring-like force to a layer’s properties.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CASpringAnimation
```

#### Overview

You would typically use a spring animation to animate a layer’s position so that it appears to be pulled towards a target by a spring. The further the layer is from the target, the greater the acceleration towards it is.

[`CASpringAnimation`](caspringanimation.md) allows control over physically based attributes such as the spring’s damping and stiffness.

You can use a spring animation to animation properties of a layer other than its position. The following code shows how to create a spring animation that bounces a layer into view by animating its scale from `0` to `1`. Because the spring animation can overshoot its [`toValue`](cabasicanimation/tovalue.md), the animated layer may exceed its frame.

```swift
let springAnimation = CASpringAnimation(keyPath: "transform.scale")

springAnimation.fromValue = 0
springAnimation.toValue = 1
```

## Topics

### Configuring Physical Attributes
- [var damping: CGFloat](caspringanimation/damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
- [var initialVelocity: CGFloat](caspringanimation/initialvelocity.md)
  The initial velocity of the object attached to the spring.
- [var mass: CGFloat](caspringanimation/mass.md)
  The mass of the object attached to the end of the spring.
- [var settlingDuration: CFTimeInterval](caspringanimation/settlingduration.md)
  The estimated duration required for the spring system to be considered at rest.
- [var stiffness: CGFloat](caspringanimation/stiffness.md)
  The spring stiffness coefficient.
### Initializers
- [init(perceptualDuration: CFTimeInterval, bounce: CGFloat)](caspringanimation/init(perceptualduration:bounce:).md)
### Instance Properties
- [var allowsOverdamping: Bool](caspringanimation/allowsoverdamping.md)
- [var bounce: CGFloat](caspringanimation/bounce.md)
- [var perceptualDuration: CFTimeInterval](caspringanimation/perceptualduration.md)

## Relationships

### Inherits From
- [CABasicAnimation](cabasicanimation.md)
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

## See Also

- [class CAAnimation](caanimation.md)
  The abstract superclass for animations in Core Animation.
- [protocol CAAnimationDelegate](caanimationdelegate.md)
  Methods your app can implement to respond when animations start and stop.
- [class CAPropertyAnimation](capropertyanimation.md)
  An abstract subclass for creating animations that manipulate the value of layer properties.
- [class CABasicAnimation](cabasicanimation.md)
  An object that provides basic, single-keyframe animation capabilities for a layer property.
- [class CAKeyframeAnimation](cakeyframeanimation.md)
  An object that provides keyframe animation capabilities for a layer object.
- [class CATransition](catransition.md)
  An object that provides an animated transition between a layer’s states.
- [class CAValueFunction](cavaluefunction.md)
  An object that provides a flexible method of defining animated transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caspringanimation)*