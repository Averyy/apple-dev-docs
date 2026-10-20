# CHHapticEngine.FinishedHandler

**Framework**: Core Haptics  
**Kind**: typealias  
**Role**: Type Alias

A type alias for a completion handler to execute after finishing haptic playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias FinishedHandler = ((any Error)?) -> CHHapticEngine.FinishedAction
```

```c
typedef enum CHHapticEngineFinishedAction (^)(NSError *) CHHapticEngineFinishedHandler;
```

## See Also

### Monitoring Finished Playback
- [func notifyWhenPlayersFinished(finishedHandler: CHHapticEngine.FinishedHandler)](./notifywhenplayersfinished%28finishedhandler%29.md)
  Notifies you when all haptic pattern players have finished playing their haptic patterns.
- [CHHapticEngine.FinishedAction](./finishedaction.md)
  Possible actions to take after the haptic engine finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/finishedhandler)*