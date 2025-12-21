# wantsForwardedScrollEvents(for:)

**Framework**: AppKit  
**Kind**: method

Returns whether to forward elastic scrolling gesture events up the responder.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func wantsForwardedScrollEvents(for axis: NSEvent.GestureAxis) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) when forward gesture scroll events should be forwarded up the responder chain when the scrolling content is already at the edge of the scrolled direction at the beginning of the scroll gesture; [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

Some views process gesture scroll events to perform elastic scrolling. In some cases, you may want to track gesture scroll events like a swipe, see [`trackSwipeEvent(options:dampenAmountThresholdMin:max:usingHandler:)`](nsevent/trackswipeevent(options:dampenamountthresholdmin:max:usinghandler:).md).

Implement this method and return [`true`](https://developer.apple.com/documentation/Swift/true) in your swipe controller and views that perform elastic scrolling will forward gesture scroll events up the responder chain on the following condition: the content to be scrolled is already at the edge of the scrolled direction at the beginning of the scroll gesture.

Otherwise, the view will perform elastic scrolling.

## Parameters

- `axis`: The gesture axis. See   for the possible values.

## See Also

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
- [func smartMagnify(with: NSEvent)](nsresponder/smartmagnify(with:).md)
  Informs the receiver that the user performed a smart zoom gesture.
- [func wantsScrollEventsForSwipeTracking(on: NSEvent.GestureAxis) -> Bool](nsresponder/wantsscrolleventsforswipetracking(on:).md)
  Implement this method to track gesture scroll events such as a swipe.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/wantsforwardedscrollevents(for:))*