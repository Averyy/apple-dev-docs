# NSPressGestureRecognizer

**Framework**: AppKit  
**Kind**: class

A discrete gesture recognizer that tracks whether the user holds down a mouse button for a minimum amount of time before releasing it.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSPressGestureRecognizer
```

#### Overview

Use a press gesture recognizer to configure which button the user must hold and the length of time they must hold it. You can also specify how far the mouse can move for a valid gesture.

Upon creation, the gesture recognizer recognizes press gestures involving only the primary button. It also delays sending primary button events to the view by setting the [`delaysPrimaryMouseButtonEvents`](nsgesturerecognizer/delaysprimarymousebuttonevents.md) property to [`true`](https://developer.apple.com/documentation/swift/true). To change the set of buttons to track, modify the [`buttonMask`](nspressgesturerecognizer/buttonmask.md) property.

## Topics

### Configuring the Gesture Recognizer
- [var allowableMovement: CGFloat](nspressgesturerecognizer/allowablemovement.md)
  The maximum movement of the mouse in the view before the gesture fails.
- [var buttonMask: Int](nspressgesturerecognizer/buttonmask.md)
  A bit mask of the buttons required to recognize this press.
- [var minimumPressDuration: TimeInterval](nspressgesturerecognizer/minimumpressduration.md)
  The minimum time (in seconds) that the user must hold the mouse button in the view for a valid gesture.
- [var numberOfTouchesRequired: Int](nspressgesturerecognizer/numberoftouchesrequired.md)
  The number of necessary touches on a Touch Bar for the gesture recognizer to match.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSClickGestureRecognizer](nsclickgesturerecognizer.md)
  A discrete gesture recognizer that tracks a specified number of mouse clicks.
- [class NSPanGestureRecognizer](nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
- [class NSRotationGestureRecognizer](nsrotationgesturerecognizer.md)
  A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.
- [class NSMagnificationGestureRecognizer](nsmagnificationgesturerecognizer.md)
  A continuous gesture recognizer that tracks a pinch gesture that magnifies content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer)*