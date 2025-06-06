# CHHapticEngine.StoppedReason.systemError

**Framework**: Core Haptics  
**Kind**: case

A system error stopped the engine.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case systemError
```

## Mentions

- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)

#### Discussion

Your app should attempt to restart the engine. If the restart attempt fails multiple times, treat the condition as fatal.

## See Also

- [CHHapticEngine.StoppedReason.audioSessionInterrupt](chhapticengine/stoppedreason/audiosessioninterrupt.md)
  The system interrupted the audio session.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/stoppedreason/systemerror)*