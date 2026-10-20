# isDirectionInvertedFromDevice

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user has changed the device inversion.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isDirectionInvertedFromDevice: Bool { get }
```

```objc
@property (readonly, getter=isDirectionInvertedFromDevice) BOOL directionInvertedFromDevice;
```

#### Discussion

This property is set to [`true`](../../Swift/true.md) if the direction is inverted; otherwise, [`false`](../../Swift/false.md).

This property is valid for `NSEventScrollWheel` and [`NSEvent.EventType.swipe`](./eventtype/swipe.md) events. The user may choose to change the scrolling behavior such that it feels like they are moving the content instead of the scroll bar.

To accomplish this, [`deltaX`](./deltax.md) and [`deltaY`](./deltay.md) and [`scrollingDeltaX`](./scrollingdeltax.md) and [`scrollingDeltaY`](./scrollingdeltay.md) values are automatically inverted for NSEventScrollWheel events according to the user’s preferences.

The direction of fluid swipes matches the direction of scrolling and as such for NSEventTypeSwipe events gestureAmount is inverted. However, for some uses of NSEventScrollWheel and NSEventTypeSwipe events, the behavior should not respect the user preference. This property allows you to determine when the event has been inverted and compensate by multiplying by `-1` if needed.

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
- [var scrollingDeltaY: CGFloat](./scrollingdeltay.md)
  The scroll wheel’s vertical delta.
- [var momentumPhase: NSEvent.Phase](./momentumphase.md)
  The momentum phase for a scroll or flick gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/isdirectioninvertedfromdevice)*