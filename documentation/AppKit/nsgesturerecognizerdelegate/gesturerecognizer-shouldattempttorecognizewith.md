# gestureRecognizer(_:shouldAttemptToRecognizeWith:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate if a gesture recognizer should attempt to recognize gestures for a particular event.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer, shouldAttemptToRecognizeWith event: NSEvent) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to allow the gesture recognizer to begin recognizing gestures for the specified event, or [`false`](https://developer.apple.com/documentation/swift/false) to prevent it from recognizing gestures for the specified event. If you do not implement this method, the default return value is [`true`](https://developer.apple.com/documentation/swift/true).

#### Discussion

This method is called when a target view recognizes a new gesture event stream. The target view calls this method to determine whether the gesture recognizer should process events for the stream, or opt out of them. Returning [`false`](https://developer.apple.com/documentation/swift/false) from this method causes the gesture recognizer to opt out, and prevents the other delegate methods from being called for the event stream.

## Parameters

- `gestureRecognizer`: The gesture recognizer object that is interpreting events. This is the object with which the delegate is associated.
- `event`: An event object associated with the request.

## See Also

- [func gestureRecognizerShouldBegin(NSGestureRecognizer) -> Bool](nsgesturerecognizerdelegate/gesturerecognizershouldbegin(_:).md)
  Asks the delegate if a gesture recognizer should transition out of the Possible (`NSGestureRecognizerStatePossible`) state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/gesturerecognizer(_:shouldattempttorecognizewith:))*