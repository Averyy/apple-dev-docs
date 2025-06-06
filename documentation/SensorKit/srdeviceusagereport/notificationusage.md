# SRDeviceUsageReport.NotificationUsage

**Framework**: SensorKit  
**Kind**: class

An object that describes notification frequency and the manner in which the user interacts with notifications.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class NotificationUsage
```

#### Overview

Each instance of this class represents a user notification in a particular app category. For more information, see [`notificationUsageByCategory`](srdeviceusagereport/notificationusagebycategory.md).

## Topics

### Analyzing Notification Use
- [var bundleIdentifier: String?](srdeviceusagereport/notificationusage/bundleidentifier.md)
  The bundle identifier of the app that corresponds to the notification.
- [var event: SRDeviceUsageReport.NotificationUsage.Event](srdeviceusagereport/notificationusage/event-swift.property.md)
  The way that the user interacts with the notification.
- [SRDeviceUsageReport.NotificationUsage.Event](srdeviceusagereport/notificationusage/event-swift.enum.md)
  The ways that a user interacts with notifications.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var notificationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.NotificationUsage]]](srdeviceusagereport/notificationusagebycategory.md)
  The frequency of notifications per category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage)*