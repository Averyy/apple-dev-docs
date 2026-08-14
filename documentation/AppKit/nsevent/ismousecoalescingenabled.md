# isMouseCoalescingEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the system coalesces mouse movement events.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class var isMouseCoalescingEnabled: Bool { get set }
```

#### Discussion

Mouse movement events include mouse-moved, mouse-dragged, and tablet events. If this property is [`true`](https://developer.apple.com/documentation/swift/true), coalescing is enabled; otherwise, it’s disabled. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

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
- [func coalescedTouches(for: NSTouch) -> [NSTouch]](nsevent/coalescedtouches(for:).md)
  Returns all of the touch objects associated with the specified main touch.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/ismousecoalescingenabled)*