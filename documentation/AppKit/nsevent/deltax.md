# deltaX

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The x-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.

**Availability**:
- macOS

## Declaration

```swift
var deltaX: CGFloat { get }
```

```objc
@property (readonly) CGFloat deltaX;
```

## Discussion

This property is only valid for scroll wheel, mouse-move, mouse-drag, and swipe events. For swipe events, a nonzero value represents a horizontal swipe; `-1.0` corresponds to swipe right and `1.0` corresponds to swipe left.

For scroll wheel events, use [`scrollingDeltaX`](./scrollingdeltax.md) instead.

## See Also

### Getting scroll wheel and flick events
- [var deltaY: CGFloat](./deltay.md)
  The y-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaZ: CGFloat](./deltaz.md)
  The z-coordinate change for a scroll wheel, mouse-move, or mouse-drag event.
- [var hasPreciseScrollingDeltas: Bool](./hasprecisescrollingdeltas.md)
  A Boolean value that indicates whether precise scrolling deltas are available.
- [var scrollingDeltaX: CGFloat](./scrollingdeltax.md)
  The scroll wheel’s horizontal delta.
- [var scrollingDeltaY: CGFloat](./scrollingdeltay.md)
  The scroll wheel’s vertical delta.
- [var momentumPhase: NSEvent.Phase](./momentumphase.md)
  The momentum phase for a scroll or flick gesture.
- [var isDirectionInvertedFromDevice: Bool](./isdirectioninvertedfromdevice.md)
  A Boolean value that indicates whether the user has changed the device inversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/deltax)*