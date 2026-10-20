# CHHapticEngine.FinishedAction

**Framework**: Core Haptics  
**Kind**: enum  
**Role**: Enumeration

Possible actions to take after the haptic engine finishes execution.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum FinishedAction
```

```c
enum CHHapticEngineFinishedAction : NSInteger;
```

## Topics

### Finished Actions
- [CHHapticEngine.FinishedAction.leaveEngineRunning](./finishedaction/leaveenginerunning.md)
  Keeps the engine running after it finishes playing all haptic patterns.
- [CHHapticEngine.FinishedAction.stopEngine](./finishedaction/stopengine.md)
  Stops the engine after it finishes playing all haptic patterns.
### Initializers
- [init?(rawValue: Int)](./finishedaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitoring Finished Playback
- [func notifyWhenPlayersFinished(finishedHandler: CHHapticEngine.FinishedHandler)](./notifywhenplayersfinished%28finishedhandler%29.md)
  Notifies you when all haptic pattern players have finished playing their haptic patterns.
- [CHHapticEngine.FinishedHandler](./finishedhandler.md)
  A type alias for a completion handler to execute after finishing haptic playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/finishedaction)*