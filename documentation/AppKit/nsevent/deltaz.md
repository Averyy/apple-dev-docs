# deltaZ

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The z-coordinate change for a scroll wheel, mouse-move, or mouse-drag event.

**Availability**:
- macOS

## Declaration

```swift
var deltaZ: CGFloat { get }
```

```objc
@property (readonly) CGFloat deltaZ;
```

#### Discussion

This value is typically `0.0`.

## See Also

### Getting scroll wheel and flick events
- [var deltaX: CGFloat](./deltax.md)
  The x-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaY: CGFloat](./deltay.md)
  The y-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/deltaz)*