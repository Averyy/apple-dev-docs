# CHHapticEngine.FinishedHandler

**Framework**: Core Haptics  
**Kind**: typealias

A type alias for a completion handler to execute after finishing haptic playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias FinishedHandler = ((any Error)?) -> CHHapticEngine.FinishedAction
```

## See Also

- [func notifyWhenPlayersFinished(finishedHandler: CHHapticEngine.FinishedHandler)](chhapticengine/notifywhenplayersfinished(finishedhandler:).md)
  Notifies you when all haptic pattern players have finished playing their haptic patterns.
- [CHHapticEngine.FinishedAction](chhapticengine/finishedaction.md)
  Possible actions to take after the haptic engine finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/finishedhandler)*