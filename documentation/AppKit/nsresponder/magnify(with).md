# magnify(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the receiver that the user has begun a pinch gesture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func magnify(with event: NSEvent)
```

```objc
- (void) magnifyWithEvent:(NSEvent *) event;
```

#### Discussion

The event will be sent to the view under the touch in the key window.

## Parameters

- `event`: An event object representing the magnify gesture.

## See Also

### Touch and Gesture Events
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
- [func wantsScrollEventsForSwipeTracking(on: NSEvent.GestureAxis) -> Bool](./wantsscrolleventsforswipetracking%28on%29.md)
  Implement this method to track gesture scroll events such as a swipe.
- [NSEvent.GestureAxis](../nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/magnify(with:))*