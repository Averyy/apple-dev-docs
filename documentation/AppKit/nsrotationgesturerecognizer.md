# NSRotationGestureRecognizer

**Framework**: AppKit  
**Kind**: class

A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSRotationGestureRecognizer
```

#### Overview

This rotation gesture implies that the underlying view should rotate in a matching direction. The gesture is recognized when the trackpad touches end.

Upon creation, the gesture recognizer sets the value of the [`delaysRotationEvents`](nsgesturerecognizer/delaysrotationevents.md) property to [`true`](https://developer.apple.com/documentation/swift/true).

## Topics

### Interpreting the Gesture
- [var rotation: CGFloat](nsrotationgesturerecognizer/rotation.md)
  The rotation of the gesture in radians.
- [var rotationInDegrees: CGFloat](nsrotationgesturerecognizer/rotationindegrees.md)
  The rotation of the gesture in degrees.

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
- [class NSPressGestureRecognizer](nspressgesturerecognizer.md)
  A discrete gesture recognizer that tracks whether the user holds down a mouse button for a minimum amount of time before releasing it.
- [class NSPanGestureRecognizer](nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
- [class NSMagnificationGestureRecognizer](nsmagnificationgesturerecognizer.md)
  A continuous gesture recognizer that tracks a pinch gesture that magnifies content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrotationgesturerecognizer)*