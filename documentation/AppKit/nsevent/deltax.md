# deltaX

**Framework**: AppKit  
**Kind**: property

The x-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.

**Availability**:
- macOS ?+

## Declaration

```swift
var deltaX: CGFloat { get }
```

#### Discussion

This property is only valid for scroll wheel, mouse-move, mouse-drag, and swipe events. For swipe events, a nonzero value represents a horizontal swipe; `-1.0` corresponds to swipe right and `1.0` corresponds to swipe left.

For scroll wheel events, use [`scrollingDeltaX`](nsevent/scrollingdeltax.md) instead.

## See Also

- [var deltaY: CGFloat](nsevent/deltay.md)
  The y-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaZ: CGFloat](nsevent/deltaz.md)
  The z-coordinate change for a scroll wheel, mouse-move, or mouse-drag event.
- [var hasPreciseScrollingDeltas: Bool](nsevent/hasprecisescrollingdeltas.md)
  A Boolean value that indicates whether precise scrolling deltas are available.
- [var scrollingDeltaX: CGFloat](nsevent/scrollingdeltax.md)
  The scroll wheel’s horizontal delta.
- [var scrollingDeltaY: CGFloat](nsevent/scrollingdeltay.md)
  The scroll wheel’s vertical delta.
- [var momentumPhase: NSEvent.Phase](nsevent/momentumphase.md)
  The momentum phase for a scroll or flick gesture.
- [var isDirectionInvertedFromDevice: Bool](nsevent/isdirectioninvertedfromdevice.md)
  A Boolean value that indicates whether the user has changed the device inversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/deltax)*