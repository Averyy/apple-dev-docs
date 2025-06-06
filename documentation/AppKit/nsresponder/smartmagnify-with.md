# smartMagnify(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the user performed a smart zoom gesture.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func smartMagnify(with event: NSEvent)
```

#### Discussion

The smart zoom gesture is a two-finger double tap on trackpads. In response to this event, you should intelligently magnify the content.

## Parameters

- `event`: An event object representing the smart zoom gesture.

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
- [func wantsForwardedScrollEvents(for: NSEvent.GestureAxis) -> Bool](nsresponder/wantsforwardedscrollevents(for:).md)
  Returns whether to forward elastic scrolling gesture events up the responder.
- [func wantsScrollEventsForSwipeTracking(on: NSEvent.GestureAxis) -> Bool](nsresponder/wantsscrolleventsforswipetracking(on:).md)
  Implement this method to track gesture scroll events such as a swipe.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/smartmagnify(with:))*