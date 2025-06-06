# NSEvent.GestureAxis

**Framework**: AppKit  
**Kind**: enum

Constants that specify the direction of travel for a gesture.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum GestureAxis
```

## Topics

### Getting the Axis
- [NSEvent.GestureAxis.none](nsevent/gestureaxis/none.md)
  No specific axis.
- [NSEvent.GestureAxis.horizontal](nsevent/gestureaxis/horizontal.md)
  The horizontal axis.
- [NSEvent.GestureAxis.vertical](nsevent/gestureaxis/vertical.md)
  The vertical axis.
### Initializers
- [init?(rawValue: Int)](nsevent/gestureaxis/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [class var isMouseCoalescingEnabled: Bool](nsevent/ismousecoalescingenabled.md)
  A Boolean value that indicates whether the system coalesces mouse movement events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/gestureaxis)*