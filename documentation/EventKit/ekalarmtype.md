# EKAlarmType

**Framework**: EventKit  
**Kind**: enum

A value that specifies what type of action occurs when the alarm triggers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum EKAlarmType
```

## Topics

### Constants
- [EKAlarmType.display](ekalarmtype/display.md)
  The alarm displays a message.
- [EKAlarmType.audio](ekalarmtype/audio.md)
  The alarm plays a sound.
- [EKAlarmType.procedure](ekalarmtype/procedure.md)
  The alarm opens a URL.
- [EKAlarmType.email](ekalarmtype/email.md)
  The alarm sends an email.
### Initializers
- [init?(rawValue: Int)](ekalarmtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var type: EKAlarmType](ekalarm/type.md)
  The type of action to trigger when the alarm fires.
- [var emailAddress: String?](ekalarm/emailaddress.md)
  The recipient of an email to send when the alarm triggers.
- [var soundName: String?](ekalarm/soundname.md)
  The name of the sound to play when the alarm triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarmtype)*