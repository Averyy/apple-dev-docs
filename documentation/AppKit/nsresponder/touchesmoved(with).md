# touchesMoved(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the receiver that one or more touches has moved.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func touchesMoved(with event: NSEvent)
```

```objc
- (void) touchesMovedWithEvent:(NSEvent *) event;
```

## Discussion

The system sends the to the view under the touch in the key window. To get the set of touches that moved for this view (or descendants of this view) call [`touches(matching:in:)`](../nsevent/touches%28matching,in%29.md) on `event` and pass [`moved`](../nstouch/phase-swift.struct/moved.md) for the phase.

## Parameters

- `event`: An event object representing a touch movement.

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
- [func touchesCancelled(with: NSEvent)](./touchescancelled%28with%29.md)
  Informs the receiver that tracking of touches has been cancelled for any reason.
- [func touchesEnded(with: NSEvent)](./touchesended%28with%29.md)
  Returns that a set of touches have been removed.
- [func wantsForwardedScrollEvents(for: NSEvent.GestureAxis) -> Bool](./wantsforwardedscrollevents%28for%29.md)
  Returns whether to forward elastic scrolling gesture events up the responder.
- [func smartMagnify(with: NSEvent)](./smartmagnify%28with%29.md)
  Informs the receiver that the user performed a smart zoom gesture.
- [func wantsScrollEventsForSwipeTracking(on: NSEvent.GestureAxis) -> Bool](./wantsscrolleventsforswipetracking%28on%29.md)
  Implement this method to track gesture scroll events such as a swipe.
- [NSEvent.GestureAxis](../nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/touchesmoved(with:))*