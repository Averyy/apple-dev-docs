# coalescedTouches(for:)

**Framework**: AppKit  
**Kind**: method

Returns all of the touch objects associated with the specified main touch.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func coalescedTouches(for touch: NSTouch) -> [NSTouch]
```

#### Return Value

An array that contains the [`NSTouch`](nstouch.md) objects AppKit generated since the last event, but didn’t deliver. This method returns `nil` if the object in the `touch` parameter isn’t associated with the current event.

#### Discussion

Use this method to obtain additional touch objects that the system received but didn’t deliver to your app. You might use these extra touch objects to create a more precise path for the touch sequence.

AppKit coalesces touches only when they occur in the Touch Bar; it doesn’t coalesce touch events on the track pad. This method returns the complete sequence of touches since the last event, and it returns them in the same order the system reported them. The last object in the array is a copy of the same object you provided in the `touch` parameter.

## Parameters

- `touch`: A touch that occurred in the Touch Bar. The method uses this object to determine which additional touch objects to return.

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
- [func touches(for: NSView) -> Set<NSTouch>](nsevent/touches(for:).md)
  Returns the touch objects from the event that belong to the specified view.
- [class var isMouseCoalescingEnabled: Bool](nsevent/ismousecoalescingenabled.md)
  A Boolean value that indicates whether the system coalesces mouse movement events.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/coalescedtouches(for:))*