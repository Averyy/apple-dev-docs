# gestureRecognizer(_:shouldAttemptToRecognizeWith:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if a gesture recognizer should attempt to recognize gestures for a particular event.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer, shouldAttemptToRecognizeWith event: NSEvent) -> Bool
```

```objc
- (BOOL) gestureRecognizer:(NSGestureRecognizer *) gestureRecognizer shouldAttemptToRecognizeWithEvent:(NSEvent *) event;
```

## Return Value

[`true`](../../Swift/true.md) to allow the gesture recognizer to begin recognizing gestures for the specified event, or [`false`](../../Swift/false.md) to prevent it from recognizing gestures for the specified event. If you do not implement this method, the default return value is [`true`](../../Swift/true.md).

## Discussion

This method is called when a target view recognizes a new gesture event stream. The target view calls this method to determine whether the gesture recognizer should process events for the stream, or opt out of them. Returning [`false`](../../Swift/false.md) from this method causes the gesture recognizer to opt out, and prevents the other delegate methods from being called for the event stream.

## Parameters

- `gestureRecognizer`: The gesture recognizer object that is interpreting events. This is the object with which the delegate is associated.
- `event`: An event object associated with the request.

## See Also

### Regulating gesture recognition
- [func gestureRecognizerShouldBegin(NSGestureRecognizer) -> Bool](./gesturerecognizershouldbegin%28_%29.md)
  Asks the delegate if a gesture recognizer should transition out of the Possible (`NSGestureRecognizerStatePossible`) state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/gesturerecognizer(_:shouldattempttorecognizewith:))*