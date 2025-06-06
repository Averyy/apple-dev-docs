# CAValueFunction

**Framework**: Core Animation  
**Kind**: class

An object that provides a flexible method of defining animated transformations.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAValueFunction
```

#### Overview

You can use a value function to specify the individual components of an animated transform.

For example, to create a basic animation that rotates a layer from 0° to 180° around its z-axis, you would create a [`CABasicAnimation`](cabasicanimation.md) object with a [`fromValue`](cabasicanimation/fromvalue.md) of `0`, a [`toValue`](cabasicanimation/tovalue.md) of [`pi`](https://developer.apple.com/documentation/Swift/Float/pi), and a [`valueFunction`](capropertyanimation/valuefunction.md) of a [`CAValueFunction`](cavaluefunction.md) with a function name of [`rotateZ`](cavaluefunctionname/rotatez.md).

The following code shows how you would create such a rotation and apply it to a [`CALayer`](calayer.md) named `rotatingLayer`.

```swift
let rotateAnimation = CABasicAnimation()
rotateAnimation.valueFunction = CAValueFunction(name: kCAValueFunctionRotateZ)
rotateAnimation.fromValue = 0
rotateAnimation.toValue = Float.pi
rotateAnimation.duration = 3
rotatingLayer.add(rotateAnimation,
                  forKey: "transform")
```

The value functions [`scale`](cavaluefunctionname/scale.md) and [`translate`](cavaluefunctionname/translate.md) require 3 values, for the individual `x`, `y` and `z` components. When working with these value functions, you specify the animation’s [`fromValue`](cabasicanimation/fromvalue.md) and [`toValue`](cabasicanimation/tovalue.md) as arrays.

The following code shows how you could animate a layer’s scale from `0` to `1` using a value function.

```swift
let scaleAnimation = CABasicAnimation()
scaleAnimation.valueFunction = CAValueFunction(name: kCAValueFunctionScale)
scaleAnimation.fromValue = [0, 0, 0]
scaleAnimation.toValue = [1, 1, 1]
scaleAnimation.duration = 3
scalingLayer.add(scaleAnimation,
                 forKey: "transform")
```

## Topics

### Getting Value Function Properties
- [var name: CAValueFunctionName](cavaluefunction/name.md)
  Returns the name of the value function.
### Creating and Initializing Value Functions
- [convenience init?(name: CAValueFunctionName)](cavaluefunction/init(name:).md)
  Returns the value function object identified by the name.
### Constants
- [Rotate Value Functions](rotate-value-functions.md)
  Rotate value transform functions construct a 4x4 matrix that represents the corresponding rotation matrix.
- [Scale Value Functions](scale-value-functions.md)
  Scale value transform functions construct a 4x4 matrix that represents the corresponding scale matrix.
- [Translate Functions](translate-functions.md)
  Translate value transform functions construct a 4x4 matrix that represents the corresponding translate matrix.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
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
- [class CASpringAnimation](caspringanimation.md)
  An animation that applies a spring-like force to a layer’s properties.
- [class CATransition](catransition.md)
  An object that provides an animated transition between a layer’s states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cavaluefunction)*