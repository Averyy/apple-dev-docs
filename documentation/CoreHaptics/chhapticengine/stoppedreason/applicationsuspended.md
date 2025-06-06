# CHHapticEngine.StoppedReason.applicationSuspended

**Framework**: Core Haptics  
**Kind**: case

The system suspended your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case applicationSuspended
```

#### Discussion

This condition occurs if the system suspended your app while it was in the background. Restart the engine when your app returns to the foreground to ensure proper haptic playback.

## See Also

- [CHHapticEngine.StoppedReason.audioSessionInterrupt](chhapticengine/stoppedreason/audiosessioninterrupt.md)
  The system interrupted the audio session.
- [CHHapticEngine.StoppedReason.engineDestroyed](chhapticengine/stoppedreason/enginedestroyed.md)
  The system destroyed the engine.
- [CHHapticEngine.StoppedReason.gameControllerDisconnect](chhapticengine/stoppedreason/gamecontrollerdisconnect.md)
  The engine stopped because the associated game controller disconnected from the device.
- [CHHapticEngine.StoppedReason.idleTimeout](chhapticengine/stoppedreason/idletimeout.md)
  The engine shut down because you’ve enabled automatic shutdown, and the engine reached its idle timeout.
- [CHHapticEngine.StoppedReason.notifyWhenFinished](chhapticengine/stoppedreason/notifywhenfinished.md)
  You’ve asked the system to notify you when it shuts down the engine.
- [CHHapticEngine.StoppedReason.systemError](chhapticengine/stoppedreason/systemerror.md)
  A system error stopped the engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/stoppedreason/applicationsuspended)*