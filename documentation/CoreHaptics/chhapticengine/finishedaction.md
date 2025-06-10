# CHHapticEngine.FinishedAction

**Framework**: Core Haptics  
**Kind**: enum

Possible actions to take after the haptic engine finishes execution.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum FinishedAction
```

## Topics

### Finished Actions
- [CHHapticEngine.FinishedAction.leaveEngineRunning](chhapticengine/finishedaction/leaveenginerunning.md)
  Keeps the engine running after it finishes playing all haptic patterns.
- [CHHapticEngine.FinishedAction.stopEngine](chhapticengine/finishedaction/stopengine.md)
  Stops the engine after it finishes playing all haptic patterns.
### Initializers
- [init?(rawValue: Int)](chhapticengine/finishedaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func notifyWhenPlayersFinished(finishedHandler: CHHapticEngine.FinishedHandler)](chhapticengine/notifywhenplayersfinished(finishedhandler:).md)
  Notifies you when all haptic pattern players have finished playing their haptic patterns.
- [CHHapticEngine.FinishedHandler](chhapticengine/finishedhandler.md)
  A type alias for a completion handler to execute after finishing haptic playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/finishedaction)*