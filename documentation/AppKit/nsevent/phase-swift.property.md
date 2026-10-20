# phase

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The phase of a gesture event, such as a magnify, scroll, or pressure change.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var phase: NSEvent.Phase { get }
```

```objc
@property (readonly) NSEventPhase phase;
```

#### Discussion

A gesture phase corresponds to a fluid gesture event. As a gesture event occurs, its phase begins with [`began`](./phase-swift.struct/began.md) and ends with either [`ended`](./phase-swift.struct/ended.md) or [`cancelled`](./phase-swift.struct/cancelled.md). All the gesture events are sent to the view under the cursor when the [`began`](./phase-swift.struct/began.md) occurred.

Technically, a gesture scroll event starts with a [`began`](./phase-swift.struct/began.md) phase and ends with a [`ended`](./phase-swift.struct/ended.md). However, when the user puts two fingers down on a trackpad, the trackpad issues [`mayBegin`](./phase-swift.struct/maybegin.md), followed by [`began`](./phase-swift.struct/began.md), [`cancelled`](./phase-swift.struct/cancelled.md), or [`ended`](./phase-swift.struct/ended.md). The [`mayBegin`](./phase-swift.struct/maybegin.md) event phase signals that scrolling is about to begin before the gesture has technically started. A Magic Mouse does not issue [`mayBegin`](./phase-swift.struct/maybegin.md) scroll wheel events.

A pressure event (type [`NSEvent.EventType.pressure`](./eventtype/pressure.md)) is a fluid gesture. Like the other fluid gesture events, it has a phase that describes the sequence of the pressure gesture stream.

Legacy scroll wheel events (say from a Mighty Mouse) and momentum scroll wheel events both have a phase of [`NSEventPhaseNone`](../nseventphase/nseventphasenone.md). (Legacy scroll wheel events also have a [`momentumPhase`](./momentumphase.md) of [`NSEventPhaseNone`](../nseventphase/nseventphasenone.md).) For more information, see [`momentumPhase`](./momentumphase.md).

See [`NSEvent.Phase`](./phase-swift.struct.md) for possible values.

## See Also

### Getting gesture and touch information
- [NSEvent.Phase](./phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [var magnification: CGFloat](./magnification.md)
  The amount of change to add to a magnification gesture.
- [func touches(matching: NSTouch.Phase, in: NSView?) -> Set<NSTouch>](./touches%28matching,in%29.md)
  Returns the touch objects associated with the specified phase.
- [func allTouches() -> Set<NSTouch>](./alltouches%28%29.md)
  Returns all touch objects associated with the event.
- [func touches(for: NSView) -> Set<NSTouch>](./touches%28for%29.md)
  Returns the touch objects from the event that belong to the specified view.
- [func coalescedTouches(for: NSTouch) -> [NSTouch]](./coalescedtouches%28for%29.md)
  Returns all of the touch objects associated with the specified main touch.
- [class var isMouseCoalescingEnabled: Bool](./ismousecoalescingenabled.md)
  A Boolean value that indicates whether the system coalesces mouse movement events.
- [NSEvent.GestureAxis](./gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/phase-swift.property)*