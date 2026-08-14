# ProcessInfo.ThermalStateDidChangeMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the device’s thermal state changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ThermalStateDidChangeMessage
```

#### Overview

To observe this message, access the [`thermalState`](processinfo/thermalstate-swift.property.md) property prior to adding your observer.

Observe this message with the identifier [`thermalStateDidChange`](notificationcenter/messageidentifier/thermalstatedidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`ProcessInfo`](processinfo.md).

This message interoperates with the notification [`thermalStateDidChangeNotification`](processinfo/thermalstatedidchangenotification.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](processinfo/thermalstatedidchangemessage/init.md)
  Creates a message about a thermal state change.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [ProcessInfo.PowerStateDidChangeMessage](processinfo/powerstatedidchangemessage.md)
  A message the system sends when the device’s power state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/thermalstatedidchangemessage)*