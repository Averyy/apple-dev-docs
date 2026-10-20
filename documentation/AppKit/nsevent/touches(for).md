# touches(for:)

**Framework**: AppKit  
**Kind**: method

Returns the touch objects from the event that belong to the specified view.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func touches(for view: NSView) -> Set<NSTouch>
```

#### Return Value

A set of [`NSTouch`](nstouch.md) objects that correspond to the touches in the view.

## Parameters

- `view`: The view in which the touches originally occurred.

## See Also

- [var phase: NSEvent.Phase](nsevent/phase-swift.property.md)
  The phase of a gesture event, such as a magnify, scroll, or pressure change.
- [NSEvent.Phase](nsevent/phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [var magnification: CGFloat](nsevent/magnification.md)
  The amount of change to add to a magnification gesture.
- [func touches(matching: NSTouch.Phase, in: NSView?) -> Set<NSTouch>](nsevent/touches(matching:in:).md)
  Returns the touch objects associated with the specified phase.
- [func allTouches() -> Set<NSTouch>](nsevent/alltouches.md)
  Returns all touch objects associated with the event.
- [func coalescedTouches(for: NSTouch) -> [NSTouch]](nsevent/coalescedtouches(for:).md)
  Returns all of the touch objects associated with the specified main touch.
- [class var isMouseCoalescingEnabled: Bool](nsevent/ismousecoalescingenabled.md)
  A Boolean value that indicates whether the system coalesces mouse movement events.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/touches(for:))*