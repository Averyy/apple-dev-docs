# SRDeviceUsageReport.NotificationUsage

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

An object that describes notification frequency and the manner in which the user interacts with notifications.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class NotificationUsage
```

```objc
@interface SRNotificationUsage : NSObject
```

#### Overview

Each instance of this class represents a user notification in a particular app category. For more information, see [`notificationUsageByCategory`](./notificationusagebycategory.md).

## Topics

### Analyzing Notification Use
- [var bundleIdentifier: String?](./notificationusage/bundleidentifier.md)
  The bundle identifier of the app that corresponds to the notification.
- [var event: SRDeviceUsageReport.NotificationUsage.Event](./notificationusage/event-swift.property.md)
  The way that the user interacts with the notification.
- [SRDeviceUsageReport.NotificationUsage.Event](./notificationusage/event-swift.enum.md)
  The ways that a user interacts with notifications.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Analyzing Notification Use
- [var notificationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.NotificationUsage]]](./notificationusagebycategory.md)
  The frequency of notifications per category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage)*