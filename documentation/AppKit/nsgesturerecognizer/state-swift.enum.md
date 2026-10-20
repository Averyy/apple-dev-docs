# NSGestureRecognizer.State

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The current state of the gesture recognizer.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum State
```

```c
enum NSGestureRecognizerState : NSInteger;
```

## Topics

### Getting state values
- [NSGestureRecognizer.State.possible](./state-swift.enum/possible.md)
  The gesture recognizer has not yet recognized its gesture but may be evaluating events. This is the default state.
- [NSGestureRecognizer.State.began](./state-swift.enum/began.md)
  The gesture recognizer has recognized a sequence of events as a continuous gesture. It calls its action method at the next cycle of the run loop.
- [NSGestureRecognizer.State.changed](./state-swift.enum/changed.md)
  The gesture recognizer has detected a change to a continuous gesture. It calls its action method at the next cycle of the run loop.
- [NSGestureRecognizer.State.ended](./state-swift.enum/ended.md)
  The gesture recognizer has detected the end of a continuous gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](./state-swift.enum/possible.md).
- [NSGestureRecognizer.State.cancelled](./state-swift.enum/cancelled.md)
  The gesture recognizer received events that resulted in the cancellation of a continuous gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](./state-swift.enum/possible.md).
- [NSGestureRecognizer.State.failed](./state-swift.enum/failed.md)
  The gesture recognizer failed to recognize its gesture and will not call its action method. The gesture recognizer resets itself to the [`NSGestureRecognizer.State.possible`](./state-swift.enum/possible.md) state.
- [static var recognized: NSGestureRecognizer.State](./state-swift.enum/recognized.md)
  The gesture recognizer successfully recognized its gesture. It calls its action method at the next cycle of the run loop and resets its state to [`NSGestureRecognizer.State.possible`](./state-swift.enum/possible.md).
### Creating a state
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/state-swift.enum)*