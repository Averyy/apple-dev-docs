# CHHapticEngine.StoppedReason.idleTimeout

**Framework**: Corehaptics  
**Kind**: case

The engine shut down because you’ve enabled automatic shutdown, and the engine reached its idle timeout.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case idleTimeout
```

#### Discussion

If there’s a time-critical pattern to play, restart the engine. Otherwise, do nothing and the engine will automatically restart when the next pattern plays.

> **Note**:  Delegating engine restart to the system can add a slight delay to the start of the pattern.

## See Also

- [CHHapticEngine.StoppedReason.audioSessionInterrupt](chhapticengine/stoppedreason/audiosessioninterrupt.md)
  The system interrupted the audio session.
- [CHHapticEngine.StoppedReason.applicationSuspended](chhapticengine/stoppedreason/applicationsuspended.md)
  The system suspended your app.
- [CHHapticEngine.StoppedReason.engineDestroyed](chhapticengine/stoppedreason/enginedestroyed.md)
  The system destroyed the engine.
- [CHHapticEngine.StoppedReason.gameControllerDisconnect](chhapticengine/stoppedreason/gamecontrollerdisconnect.md)
  The engine stopped because the associated game controller disconnected from the device.
- [CHHapticEngine.StoppedReason.notifyWhenFinished](chhapticengine/stoppedreason/notifywhenfinished.md)
  You’ve asked the system to notify you when it shuts down the engine.
- [CHHapticEngine.StoppedReason.systemError](chhapticengine/stoppedreason/systemerror.md)
  A system error stopped the engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreHaptics/chhapticengine/stoppedreason/idletimeout)*