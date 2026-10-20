# NSRotationGestureRecognizer

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSRotationGestureRecognizer
```

```objc
@interface NSRotationGestureRecognizer : NSGestureRecognizer
```

#### Overview

This rotation gesture implies that the underlying view should rotate in a matching direction. The gesture is recognized when the trackpad touches end.

Upon creation, the gesture recognizer sets the value of the [`delaysRotationEvents`](./nsgesturerecognizer/delaysrotationevents.md) property to [`true`](../Swift/true.md).

## Topics

### Interpreting the gesture
- [var rotation: CGFloat](./nsrotationgesturerecognizer/rotation.md)
  The rotation of the gesture in radians.
- [var rotationInDegrees: CGFloat](./nsrotationgesturerecognizer/rotationindegrees.md)
  The rotation of the gesture in degrees.

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
- [class NSMagnificationGestureRecognizer](./nsmagnificationgesturerecognizer.md)
  A continuous gesture recognizer that tracks a pinch gesture that magnifies content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrotationgesturerecognizer)*