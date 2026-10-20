# gestureRecognizerShouldBegin(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if a gesture recognizer should transition out of the Possible (`NSGestureRecognizerStatePossible`) state.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func gestureRecognizerShouldBegin(_ gestureRecognizer: NSGestureRecognizer) -> Bool
```

```objc
- (BOOL) gestureRecognizerShouldBegin:(NSGestureRecognizer *) gestureRecognizer;
```

#### Return Value

[`true`](../../Swift/true.md) to let the gesture recognizer transition out of the Possible ([`NSGestureRecognizer.State.possible`](../nsgesturerecognizer/state-swift.enum/possible.md)) and continue trying to recognize the gesture or [`false`](../../Swift/false.md) to prevent it from trying to recognize its gesture. If you do not implement this method, the default return value is [`true`](../../Swift/true.md).

#### Discussion

When a gesture recognizer attempts to transition from the Possible ([`NSGestureRecognizer.State.possible`](../nsgesturerecognizer/state-swift.enum/possible.md)) state to a different state, such as [`NSGestureRecognizer.State.began`](../nsgesturerecognizer/state-swift.enum/began.md), the gesture recognizer calls this method to see if the transition should occur. Returning [`false`](../../Swift/false.md) from this delegate method causes the gesture recognizer to transition to the [`NSGestureRecognizer.State.failed`](../nsgesturerecognizer/state-swift.enum/failed.md) state.

For information about gesture states and transitions, see [State Transitions](../nsgesturerecognizer.md#State-Transitions) in [`NSGestureRecognizer`](../nsgesturerecognizer.md).

## Parameters

- `gestureRecognizer`: The gesture recognizer object that is interpreting events. This is the object with which the delegate is associated.

## See Also

### Regulating gesture recognition
- [func gestureRecognizer(NSGestureRecognizer, shouldAttemptToRecognizeWith: NSEvent) -> Bool](./gesturerecognizer%28_,shouldattempttorecognizewith%29.md)
  Asks the delegate if a gesture recognizer should attempt to recognize gestures for a particular event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/gesturerecognizershouldbegin(_:))*