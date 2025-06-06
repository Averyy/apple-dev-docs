# SRDeviceUsageReport.NotificationUsage.Event

**Framework**: SensorKit  
**Kind**: enum

The ways that a user interacts with notifications.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum Event
```

## Topics

### Events
- [SRDeviceUsageReport.NotificationUsage.Event.appLaunch](srdeviceusagereport/notificationusage/event-swift.enum/applaunch.md)
  A notification of an app launch.
- [SRDeviceUsageReport.NotificationUsage.Event.bannerPulldown](srdeviceusagereport/notificationusage/event-swift.enum/bannerpulldown.md)
  A notification of a banner pull down.
- [SRDeviceUsageReport.NotificationUsage.Event.clear](srdeviceusagereport/notificationusage/event-swift.enum/clear.md)
  A notification of a clear event.
- [SRDeviceUsageReport.NotificationUsage.Event.deduped](srdeviceusagereport/notificationusage/event-swift.enum/deduped.md)
  A notification of a deduped event.
- [SRDeviceUsageReport.NotificationUsage.Event.defaultAction](srdeviceusagereport/notificationusage/event-swift.enum/defaultaction.md)
  A notification of a default action.
- [SRDeviceUsageReport.NotificationUsage.Event.deviceActivated](srdeviceusagereport/notificationusage/event-swift.enum/deviceactivated.md)
  A notification of device activation.
- [SRDeviceUsageReport.NotificationUsage.Event.deviceUnlocked](srdeviceusagereport/notificationusage/event-swift.enum/deviceunlocked.md)
  A notification of a device unlock.
- [SRDeviceUsageReport.NotificationUsage.Event.expired](srdeviceusagereport/notificationusage/event-swift.enum/expired.md)
  A notification of an expiration event.
- [SRDeviceUsageReport.NotificationUsage.Event.hide](srdeviceusagereport/notificationusage/event-swift.enum/hide.md)
  A notification of a hide event.
- [SRDeviceUsageReport.NotificationUsage.Event.longLook](srdeviceusagereport/notificationusage/event-swift.enum/longlook.md)
  A notification of a long look.
- [SRDeviceUsageReport.NotificationUsage.Event.notificationCenterClearAll](srdeviceusagereport/notificationusage/event-swift.enum/notificationcenterclearall.md)
  A notification of clear-all event.
- [SRDeviceUsageReport.NotificationUsage.Event.received](srdeviceusagereport/notificationusage/event-swift.enum/received.md)
  A notification of a received event.
- [SRDeviceUsageReport.NotificationUsage.Event.removed](srdeviceusagereport/notificationusage/event-swift.enum/removed.md)
  A notification of a removed event.
- [SRDeviceUsageReport.NotificationUsage.Event.silence](srdeviceusagereport/notificationusage/event-swift.enum/silence.md)
  A notification of a silence event.
- [SRDeviceUsageReport.NotificationUsage.Event.supplementaryAction](srdeviceusagereport/notificationusage/event-swift.enum/supplementaryaction.md)
  A notification of a supplementary action.
- [SRDeviceUsageReport.NotificationUsage.Event.tapCoalesce](srdeviceusagereport/notificationusage/event-swift.enum/tapcoalesce.md)
  A notification of a tap-coalesce event.
- [SRDeviceUsageReport.NotificationUsage.Event.unknown](srdeviceusagereport/notificationusage/event-swift.enum/unknown.md)
  A notification of an unknown event.
### Initializers
- [init?(rawValue: Int)](srdeviceusagereport/notificationusage/event-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var bundleIdentifier: String?](srdeviceusagereport/notificationusage/bundleidentifier.md)
  The bundle identifier of the app that corresponds to the notification.
- [var event: SRDeviceUsageReport.NotificationUsage.Event](srdeviceusagereport/notificationusage/event-swift.property.md)
  The way that the user interacts with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum)*