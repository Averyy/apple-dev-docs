# NSPanGestureRecognizer

**Framework**: AppKit  
**Kind**: class

A continuous gesture recognizer for panning gestures.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSPanGestureRecognizer
```

#### Overview

The gesture is recognized when the user clicks all of specified buttons, drags the mouse, and releases one or more of the buttons. Use the pan gesture recognizer object to retrieve the distance traveled during the pan and the location of the mouse as it pans.

Upon creation, the gesture recognizer is configured to recognize pan gestures involving only the primary button. It also delays sending primary button events to the view by setting the [`delaysPrimaryMouseButtonEvents`](nsgesturerecognizer/delaysprimarymousebuttonevents.md) property to [`true`](https://developer.apple.com/documentation/swift/true). To change the set of buttons to track, modify the [`buttonMask`](nspangesturerecognizer/buttonmask.md) property.

In this gesture recognizer, the [`location(in:)`](nsgesturerecognizer/location(in:).md) method always reports the current mouse point, which changes as the user drags the mouse.

## Topics

### Configuring the Gesture Recognizer
- [var buttonMask: Int](nspangesturerecognizer/buttonmask.md)
  A bit mask of the button (or buttons) required to recognize this gesture.
- [var numberOfTouchesRequired: Int](nspangesturerecognizer/numberoftouchesrequired.md)
  The number of necessary touches on a Touch Bar for the gesture recognizer to match.
### Tracking the Location and Velocity of the Gesture
- [func translation(in: NSView?) -> NSPoint](nspangesturerecognizer/translation(in:).md)
  The distance traveled by the mouse during the gesture.
- [func setTranslation(NSPoint, in: NSView?)](nspangesturerecognizer/settranslation(_:in:).md)
  Changes the current translation value of the gesture recognizer.
- [func velocity(in: NSView?) -> NSPoint](nspangesturerecognizer/velocity(in:).md)
  The velocity of the pan, measured in points per second.

## Relationships

### Inherits From
- [NSGestureRecognizer](nsgesturerecognizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSClickGestureRecognizer](nsclickgesturerecognizer.md)
  A discrete gesture recognizer that tracks a specified number of mouse clicks.
- [class NSPressGestureRecognizer](nspressgesturerecognizer.md)
  A discrete gesture recognizer that tracks whether the user holds down a mouse button for a minimum amount of time before releasing it.
- [class NSRotationGestureRecognizer](nsrotationgesturerecognizer.md)
  A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.
- [class NSMagnificationGestureRecognizer](nsmagnificationgesturerecognizer.md)
  A continuous gesture recognizer that tracks a pinch gesture that magnifies content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer)*