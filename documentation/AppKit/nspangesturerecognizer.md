# NSPanGestureRecognizer

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A continuous gesture recognizer for panning gestures.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSPanGestureRecognizer
```

```objc
@interface NSPanGestureRecognizer : NSGestureRecognizer
```

## Mentions

- [Adopting gesture recognizers in your app](./adopting-gesture-recognizers-in-your-app.md)
- [Handling AppKit gestures](./handling-appkit-gestures.md)

## Overview

The gesture is recognized when the user clicks all of specified buttons, drags the mouse, and releases one or more of the buttons. Use the pan gesture recognizer object to retrieve the distance traveled during the pan and the location of the mouse as it pans.

Upon creation, the gesture recognizer is configured to recognize pan gestures involving only the primary button. It also delays sending primary button events to the view by setting the [`delaysPrimaryMouseButtonEvents`](./nsgesturerecognizer/delaysprimarymousebuttonevents.md) property to [`true`](../Swift/true.md). To change the set of buttons to track, modify the [`buttonMask`](./nspangesturerecognizer/buttonmask.md) property.

In this gesture recognizer, the [`location(in:)`](./nsgesturerecognizer/location%28in%29.md) method always reports the current mouse point, which changes as the user drags the mouse.

## Topics

### Configuring the gesture recognizer
- [var buttonMask: Int](./nspangesturerecognizer/buttonmask.md)
  A bit mask of the button (or buttons) required to recognize this gesture.
### Setting the number of touches
- [var maximumNumberOfTouches: Int](./nspangesturerecognizer/maximumnumberoftouches.md)
  The maximum number of touches allowed to recognize this gesture
- [var minimumNumberOfTouches: Int](./nspangesturerecognizer/minimumnumberoftouches.md)
  The minimum number of touches needed to recognize this gesture
- [var numberOfTouchesRequired: Int](./nspangesturerecognizer/numberoftouchesrequired.md)
  The number of necessary touches on a Touch Bar for the gesture recognizer to match.
### Tracking the location and velocity of the gesture
- [func translation(in: NSView?) -> NSPoint](./nspangesturerecognizer/translation%28in%29.md)
  The distance traveled by the mouse during the gesture.
- [func setTranslation(NSPoint, in: NSView?)](./nspangesturerecognizer/settranslation%28_,in%29.md)
  Changes the current translation value of the gesture recognizer.
- [func velocity(in: NSView?) -> NSPoint](./nspangesturerecognizer/velocity%28in%29.md)
  The velocity of the pan, measured in points per second.

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
- [class NSPressGestureRecognizer](./nspressgesturerecognizer.md)
  A discrete gesture recognizer that tracks whether the user holds down a mouse button for a minimum amount of time before releasing it.
- [class NSRotationGestureRecognizer](./nsrotationgesturerecognizer.md)
  A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.
- [class NSMagnificationGestureRecognizer](./nsmagnificationgesturerecognizer.md)
  A continuous gesture recognizer that tracks a pinch gesture that magnifies content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer)*