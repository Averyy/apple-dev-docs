# hasPreciseScrollingDeltas

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether precise scrolling deltas are available.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var hasPreciseScrollingDeltas: Bool { get }
```

```objc
@property (readonly) BOOL hasPreciseScrollingDeltas;
```

## Discussion

This property is set to [`true`](../../Swift/true.md) if precise scrolling deltas are available; otherwise, [`false`](../../Swift/false.md).

This property is valid for [`NSScrollWheel`](../nsscrollwheel.md) events. A generic scroll wheel issues rather coarse scroll deltas. Some mice and trackpads provide much more precise delta. This method determines how the values of the [`scrollingDeltaX`](./scrollingdeltax.md) and [`scrollingDeltaY`](./scrollingdeltay.md) should be interpreted.

## See Also

### Getting scroll wheel and flick events
- [var deltaX: CGFloat](./deltax.md)
  The x-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaY: CGFloat](./deltay.md)
  The y-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaZ: CGFloat](./deltaz.md)
  The z-coordinate change for a scroll wheel, mouse-move, or mouse-drag event.
- [var scrollingDeltaX: CGFloat](./scrollingdeltax.md)
  The scroll wheel’s horizontal delta.
- [var scrollingDeltaY: CGFloat](./scrollingdeltay.md)
  The scroll wheel’s vertical delta.
- [var momentumPhase: NSEvent.Phase](./momentumphase.md)
  The momentum phase for a scroll or flick gesture.
- [var isDirectionInvertedFromDevice: Bool](./isdirectioninvertedfromdevice.md)
  A Boolean value that indicates whether the user has changed the device inversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/hasprecisescrollingdeltas)*