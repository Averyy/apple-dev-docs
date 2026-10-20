# SRDeviceUsageReport.NotificationUsage.Event

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

The ways that a user interacts with notifications.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum Event
```

```c
enum SRNotificationEvent : NSInteger;
```

## Topics

### Events
- [SRDeviceUsageReport.NotificationUsage.Event.appLaunch](./event-swift.enum/applaunch.md)
  A notification of an app launch.
- [SRDeviceUsageReport.NotificationUsage.Event.bannerPulldown](./event-swift.enum/bannerpulldown.md)
  A notification of a banner pull down.
- [SRDeviceUsageReport.NotificationUsage.Event.clear](./event-swift.enum/clear.md)
  A notification of a clear event.
- [SRDeviceUsageReport.NotificationUsage.Event.deduped](./event-swift.enum/deduped.md)
  A notification of a deduped event.
- [SRDeviceUsageReport.NotificationUsage.Event.defaultAction](./event-swift.enum/defaultaction.md)
  A notification of a default action.
- [SRDeviceUsageReport.NotificationUsage.Event.deviceActivated](./event-swift.enum/deviceactivated.md)
  A notification of device activation.
- [SRDeviceUsageReport.NotificationUsage.Event.deviceUnlocked](./event-swift.enum/deviceunlocked.md)
  A notification of a device unlock.
- [SRDeviceUsageReport.NotificationUsage.Event.expired](./event-swift.enum/expired.md)
  A notification of an expiration event.
- [SRDeviceUsageReport.NotificationUsage.Event.hide](./event-swift.enum/hide.md)
  A notification of a hide event.
- [SRDeviceUsageReport.NotificationUsage.Event.longLook](./event-swift.enum/longlook.md)
  A notification of a long look.
- [SRDeviceUsageReport.NotificationUsage.Event.notificationCenterClearAll](./event-swift.enum/notificationcenterclearall.md)
  A notification of clear-all event.
- [SRDeviceUsageReport.NotificationUsage.Event.received](./event-swift.enum/received.md)
  A notification of a received event.
- [SRDeviceUsageReport.NotificationUsage.Event.removed](./event-swift.enum/removed.md)
  A notification of a removed event.
- [SRDeviceUsageReport.NotificationUsage.Event.silence](./event-swift.enum/silence.md)
  A notification of a silence event.
- [SRDeviceUsageReport.NotificationUsage.Event.supplementaryAction](./event-swift.enum/supplementaryaction.md)
  A notification of a supplementary action.
- [SRDeviceUsageReport.NotificationUsage.Event.tapCoalesce](./event-swift.enum/tapcoalesce.md)
  A notification of a tap-coalesce event.
- [SRDeviceUsageReport.NotificationUsage.Event.unknown](./event-swift.enum/unknown.md)
  A notification of an unknown event.
### Initializers
- [init?(rawValue: Int)](./event-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Analyzing Notification Use
- [var bundleIdentifier: String?](./bundleidentifier.md)
  The bundle identifier of the app that corresponds to the notification.
- [var event: SRDeviceUsageReport.NotificationUsage.Event](./event-swift.property.md)
  The way that the user interacts with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum)*