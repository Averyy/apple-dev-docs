# NSClickGestureRecognizer

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A discrete gesture recognizer that tracks a specified number of mouse clicks.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSClickGestureRecognizer
```

```objc
@interface NSClickGestureRecognizer : NSGestureRecognizer
```

## Overview

When configuring this gesture recognizer, you can specify which mouse buttons must be clicked and how many clicks must occur before the action method is called. The user must click the specified mouse button the required number of times without dragging the mouse for the gesture to be recognized.

The gesture recognizer automatically sets the values of the [`delaysPrimaryMouseButtonEvents`](./nsgesturerecognizer/delaysprimarymousebuttonevents.md), [`delaysSecondaryMouseButtonEvents`](./nsgesturerecognizer/delayssecondarymousebuttonevents.md), and [`delaysOtherMouseButtonEvents`](./nsgesturerecognizer/delaysothermousebuttonevents.md) properties to [`true`](../Swift/true.md) for each button in the [`buttonMask`](./nsclickgesturerecognizer/buttonmask.md) property.

## Topics

### Configuring the gesture
- [var buttonMask: Int](./nsclickgesturerecognizer/buttonmask.md)
  A bit mask of the button (or buttons) required to recognize this click.
- [var numberOfClicksRequired: Int](./nsclickgesturerecognizer/numberofclicksrequired.md)
  The number of clicks required to match.
- [var numberOfTouchesRequired: Int](./nsclickgesturerecognizer/numberoftouchesrequired.md)
  The number of touches required in an [`NSTouchBar`](./nstouchbar.md) object for the gesture recognizer to match.

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

### Standard Gestures
- [class NSPressGestureRecognizer](./nspressgesturerecognizer.md)
  A discrete gesture recognizer that tracks whether the user holds down a mouse button for a minimum amount of time before releasing it.
- [class NSPanGestureRecognizer](./nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
- [class NSRotationGestureRecognizer](./nsrotationgesturerecognizer.md)
  A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.
- [class NSMagnificationGestureRecognizer](./nsmagnificationgesturerecognizer.md)
  A continuous gesture recognizer that tracks a pinch gesture that magnifies content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclickgesturerecognizer)*