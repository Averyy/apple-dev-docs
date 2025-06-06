# touchesEnded(with:)

**Framework**: AppKit  
**Kind**: method

Returns that a set of touches have been removed.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func touchesEnded(with event: NSEvent)
```

#### Discussion

The system sends the event to the view under the touch in the key window. To get the set of touches that ended for this view (or descendants of this view) call [`touches(matching:in:)`](nsevent/touches(matching:in:).md) on `event` and pass [`ended`](nstouch/phase-swift.struct/ended.md) for the phase.

This isn’t always the point of removal with the touch device. A touch that transitions from active to resting may be part of an [`touchesEnded(with:)`](nsresponder/touchesended(with:).md) set.

## Parameters

- `event`: An event object representing the ending of a touch event.

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
- [func wantsForwardedScrollEvents(for: NSEvent.GestureAxis) -> Bool](nsresponder/wantsforwardedscrollevents(for:).md)
  Returns whether to forward elastic scrolling gesture events up the responder.
- [func smartMagnify(with: NSEvent)](nsresponder/smartmagnify(with:).md)
  Informs the receiver that the user performed a smart zoom gesture.
- [func wantsScrollEventsForSwipeTracking(on: NSEvent.GestureAxis) -> Bool](nsresponder/wantsscrolleventsforswipetracking(on:).md)
  Implement this method to track gesture scroll events such as a swipe.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/touchesended(with:))*