# magnification

**Framework**: AppKit  
**Kind**: property

The amount of change to add to a magnification gesture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var magnification: CGFloat { get }
```

#### Discussion

The change in magnification that should be added to the current scaling of an item to achieve the new scale factor. This message is valid only for events of type [`NSEvent.EventType.magnify`](nsevent/eventtype/magnify.md).

## See Also

- [var phase: NSEvent.Phase](nsevent/phase-swift.property.md)
  The phase of a gesture event, such as a magnify, scroll, or pressure change.
- [NSEvent.Phase](nsevent/phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [func touches(matching: NSTouch.Phase, in: NSView?) -> Set<NSTouch>](nsevent/touches(matching:in:).md)
  Returns the touch objects associated with the specified phase.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/magnification)*