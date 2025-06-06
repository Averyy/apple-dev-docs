# CHHapticEngine.StoppedReason

**Framework**: Core Haptics  
**Kind**: enum

The enumeration of reasons the haptic engine stopped running.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum StoppedReason
```

## Topics

### Stopped Reasons
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
- [CHHapticEngine.StoppedReason.systemError](chhapticengine/stoppedreason/systemerror.md)
  A system error stopped the engine.
### Initializers
- [init?(rawValue: Int)](chhapticengine/stoppedreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var stoppedHandler: CHHapticEngine.StoppedHandler](chhapticengine/stoppedhandler-swift.property.md)
  A closure the haptic engine calls when it stops due to external causes.
- [CHHapticEngine.StoppedHandler](chhapticengine/stoppedhandler-swift.typealias.md)
  A typealias for the block that the haptic engine calls after it stops due to an external cause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/stoppedreason)*