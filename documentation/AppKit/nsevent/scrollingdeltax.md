# scrollingDeltaX

**Framework**: AppKit  
**Kind**: property

The scroll wheel’s horizontal delta.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var scrollingDeltaX: CGFloat { get }
```

#### Discussion

This is the preferred property for accessing [`NSScrollWheel`](nsscrollwheel.md) delta values. When [`hasPreciseScrollingDeltas`](nsevent/hasprecisescrollingdeltas.md) is [`false`](https://developer.apple.com/documentation/swift/false), your application may need to modify the raw value before using it.

## See Also

- [var deltaX: CGFloat](nsevent/deltax.md)
  The x-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaY: CGFloat](nsevent/deltay.md)
  The y-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaZ: CGFloat](nsevent/deltaz.md)
  The z-coordinate change for a scroll wheel, mouse-move, or mouse-drag event.
- [var hasPreciseScrollingDeltas: Bool](nsevent/hasprecisescrollingdeltas.md)
  A Boolean value that indicates whether precise scrolling deltas are available.
- [var scrollingDeltaY: CGFloat](nsevent/scrollingdeltay.md)
  The scroll wheel’s vertical delta.
- [var momentumPhase: NSEvent.Phase](nsevent/momentumphase.md)
  The momentum phase for a scroll or flick gesture.
- [var isDirectionInvertedFromDevice: Bool](nsevent/isdirectioninvertedfromdevice.md)
  A Boolean value that indicates whether the user has changed the device inversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/scrollingdeltax)*