# wantsScrollEventsForSwipeTracking(on:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implement this method to track gesture scroll events such as a swipe.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func wantsScrollEventsForSwipeTracking(on axis: NSEvent.GestureAxis) -> Bool
```

```objc
- (BOOL) wantsScrollEventsForSwipeTrackingOnAxis:(NSEventGestureAxis) axis;
```

#### Return Value

[`true`](../../Swift/true.md) if gesture scroll events are to be forwarded up the responder chain; otherwise [`false`](../../Swift/false.md). The default implementation returns [`false`](../../Swift/false.md).

#### Discussion

Implement this method in your swipe controller and return [`true`](../../Swift/true.md) to inform views that perform elastic scrolling to forward gesture scroll events up the responder chain. The events are forwarded only on the following condition: the content to be scrolled is already at the edge of the scrolled direction when the scroll gesture begins. Otherwise, the view performs elastic scrolling. The default implementation returns [`false`](../../Swift/false.md).

## Parameters

- `axis`: The event gesture axis of the swipe, which defines the scroll direction.

## See Also

### Related Documentation
- [func trackSwipeEvent(options: NSEvent.SwipeTrackingOptions, dampenAmountThresholdMin: CGFloat, max: CGFloat, usingHandler: (CGFloat, NSEvent.Phase, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](../nsevent/trackswipeevent%28options,dampenamountthresholdmin,max,usinghandler%29.md)
  Allows tracking and user interface feedback of scroll wheel events.
### Touch and Gesture Events
- [func magnify(with: NSEvent)](./magnify%28with%29.md)
  Informs the receiver that the user has begun a pinch gesture.
- [func rotate(with: NSEvent)](./rotate%28with%29.md)
  Informs the receiver that the user has begun a rotation gesture.
- [func swipe(with: NSEvent)](./swipe%28with%29.md)
  Informs the receiver that the user has begun a swipe gesture.
- [func touchesBegan(with: NSEvent)](./touchesbegan%28with%29.md)
  Informs the receiver that new set of touches has been recognized.
- [func touchesMoved(with: NSEvent)](./touchesmoved%28with%29.md)
  Informs the receiver that one or more touches has moved.
- [func touchesCancelled(with: NSEvent)](./touchescancelled%28with%29.md)
  Informs the receiver that tracking of touches has been cancelled for any reason.
- [func touchesEnded(with: NSEvent)](./touchesended%28with%29.md)
  Returns that a set of touches have been removed.
- [func wantsForwardedScrollEvents(for: NSEvent.GestureAxis) -> Bool](./wantsforwardedscrollevents%28for%29.md)
  Returns whether to forward elastic scrolling gesture events up the responder.
- [func smartMagnify(with: NSEvent)](./smartmagnify%28with%29.md)
  Informs the receiver that the user performed a smart zoom gesture.
- [NSEvent.GestureAxis](../nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/wantsscrolleventsforswipetracking(on:))*