# CHHapticEngine.StoppedReason

**Framework**: Core Haptics  
**Kind**: enum  
**Role**: Enumeration

The enumeration of reasons the haptic engine stopped running.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum StoppedReason
```

```c
enum CHHapticEngineStoppedReason : NSInteger;
```

## Topics

### Stopped Reasons
- [CHHapticEngine.StoppedReason.audioSessionInterrupt](./stoppedreason/audiosessioninterrupt.md)
  The system interrupted the audio session.
- [CHHapticEngine.StoppedReason.applicationSuspended](./stoppedreason/applicationsuspended.md)
  The system suspended your app.
- [CHHapticEngine.StoppedReason.engineDestroyed](./stoppedreason/enginedestroyed.md)
  The system destroyed the engine.
- [CHHapticEngine.StoppedReason.gameControllerDisconnect](./stoppedreason/gamecontrollerdisconnect.md)
  The engine stopped because the associated game controller disconnected from the device.
- [CHHapticEngine.StoppedReason.idleTimeout](./stoppedreason/idletimeout.md)
  The engine shut down because you’ve enabled automatic shutdown, and the engine reached its idle timeout.
- [CHHapticEngine.StoppedReason.notifyWhenFinished](./stoppedreason/notifywhenfinished.md)
  You’ve asked the system to notify you when it shuts down the engine.
- [CHHapticEngine.StoppedReason.systemError](./stoppedreason/systemerror.md)
  A system error stopped the engine.
### Initializers
- [init?(rawValue: Int)](./stoppedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling Haptic Engine Stoppages
- [var stoppedHandler: CHHapticEngine.StoppedHandler](./stoppedhandler-swift.property.md)
  A closure the haptic engine calls when it stops due to external causes.
- [CHHapticEngine.StoppedHandler](./stoppedhandler-swift.typealias.md)
  A typealias for the block that the haptic engine calls after it stops due to an external cause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/stoppedreason)*