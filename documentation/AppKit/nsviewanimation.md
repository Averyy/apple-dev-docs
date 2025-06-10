# NSViewAnimation

**Framework**: AppKit  
**Kind**: class

An animation of an app’s views, limited to changes in frame location and size, and to fade-in and fade-out effects.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSViewAnimation
```

#### Overview

An [`NSViewAnimation`](nsviewanimation.md) object takes an array of dictionaries from which it determines the objects to animate and the effects to apply to them. Each dictionary must have a target object and, optionally, properties that specify beginning and ending frame and whether to fade in or fade out. (See [`NSViewAnimation.Key`](nsviewanimation/key.md) for further information.) Animations with [`NSViewAnimation`](nsviewanimation.md) are, by default, in non-blocking mode over a duration of 0.5 seconds using the ease in-out animation curve. But you can configure the animation to have any duration, curve, frame rate, and blocking mode. You may also set progress marks, assign a delegate, and implement delegation methods in order to animate view and windows concurrent with the ones specified as targets in the view-animation dictionary.

Invoking the [`NSAnimation`](nsanimation.md) [`stop()`](nsanimation/stop().md) method on a running [`NSViewAnimation`](nsviewanimation.md) object moves the animation to the end frame.

## Topics

### Initializing an NSViewAnimation object
- [init(viewAnimations: [[NSViewAnimation.Key : Any]])](nsviewanimation/init(viewanimations:).md)
  Returns an `NSViewAnimation` object initialized with the supplied information.
### Getting and setting view-animation dictionaries
- [var viewAnimations: [[NSViewAnimation.Key : Any]]](nsviewanimation/viewanimations.md)
  The dictionaries defining the objects to animate.
- [NSViewAnimation.Key](nsviewanimation/key.md)
  The following string constants are keys for the dictionaries in the array passed into [`init(viewAnimations:)`](nsviewanimation/init(viewanimations:).md) and [`viewAnimations`](nsviewanimation/viewanimations.md).
- [NSViewAnimation.EffectName](nsviewanimation/effectname.md)
  The following constants specify the animation effect to apply and are used as values for the animation effect property of the animation view. See the description of [`effect`](nsviewanimation/key/effect.md) for usage details.

## Relationships

### Inherits From
- [NSAnimation](nsanimation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
  A set of methods that defines a way to add animation to an existing class with a minimum of API impact.
- [class NSAnimationContext](nsanimationcontext.md)
  An animation context, which contains information about environment and state.
- [NSAnimation.Progress](nsanimation/progress.md)
  The animation progress, as a floating-point number between `0.0` and `1.0`.
- [enum NSAnimationEffect](nsanimationeffect.md)
  The type for standard system animation effects, which include both display and sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation)*