# CABasicAnimation

**Framework**: Core Animation  
**Kind**: class

An object that provides basic, single-keyframe animation capabilities for a layer property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CABasicAnimation
```

#### Overview

You create an instance of  [`CABasicAnimation`](cabasicanimation.md) using the inherited [`init(keyPath:)`](capropertyanimation/init(keypath:).md) method, specifying the key path of the property to be animated in the render tree.

For example, you can animate a layer’s scalar (i.e. containing a single value) properties such as its [`opacity`](calayer/opacity.md). The following code fades in a layer by animating its opacity from `0` to `1`.

```swift
let animation = CABasicAnimation(keyPath: "opacity") 
animation.fromValue = 0 
animation.toValue = 1
```

Non-scalar properties, such as [`backgroundColor`](calayer/backgroundcolor.md), can also be animated. Core Animation will interpolate between the [`fromValue`](cabasicanimation/fromvalue.md) color and the [`toValue`](cabasicanimation/tovalue.md) color. The animation created in the following code fades a layer’s background color from red to blue.

```swift
let animation = CABasicAnimation(keyPath: "backgroundColor")
animation.fromValue = NSColor.red.cgColor
animation.toValue = NSColor.blue.cgColor
```

If you want to animate the individual components of a non-scalar property with different values, you pass the values to [`toValue`](cabasicanimation/tovalue.md) and [`fromValue`](cabasicanimation/fromvalue.md) as arrays. The following animation moves a layer from `(0, 0)` to `(100, 100)`.

```swift
let animation = CABasicAnimation(keyPath: "position")
animation.fromValue = [0, 0]
animation.toValue = [100, 100]
```

The `keyPath` can access the individual components of a property. For example, the following animation stretches a layer by animating its [`transform`](calayer/transform.md) object’s `x` from `1` to `2`.

```swift
let animation = CABasicAnimation(keyPath: "transform.scale.x")
animation.fromValue = 1
animation.toValue = 2
```

##### Setting Interpolation Values

The [`fromValue`](cabasicanimation/fromvalue.md), [`byValue`](cabasicanimation/byvalue.md) and [`toValue`](cabasicanimation/tovalue.md) properties define the values being interpolated between. All are optional, and no more than two should be non-`nil`. The object type should match the type of the property being animated.

The interpolation values are used as follows:

- Both [`fromValue`](cabasicanimation/fromvalue.md) and [`toValue`](cabasicanimation/tovalue.md) are non-`nil`. Interpolates between [`fromValue`](cabasicanimation/fromvalue.md) and [`toValue`](cabasicanimation/tovalue.md).
- [`fromValue`](cabasicanimation/fromvalue.md) and [`byValue`](cabasicanimation/byvalue.md) are non-`nil`. Interpolates between [`fromValue`](cabasicanimation/fromvalue.md) and ([`fromValue`](cabasicanimation/fromvalue.md) + [`byValue`](cabasicanimation/byvalue.md)).
- [`byValue`](cabasicanimation/byvalue.md) and [`toValue`](cabasicanimation/tovalue.md) are non-`nil`. Interpolates between ([`toValue`](cabasicanimation/tovalue.md) - [`byValue`](cabasicanimation/byvalue.md)) and [`toValue`](cabasicanimation/tovalue.md).
- [`fromValue`](cabasicanimation/fromvalue.md) is non-`nil`. Interpolates between [`fromValue`](cabasicanimation/fromvalue.md) and the current presentation value of the property.
- [`toValue`](cabasicanimation/tovalue.md) is non-`nil`. Interpolates between the current value of `keyPath` in the target layer’s presentation layer and [`toValue`](cabasicanimation/tovalue.md).
- [`byValue`](cabasicanimation/byvalue.md) is non-`nil`. Interpolates between the current value of `keyPath` in the target layer’s presentation layer and that value plus [`byValue`](cabasicanimation/byvalue.md).
- All properties are `nil`. Interpolates between the previous value of `keyPath` in the target layer’s presentation layer and the current value of  `keyPath` in the target layer’s presentation layer.

## Topics

### Interpolation values
- [var fromValue: Any?](cabasicanimation/fromvalue.md)
  Defines the value the receiver uses to start interpolation.
- [var toValue: Any?](cabasicanimation/tovalue.md)
  Defines the value the receiver uses to end interpolation.
- [var byValue: Any?](cabasicanimation/byvalue.md)
  Defines the value the receiver uses to perform relative interpolation.

## Relationships

### Inherits From
- [CAPropertyAnimation](capropertyanimation.md)
### Inherited By
- [CASpringAnimation](caspringanimation.md)
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
- [class CAPropertyAnimation](capropertyanimation.md)
  An abstract subclass for creating animations that manipulate the value of layer properties.
- [class CAKeyframeAnimation](cakeyframeanimation.md)
  An object that provides keyframe animation capabilities for a layer object.
- [class CASpringAnimation](caspringanimation.md)
  An animation that applies a spring-like force to a layer’s properties.
- [class CATransition](catransition.md)
  An object that provides an animated transition between a layer’s states.
- [class CAValueFunction](cavaluefunction.md)
  An object that provides a flexible method of defining animated transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cabasicanimation)*