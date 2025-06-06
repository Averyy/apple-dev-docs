# NSMagnificationGestureRecognizer

**Framework**: AppKit  
**Kind**: class

A continuous gesture recognizer that tracks a pinch gesture that magnifies content.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSMagnificationGestureRecognizer
```

#### Overview

This object tracks pinch gestures on a track pad or other input device and stores the resulting magnification value for you to use in your code.

This gesture recognizer automatically sets the value of the [`delaysMagnificationEvents`](nsgesturerecognizer/delaysmagnificationevents.md) property to [`true`](https://developer.apple.com/documentation/swift/true).

## Topics

### Finding the Magnification Factor
- [var magnification: CGFloat](nsmagnificationgesturerecognizer/magnification.md)
  The amount of magnification to apply.

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
- [class NSPanGestureRecognizer](nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
- [class NSRotationGestureRecognizer](nsrotationgesturerecognizer.md)
  A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmagnificationgesturerecognizer)*