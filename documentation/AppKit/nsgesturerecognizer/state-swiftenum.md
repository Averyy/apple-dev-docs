# NSGestureRecognizer.State

**Framework**: AppKit  
**Kind**: enum

The current state of the gesture recognizer.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum State
```

## Topics

### Constants
- [NSGestureRecognizer.State.possible](nsgesturerecognizer/state-swift.enum/possible.md)
  The gesture recognizer has not yet recognized its gesture but may be evaluating events. This is the default state.
- [NSGestureRecognizer.State.began](nsgesturerecognizer/state-swift.enum/began.md)
  The gesture recognizer has recognized a sequence of events as a continuous gesture. It calls its action method at the next cycle of the run loop.
- [NSGestureRecognizer.State.changed](nsgesturerecognizer/state-swift.enum/changed.md)
  The gesture recognizer has detected a change to a continuous gesture. It calls its action method at the next cycle of the run loop.
- [NSGestureRecognizer.State.ended](nsgesturerecognizer/state-swift.enum/ended.md)
  The gesture recognizer has detected the end of a continuous gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](nsgesturerecognizer/state-swift.enum/possible.md).
- [NSGestureRecognizer.State.cancelled](nsgesturerecognizer/state-swift.enum/cancelled.md)
  The gesture recognizer received events that resulted in the cancellation of a continuous gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](nsgesturerecognizer/state-swift.enum/possible.md).
- [NSGestureRecognizer.State.failed](nsgesturerecognizer/state-swift.enum/failed.md)
  The gesture recognizer failed to recognize its gesture and will not call its action method. The gesture recognizer resets itself to the [`NSGestureRecognizer.State.possible`](nsgesturerecognizer/state-swift.enum/possible.md) state.
- [static var recognized: NSGestureRecognizer.State](nsgesturerecognizer/state-swift.enum/recognized.md)
  The gesture recognizer successfully recognized its gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](nsgesturerecognizer/state-swift.enum/possible.md).
### Initializers
- [init?(rawValue: Int)](nsgesturerecognizer/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/state-swift.enum)*