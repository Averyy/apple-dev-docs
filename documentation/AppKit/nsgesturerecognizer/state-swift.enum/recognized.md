# recognized

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The gesture recognizer successfully recognized its gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](./possible.md).

**Availability**:
- macOS 10.10+

## Declaration

```swift
static var recognized: NSGestureRecognizer.State { get }
```

```c
NSGestureRecognizerStateRecognized
```

## See Also

### Getting state values
- [NSGestureRecognizer.State.possible](./possible.md)
  The gesture recognizer has not yet recognized its gesture but may be evaluating events. This is the default state.
- [NSGestureRecognizer.State.began](./began.md)
  The gesture recognizer has recognized a sequence of events as a continuous gesture. It calls its action method at the next cycle of the run loop.
- [NSGestureRecognizer.State.changed](./changed.md)
  The gesture recognizer has detected a change to a continuous gesture. It calls its action method at the next cycle of the run loop.
- [NSGestureRecognizer.State.ended](./ended.md)
  The gesture recognizer has detected the end of a continuous gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](./possible.md).
- [NSGestureRecognizer.State.cancelled](./cancelled.md)
  The gesture recognizer received events that resulted in the cancellation of a continuous gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](./possible.md).
- [NSGestureRecognizer.State.failed](./failed.md)
  The gesture recognizer failed to recognize its gesture and will not call its action method. The gesture recognizer resets itself to the [`NSGestureRecognizer.State.possible`](./possible.md) state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/state-swift.enum/recognized)*