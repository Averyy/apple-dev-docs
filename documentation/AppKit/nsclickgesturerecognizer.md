# NSClickGestureRecognizer

**Framework**: AppKit  
**Kind**: class

A discrete gesture recognizer that tracks a specified number of mouse clicks.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSClickGestureRecognizer
```

#### Overview

When configuring this gesture recognizer, you can specify which mouse buttons must be clicked and how many clicks must occur before the action method is called. The user must click the specified mouse button the required number of times without dragging the mouse for the gesture to be recognized.

The gesture recognizer automatically sets the values of the [`delaysPrimaryMouseButtonEvents`](nsgesturerecognizer/delaysprimarymousebuttonevents.md), [`delaysSecondaryMouseButtonEvents`](nsgesturerecognizer/delayssecondarymousebuttonevents.md), and [`delaysOtherMouseButtonEvents`](nsgesturerecognizer/delaysothermousebuttonevents.md) properties to [`true`](https://developer.apple.com/documentation/swift/true) for each button in the [`buttonMask`](nsclickgesturerecognizer/buttonmask.md) property.

## Topics

### Configuring the Gesture
- [var buttonMask: Int](nsclickgesturerecognizer/buttonmask.md)
  A bit mask of the button (or buttons) required to recognize this click.
- [var numberOfClicksRequired: Int](nsclickgesturerecognizer/numberofclicksrequired.md)
  The number of clicks required to match.
- [var numberOfTouchesRequired: Int](nsclickgesturerecognizer/numberoftouchesrequired.md)
  The number of touches required in an [`NSTouchBar`](nstouchbar.md) object for the gesture recognizer to match.

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

## See Also

- [class NSPressGestureRecognizer](nspressgesturerecognizer.md)
  A discrete gesture recognizer that tracks whether the user holds down a mouse button for a minimum amount of time before releasing it.
- [class NSPanGestureRecognizer](nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
- [class NSRotationGestureRecognizer](nsrotationgesturerecognizer.md)
  A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.
- [class NSMagnificationGestureRecognizer](nsmagnificationgesturerecognizer.md)
  A continuous gesture recognizer that tracks a pinch gesture that magnifies content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclickgesturerecognizer)*