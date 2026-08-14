# ProcessInfo.PowerStateDidChangeMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the device’s power state changes.

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
struct PowerStateDidChangeMessage
```

#### Overview

After your observer receives this notification, query the [`isLowPowerModeEnabled`](processinfo/islowpowermodeenabled.md) property to determine the current power state of the device. If Low Power Mode is active, take appropriate steps to reduce activity in your app. Otherwise, your app can resume normal operations.

Observe this message with the identifier [`powerStateDidChange`](notificationcenter/messageidentifier/powerstatedidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`ProcessInfo`](processinfo.md).

This message interoperates with the notification [`NSProcessInfoPowerStateDidChange`](nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](processinfo/powerstatedidchangemessage/init.md)
  Creates a message about a power state change.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [ProcessInfo.ThermalStateDidChangeMessage](processinfo/thermalstatedidchangemessage.md)
  A message the system sends when the device’s thermal state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/powerstatedidchangemessage)*