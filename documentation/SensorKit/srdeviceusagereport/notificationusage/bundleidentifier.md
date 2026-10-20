# bundleIdentifier

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The bundle identifier of the app that corresponds to the notification.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var bundleIdentifier: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * bundleIdentifier;
```

#### Discussion

The framework sets a value for this property only if the bundle identifier corresponds to an Apple app.

## See Also

### Analyzing Notification Use
- [var event: SRDeviceUsageReport.NotificationUsage.Event](./event-swift.property.md)
  The way that the user interacts with the notification.
- [SRDeviceUsageReport.NotificationUsage.Event](./event-swift.enum.md)
  The ways that a user interacts with notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/bundleidentifier)*