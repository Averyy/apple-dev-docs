# NSGestureRecognizer.State.began

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The gesture recognizer has recognized a sequence of events as a continuous gesture. It calls its action method at the next cycle of the run loop.

**Availability**:
- macOS 10.10+

## Declaration

```swift
case began
```

```c
NSGestureRecognizerStateBegan
```

## See Also

### Getting state values
- [NSGestureRecognizer.State.possible](./possible.md)
  The gesture recognizer has not yet recognized its gesture but may be evaluating events. This is the default state.
- [NSGestureRecognizer.State.changed](./changed.md)
  The gesture recognizer has detected a change to a continuous gesture. It calls its action method at the next cycle of the run loop.
- [NSGestureRecognizer.State.ended](./ended.md)
  The gesture recognizer has detected the end of a continuous gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](./possible.md).
- [NSGestureRecognizer.State.cancelled](./cancelled.md)
  The gesture recognizer received events that resulted in the cancellation of a continuous gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](./possible.md).
- [NSGestureRecognizer.State.failed](./failed.md)
  The gesture recognizer failed to recognize its gesture and will not call its action method. The gesture recognizer resets itself to the [`NSGestureRecognizer.State.possible`](./possible.md) state.
- [static var recognized: NSGestureRecognizer.State](./recognized.md)
  The gesture recognizer successfully recognized its gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](./possible.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/state-swift.enum/began)*