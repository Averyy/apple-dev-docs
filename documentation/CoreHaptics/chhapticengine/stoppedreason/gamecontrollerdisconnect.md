# CHHapticEngine.StoppedReason.gameControllerDisconnect

**Framework**: Core Haptics  
**Kind**: case  
**Role**: Case

The engine stopped because the associated game controller disconnected from the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case gameControllerDisconnect
```

```c
CHHapticEngineStoppedReasonGameControllerDisconnect
```

## See Also

### Stopped Reasons
- [CHHapticEngine.StoppedReason.audioSessionInterrupt](./audiosessioninterrupt.md)
  The system interrupted the audio session.
- [CHHapticEngine.StoppedReason.applicationSuspended](./applicationsuspended.md)
  The system suspended your app.
- [CHHapticEngine.StoppedReason.engineDestroyed](./enginedestroyed.md)
  The system destroyed the engine.
- [CHHapticEngine.StoppedReason.idleTimeout](./idletimeout.md)
  The engine shut down because you’ve enabled automatic shutdown, and the engine reached its idle timeout.
- [CHHapticEngine.StoppedReason.notifyWhenFinished](./notifywhenfinished.md)
  You’ve asked the system to notify you when it shuts down the engine.
- [CHHapticEngine.StoppedReason.systemError](./systemerror.md)
  A system error stopped the engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/stoppedreason/gamecontrollerdisconnect)*