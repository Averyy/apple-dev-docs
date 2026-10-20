# wantsForwardedScrollEvents(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether to forward elastic scrolling gesture events up the responder.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func wantsForwardedScrollEvents(for axis: NSEvent.GestureAxis) -> Bool
```

```objc
- (BOOL) wantsForwardedScrollEventsForAxis:(NSEventGestureAxis) axis;
```

#### Return Value

Returns [`true`](../../Swift/true.md) when forward gesture scroll events should be forwarded up the responder chain when the scrolling content is already at the edge of the scrolled direction at the beginning of the scroll gesture; [`false`](../../Swift/false.md) otherwise.

#### Discussion

Some views process gesture scroll events to perform elastic scrolling. In some cases, you may want to track gesture scroll events like a swipe, see [`trackSwipeEvent(options:dampenAmountThresholdMin:max:usingHandler:)`](../nsevent/trackswipeevent%28options,dampenamountthresholdmin,max,usinghandler%29.md).

Implement this method and return [`true`](../../Swift/true.md) in your swipe controller and views that perform elastic scrolling will forward gesture scroll events up the responder chain on the following condition: the content to be scrolled is already at the edge of the scrolled direction at the beginning of the scroll gesture.

Otherwise, the view will perform elastic scrolling.

## Parameters

- `axis`: The gesture axis. See [`NSEvent.GestureAxis`](../nsevent/gestureaxis.md) for the possible values.

## See Also

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
- [func smartMagnify(with: NSEvent)](./smartmagnify%28with%29.md)
  Informs the receiver that the user performed a smart zoom gesture.
- [func wantsScrollEventsForSwipeTracking(on: NSEvent.GestureAxis) -> Bool](./wantsscrolleventsforswipetracking%28on%29.md)
  Implement this method to track gesture scroll events such as a swipe.
- [NSEvent.GestureAxis](../nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/wantsforwardedscrollevents(for:))*