# CATransition

**Framework**: Core Animation  
**Kind**: class

An object that provides an animated transition between a layer’s states.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CATransition
```

#### Overview

You can transition between a layer’s states by creating and adding a [`CATransition`](catransition.md) object to it. The default transition is a cross fade, but you can specify different effects from a set of predefined transitions.

The following code shows how you can transition between the two states of a [`CATextLayer`](catextlayer.md) named `transitioningLayer`. When the layer is first created, its [`backgroundColor`](calayer/backgroundcolor.md) is set to red and its [`string`](catextlayer/string.md) property is set to `Red`. When the `runTransition()` function is called, a new [`CATransition`](catransition.md) object is created and added to `transitioningLayer`, and the state of the layer is changed so that its background color is blue and its rendered text reads `Blue`.

The end result is that the push transition animates the red state from left to right with the blue state entering the scene from the left.

```swift
let transitioningLayer = CATextLayer()
     
override func viewDidLoad() {
    super.viewDidLoad()
    transitioningLayer.frame = CGRect(x: 10, y: 10,
                                      width: 320, height: 160)
    
    view.layer.addSublayer(transitioningLayer)
    
    // Initial "red" state
    transitioningLayer.backgroundColor = UIColor.red.cgColor
    transitioningLayer.string = "Red"
}
      
   
func runTransition() {
    let transition = CATransition()
    transition.duration = 2
    
    transition.type = kCATransitionPush
    
    transitioningLayer.add(transition,
                           forKey: "transition")
    
    // Transition to "blue" state
    transitioningLayer.backgroundColor = UIColor.blue.cgColor
    transitioningLayer.string = "Blue"
}
```

## Topics

### Transition start and end point
- [var startProgress: Float](catransition/startprogress.md)
  Indicates the start point of the receiver as a fraction of the entire transition.
- [var endProgress: Float](catransition/endprogress.md)
  Indicates the end point of the receiver as a fraction of the entire transition.
### Transition Properties
- [var type: CATransitionType](catransition/type.md)
  Specifies the predefined transition type.
- [var subtype: CATransitionSubtype?](catransition/subtype.md)
  Specifies an optional subtype that indicates the direction for the predefined motion-based transitions.
### Custom transition filter
- [var filter: Any?](catransition/filter.md)
  An optional Core Image filter object that provides the transition.
### Constants
- [Common Transition Types](common-transition-types.md)
  These constants specify the transition types that can be used with the [`type`](catransition/type.md) property.
- [Common Transition Subtypes](common-transition-subtypes.md)
  These constants specify the direction of motion-based transitions. They are used with the [`subtype`](catransition/subtype.md) property.

## Relationships

### Inherits From
- [CAAnimation](caanimation.md)
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
- [class CAKeyframeAnimation](cakeyframeanimation.md)
  An object that provides keyframe animation capabilities for a layer object.
- [class CASpringAnimation](caspringanimation.md)
  An animation that applies a spring-like force to a layer’s properties.
- [class CAValueFunction](cavaluefunction.md)
  An object that provides a flexible method of defining animated transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransition)*