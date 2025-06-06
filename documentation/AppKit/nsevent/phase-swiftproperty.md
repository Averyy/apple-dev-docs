# phase

**Framework**: AppKit  
**Kind**: property

The phase of a gesture event, such as a magnify, scroll, or pressure change.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var phase: NSEvent.Phase { get }
```

#### Discussion

A gesture phase corresponds to a fluid gesture event. As a gesture event occurs, its phase begins with [`began`](nsevent/phase-swift.struct/began.md) and ends with either [`ended`](nsevent/phase-swift.struct/ended.md) or [`cancelled`](nsevent/phase-swift.struct/cancelled.md). All the gesture events are sent to the view under the cursor when the [`began`](nsevent/phase-swift.struct/began.md) occurred.

Technically, a gesture scroll event starts with a [`began`](nsevent/phase-swift.struct/began.md) phase and ends with a [`ended`](nsevent/phase-swift.struct/ended.md). However, when the user puts two fingers down on a trackpad, the trackpad issues [`mayBegin`](nsevent/phase-swift.struct/maybegin.md), followed by [`began`](nsevent/phase-swift.struct/began.md), [`cancelled`](nsevent/phase-swift.struct/cancelled.md), or [`ended`](nsevent/phase-swift.struct/ended.md). The [`mayBegin`](nsevent/phase-swift.struct/maybegin.md) event phase signals that scrolling is about to begin before the gesture has technically started. A Magic Mouse does not issue [`mayBegin`](nsevent/phase-swift.struct/maybegin.md) scroll wheel events.

A pressure event (type [`NSEvent.EventType.pressure`](nsevent/eventtype/pressure.md)) is a fluid gesture. Like the other fluid gesture events, it has a phase that describes the sequence of the pressure gesture stream.

Legacy scroll wheel events (say from a Mighty Mouse) and momentum scroll wheel events both have a phase of [`NSEventPhaseNone`](nseventphase/nseventphasenone.md). (Legacy scroll wheel events also have a [`momentumPhase`](nsevent/momentumphase.md) of [`NSEventPhaseNone`](nseventphase/nseventphasenone.md).) To learn more about scroll wheel events, see [`Handling Trackpad Events`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/HandlingTouchEvents/HandlingTouchEvents.html#//apple_ref/doc/uid/10000060i-CH13).

See [`NSEvent.Phase`](nsevent/phase-swift.struct.md) for possible values.

## See Also

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
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/phase-swift.property)*