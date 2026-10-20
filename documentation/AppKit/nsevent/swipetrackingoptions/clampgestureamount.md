# clampGestureAmount

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Don’t allow gestureAmount to go beyond +/-1.0

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var clampGestureAmount: NSEvent.SwipeTrackingOptions { get }
```

```c
NSEventSwipeTrackingClampGestureAmount
```

## See Also

### Constants
- [static var lockDirection: NSEvent.SwipeTrackingOptions](./lockdirection.md)
  Clamp gestureAmount to 0 if the user starts to swipe in the opposite direction than they started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/swipetrackingoptions/clampgestureamount)*