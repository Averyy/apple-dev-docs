# reduceMotionStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that UIKit posts when the system’s Reduce Motion setting changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let reduceMotionStatusDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIAccessibilityReduceMotionStatusDidChangeNotification;
```

#### Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Motion
- [static let shakeToUndoDidChangeNotification: NSNotification.Name](./shaketoundodidchangenotification.md)
  A notification that UIKit posts when the system’s Shake to Undo setting changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/reducemotionstatusdidchangenotification)*