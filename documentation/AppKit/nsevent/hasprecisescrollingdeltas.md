# hasPreciseScrollingDeltas

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether precise scrolling deltas are available.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var hasPreciseScrollingDeltas: Bool { get }
```

#### Discussion

This property is set to [`true`](https://developer.apple.com/documentation/Swift/true) if precise scrolling deltas are available; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

This property is valid for [`NSScrollWheel`](nsscrollwheel.md) events. A generic scroll wheel issues rather coarse scroll deltas. Some mice and trackpads provide much more precise delta. This method determines how the values of the [`scrollingDeltaX`](nsevent/scrollingdeltax.md) and [`scrollingDeltaY`](nsevent/scrollingdeltay.md) should be interpreted.

## See Also

- [var deltaX: CGFloat](nsevent/deltax.md)
  The x-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaY: CGFloat](nsevent/deltay.md)
  The y-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaZ: CGFloat](nsevent/deltaz.md)
  The z-coordinate change for a scroll wheel, mouse-move, or mouse-drag event.
- [var scrollingDeltaX: CGFloat](nsevent/scrollingdeltax.md)
  The scroll wheel’s horizontal delta.
- [var scrollingDeltaY: CGFloat](nsevent/scrollingdeltay.md)
  The scroll wheel’s vertical delta.
- [var momentumPhase: NSEvent.Phase](nsevent/momentumphase.md)
  The momentum phase for a scroll or flick gesture.
- [var isDirectionInvertedFromDevice: Bool](nsevent/isdirectioninvertedfromdevice.md)
  A Boolean value that indicates whether the user has changed the device inversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/hasprecisescrollingdeltas)*