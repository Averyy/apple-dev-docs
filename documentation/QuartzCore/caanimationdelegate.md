# CAAnimationDelegate

**Framework**: Core Animation  
**Kind**: protocol

Methods your app can implement to respond when animations start and stop.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol CAAnimationDelegate : NSObjectProtocol
```

#### Overview

You can use an animation delegate to execute additional logic when an animation starts or ends. For example, you may want to remove a layer from its parent once a fade out animation has completed.

The following example shows code taken from a class that implements [`CAAnimationDelegate`](caanimationdelegate.md) and has had a layer, named `sublayer`, added to its layer. The `fadeOut` function animates the opacity of `sublayer` and, once the animation has completed, [`animationDidStop(_:finished:)`](caanimationdelegate/animationdidstop(_:finished:).md) removes it from its superlayer.

```swift
func fadeOut() {
    let fadeOutAnimation = CABasicAnimation()
    fadeOutAnimation.keyPath = "opacity"
    fadeOutAnimation.fromValue = 1
    fadeOutAnimation.toValue = 0
    fadeOutAnimation.duration = 0.25
    
    fadeOutAnimation.delegate = self
    
    sublayer.add(fadeOutAnimation,
                      forKey: "fade")
}
    
func animationDidStop(_ anim: CAAnimation, finished flag: Bool) {
    sublayer.removeFromSuperlayer()
}
```

## Topics

### Customizing Start and Stop Times
- [func animationDidStart(CAAnimation)](caanimationdelegate/animationdidstart(_:).md)
  Tells the delegate the animation has started.
- [func animationDidStop(CAAnimation, finished: Bool)](caanimationdelegate/animationdidstop(_:finished:).md)
  Tells the delegate the animation has ended.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CAAnimation](caanimation.md)
  The abstract superclass for animations in Core Animation.
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
- [class CAValueFunction](cavaluefunction.md)
  An object that provides a flexible method of defining animated transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationdelegate)*