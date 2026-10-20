# notifyWhenPlayersFinished(finishedHandler:)

**Framework**: Core Haptics  
**Kind**: method  
**Role**: Instance Method

Notifies you when all haptic pattern players have finished playing their haptic patterns.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func notifyWhenPlayersFinished(finishedHandler: @escaping CHHapticEngine.FinishedHandler)
```

```objc
- (void) notifyWhenPlayersFinished:(CHHapticEngineFinishedHandler) finishedHandler;
```

## Parameters

- `finishedHandler`: A closure to execute when all players have finished playback.

## See Also

### Monitoring Finished Playback
- [CHHapticEngine.FinishedHandler](./finishedhandler.md)
  A type alias for a completion handler to execute after finishing haptic playback.
- [CHHapticEngine.FinishedAction](./finishedaction.md)
  Possible actions to take after the haptic engine finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/notifywhenplayersfinished(finishedhandler:))*