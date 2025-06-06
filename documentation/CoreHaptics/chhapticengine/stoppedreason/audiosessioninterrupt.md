# CHHapticEngine.StoppedReason.audioSessionInterrupt

**Framework**: Core Haptics  
**Kind**: case

The system interrupted the audio session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case audioSessionInterrupt
```

#### Discussion

Audio session interruptions occur due to interactions with other audio apps. For example, the system interrupts music playback when a user receives a phone call. When an interruption occurs, restart the engine before it starts another pattern player.

## See Also

- [CHHapticEngine.StoppedReason.applicationSuspended](chhapticengine/stoppedreason/applicationsuspended.md)
  The system suspended your app.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/stoppedreason/audiosessioninterrupt)*