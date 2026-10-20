# NSMagnificationGestureRecognizer

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A continuous gesture recognizer that tracks a pinch gesture that magnifies content.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSMagnificationGestureRecognizer
```

```objc
@interface NSMagnificationGestureRecognizer : NSGestureRecognizer
```

#### Overview

This object tracks pinch gestures on a track pad or other input device and stores the resulting magnification value for you to use in your code.

This gesture recognizer automatically sets the value of the [`delaysMagnificationEvents`](./nsgesturerecognizer/delaysmagnificationevents.md) property to [`true`](../Swift/true.md).

## Topics

### Finding the magnification factor
- [var magnification: CGFloat](./nsmagnificationgesturerecognizer/magnification.md)
  The amount of magnification to apply.

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
- [class NSClickGestureRecognizer](./nsclickgesturerecognizer.md)
  A discrete gesture recognizer that tracks a specified number of mouse clicks.
- [class NSPressGestureRecognizer](./nspressgesturerecognizer.md)
  A discrete gesture recognizer that tracks whether the user holds down a mouse button for a minimum amount of time before releasing it.
- [class NSPanGestureRecognizer](./nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
- [class NSRotationGestureRecognizer](./nsrotationgesturerecognizer.md)
  A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmagnificationgesturerecognizer)*