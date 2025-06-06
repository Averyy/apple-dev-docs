# touches(matching:in:)

**Framework**: AppKit  
**Kind**: method

Returns the touch objects associated with the specified phase.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func touches(matching phase: NSTouch.Phase, in view: NSView?) -> Set<NSTouch>
```

#### Return Value

A set of applicable [`NSTouch`](nstouch.md) objects.

#### Discussion

This method is only valid for gesture events (gesture, magnify, swipe, rotate, etc.).

## Parameters

- `phase`: The touch phase for which you want touches.
- `view`: The view for which touches are wanted. Touches that target this view, or any of the view’s descendants will be returned. Passing   as the view gets all touches regardless of their targeted view.

## See Also

- [var phase: NSEvent.Phase](nsevent/phase-swift.property.md)
  The phase of a gesture event, such as a magnify, scroll, or pressure change.
- [NSEvent.Phase](nsevent/phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [var magnification: CGFloat](nsevent/magnification.md)
  The amount of change to add to a magnification gesture.
- [func allTouches() -> Set<NSTouch>](nsevent/alltouches.md)
  Returns all touch objects associated with the event.
- [func touches(for: NSView) -> Set<NSTouch>](nsevent/touches(for:).md)
  Returns the touch objects from the event that belong to the specified view.
- [func coalescedTouches(for: NSTouch) -> [NSTouch]](nsevent/coalescedtouches(for:).md)
  Returns all of the touch objects associated with the specified main touch.
- [class var isMouseCoalescingEnabled: Bool](nsevent/ismousecoalescingenabled.md)
  A Boolean value that indicates whether the system coalesces mouse movement events.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/touches(matching:in:))*