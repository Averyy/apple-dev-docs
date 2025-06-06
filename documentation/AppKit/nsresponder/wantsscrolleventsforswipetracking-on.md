# wantsScrollEventsForSwipeTracking(on:)

**Framework**: AppKit  
**Kind**: method

Implement this method to track gesture scroll events such as a swipe.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func wantsScrollEventsForSwipeTracking(on axis: NSEvent.GestureAxis) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if gesture scroll events are to be forwarded up the responder chain; otherwise [`false`](https://developer.apple.com/documentation/swift/false). The default implementation returns [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Implement this method in your swipe controller and return [`true`](https://developer.apple.com/documentation/swift/true) to inform views that perform elastic scrolling to forward gesture scroll events up the responder chain. The events are forwarded only on the following condition: the content to be scrolled is already at the edge of the scrolled direction when the scroll gesture begins. Otherwise, the view performs elastic scrolling. The default implementation returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `axis`: The event gesture axis of the swipe, which defines the scroll direction.

## See Also

- [func trackSwipeEvent(options: NSEvent.SwipeTrackingOptions, dampenAmountThresholdMin: CGFloat, max: CGFloat, usingHandler: (CGFloat, NSEvent.Phase, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nsevent/trackswipeevent(options:dampenamountthresholdmin:max:usinghandler:).md)
  Allows tracking and user interface feedback of scroll wheel events.
- [func beginGesture(with: NSEvent)](nsresponder/begingesture(with:).md)
  Informs the receiver that the user has begun a touch gesture.
- [func endGesture(with: NSEvent)](nsresponder/endgesture(with:).md)
  Informs the receiver that the user has ended a touch gesture.
- [func magnify(with: NSEvent)](nsresponder/magnify(with:).md)
  Informs the receiver that the user has begun a pinch gesture.
- [func rotate(with: NSEvent)](nsresponder/rotate(with:).md)
  Informs the receiver that the user has begun a rotation gesture.
- [func swipe(with: NSEvent)](nsresponder/swipe(with:).md)
  Informs the receiver that the user has begun a swipe gesture.
- [func touchesBegan(with: NSEvent)](nsresponder/touchesbegan(with:).md)
  Informs the receiver that new set of touches has been recognized.
- [func touchesMoved(with: NSEvent)](nsresponder/touchesmoved(with:).md)
  Informs the receiver that one or more touches has moved.
- [func touchesCancelled(with: NSEvent)](nsresponder/touchescancelled(with:).md)
  Informs the receiver that tracking of touches has been cancelled for any reason.
- [func touchesEnded(with: NSEvent)](nsresponder/touchesended(with:).md)
  Returns that a set of touches have been removed.
- [func wantsForwardedScrollEvents(for: NSEvent.GestureAxis) -> Bool](nsresponder/wantsforwardedscrollevents(for:).md)
  Returns whether to forward elastic scrolling gesture events up the responder.
- [func smartMagnify(with: NSEvent)](nsresponder/smartmagnify(with:).md)
  Informs the receiver that the user performed a smart zoom gesture.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/wantsscrolleventsforswipetracking(on:))*