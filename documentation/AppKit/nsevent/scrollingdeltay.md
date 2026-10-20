# scrollingDeltaY

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroll wheel’s vertical delta.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var scrollingDeltaY: CGFloat { get }
```

```objc
@property (readonly) CGFloat scrollingDeltaY;
```

#### Discussion

This is the preferred property for accessing [`NSScrollWheel`](../nsscrollwheel.md) delta values. When [`hasPreciseScrollingDeltas`](./hasprecisescrollingdeltas.md) is [`false`](../../Swift/false.md), multiply the value returned by this method by the line or row height. Otherwise scroll by the returned amount.

## See Also

### Getting scroll wheel and flick events
- [var deltaX: CGFloat](./deltax.md)
  The x-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaY: CGFloat](./deltay.md)
  The y-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaZ: CGFloat](./deltaz.md)
  The z-coordinate change for a scroll wheel, mouse-move, or mouse-drag event.
- [var hasPreciseScrollingDeltas: Bool](./hasprecisescrollingdeltas.md)
  A Boolean value that indicates whether precise scrolling deltas are available.
- [var scrollingDeltaX: CGFloat](./scrollingdeltax.md)
  The scroll wheel’s horizontal delta.
- [var momentumPhase: NSEvent.Phase](./momentumphase.md)
  The momentum phase for a scroll or flick gesture.
- [var isDirectionInvertedFromDevice: Bool](./isdirectioninvertedfromdevice.md)
  A Boolean value that indicates whether the user has changed the device inversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/scrollingdeltay)*