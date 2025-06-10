# CAKeyframeAnimation

**Framework**: Core Animation  
**Kind**: class

An object that provides keyframe animation capabilities for a layer object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAKeyframeAnimation
```

#### Overview

You create a [`CAKeyframeAnimation`](cakeyframeanimation.md) object using the inherited [`init(keyPath:)`](capropertyanimation/init(keypath:).md) method, specifying the key path of the property that you want to animate on the layer. You can then specify the keyframe values to use to control the timing and animation behavior.

For most types of animations, you specify the keyframe values using the [`values`](cakeyframeanimation/values.md) and [`keyTimes`](cakeyframeanimation/keytimes.md) properties. During the animation, Core Animation generates intermediate values by interpolating between the values you provide. When animating a value that is a coordinate point, such as the layer’s position, you can specify a [`path`](cakeyframeanimation/path.md) for that point to follow instead of individual values. The pacing of the animation is controlled by the timing information you provide.

The following code shows how to create a keyframe animation that animates a layer’s background color from red to green to blue over a two second duration.

```swift
let colorKeyframeAnimation = CAKeyframeAnimation(keyPath: "backgroundColor")

colorKeyframeAnimation.values = [UIColor.red.cgColor,
                                 UIColor.green.cgColor,
                                 UIColor.blue.cgColor]
colorKeyframeAnimation.keyTimes = [0, 0.5, 1]
colorKeyframeAnimation.duration = 2
```

## Topics

### Providing keyframe values
- [var values: [Any]?](cakeyframeanimation/values.md)
  An array of objects that specify the keyframe values to use for the animation.
- [var path: CGPath?](cakeyframeanimation/path.md)
  The path for a point-based property to follow.
### Keyframe timing
- [var keyTimes: [NSNumber]?](cakeyframeanimation/keytimes.md)
  An optional array of `NSNumber` objects that define the time at which to apply a given keyframe segment.
- [var timingFunctions: [CAMediaTimingFunction]?](cakeyframeanimation/timingfunctions.md)
  An optional array of `CAMediaTimingFunction` objects that define the pacing for each keyframe segment.
- [var calculationMode: CAAnimationCalculationMode](cakeyframeanimation/calculationmode.md)
  Specifies how intermediate keyframe values are calculated by the receiver.
### Rotation Mode Attribute
- [var rotationMode: CAAnimationRotationMode?](cakeyframeanimation/rotationmode.md)
  Determines whether objects animating along the path rotate to match the path tangent.
### Cubic Mode Attributes
- [var tensionValues: [NSNumber]?](cakeyframeanimation/tensionvalues.md)
  An array of numbers that define the tightness of the curve.
- [var continuityValues: [NSNumber]?](cakeyframeanimation/continuityvalues.md)
  An array of numbers that define the sharpness of the timing curve’s corners.
- [var biasValues: [NSNumber]?](cakeyframeanimation/biasvalues.md)
  An array of numbers that define the position of the curve relative to a control point.
### Constants
- [Rotation Mode Values](rotation-mode-values.md)
  These constants are used by the [`rotationMode`](cakeyframeanimation/rotationmode.md) property.
- [Value calculation modes](value-calculation-modes.md)
  These constants are used by the [`calculationMode`](cakeyframeanimation/calculationmode.md) property.

## Relationships

### Inherits From
- [CAPropertyAnimation](capropertyanimation.md)
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
- [class CABasicAnimation](cabasicanimation.md)
  An object that provides basic, single-keyframe animation capabilities for a layer property.
- [class CASpringAnimation](caspringanimation.md)
  An animation that applies a spring-like force to a layer’s properties.
- [class CATransition](catransition.md)
  An object that provides an animated transition between a layer’s states.
- [class CAValueFunction](cavaluefunction.md)
  An object that provides a flexible method of defining animated transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation)*