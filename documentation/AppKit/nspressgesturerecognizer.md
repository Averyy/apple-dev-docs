# NSPressGestureRecognizer

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A discrete gesture recognizer that tracks whether the user holds down a mouse button for a minimum amount of time before releasing it.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSPressGestureRecognizer
```

```objc
@interface NSPressGestureRecognizer : NSGestureRecognizer
```

## Mentions

- [Adopting gesture recognizers in your app](./adopting-gesture-recognizers-in-your-app.md)
- [Handling AppKit gestures](./handling-appkit-gestures.md)

## Overview

Use a press gesture recognizer to configure which button the user must hold and the length of time they must hold it. You can also specify how far the mouse can move for a valid gesture.

Upon creation, the gesture recognizer recognizes press gestures involving only the primary button. It also delays sending primary button events to the view by setting the [`delaysPrimaryMouseButtonEvents`](./nsgesturerecognizer/delaysprimarymousebuttonevents.md) property to [`true`](../Swift/true.md). To change the set of buttons to track, modify the [`buttonMask`](./nspressgesturerecognizer/buttonmask.md) property.

## Topics

### Configuring the gesture recognizer
- [var allowableMovement: CGFloat](./nspressgesturerecognizer/allowablemovement.md)
  The maximum movement of the mouse in the view before the gesture fails.
- [var buttonMask: Int](./nspressgesturerecognizer/buttonmask.md)
  A bit mask of the buttons required to recognize this press.
- [var minimumPressDuration: TimeInterval](./nspressgesturerecognizer/minimumpressduration.md)
  The minimum time (in seconds) that the user must hold the mouse button in the view for a valid gesture.
- [var numberOfTouchesRequired: Int](./nspressgesturerecognizer/numberoftouchesrequired.md)
  The number of necessary touches on a Touch Bar for the gesture recognizer to match.

## Relationships

### Inherits From
- [NSGestureRecognizer](./nsgesturerecognizer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Standard gestures
- [class NSClickGestureRecognizer](./nsclickgesturerecognizer.md)
  A discrete gesture recognizer that tracks a specified number of mouse clicks.
- [class NSPanGestureRecognizer](./nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
- [class NSRotationGestureRecognizer](./nsrotationgesturerecognizer.md)
  A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.
- [class NSMagnificationGestureRecognizer](./nsmagnificationgesturerecognizer.md)
  A continuous gesture recognizer that tracks a pinch gesture that magnifies content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer)*