# magnify(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the user has begun a pinch gesture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func magnify(with event: NSEvent)
```

#### Discussion

The event will be sent to the view under the touch in the key window.

## Parameters

- `event`: An event object representing the magnify gesture.

## See Also

- [func beginGesture(with: NSEvent)](nsresponder/begingesture(with:).md)
  Informs the receiver that the user has begun a touch gesture.
- [func endGesture(with: NSEvent)](nsresponder/endgesture(with:).md)
  Informs the receiver that the user has ended a touch gesture.
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
- [func wantsScrollEventsForSwipeTracking(on: NSEvent.GestureAxis) -> Bool](nsresponder/wantsscrolleventsforswipetracking(on:).md)
  Implement this method to track gesture scroll events such as a swipe.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/magnify(with:))*