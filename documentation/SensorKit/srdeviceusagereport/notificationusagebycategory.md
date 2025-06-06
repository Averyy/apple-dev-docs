# notificationUsageByCategory

**Framework**: SensorKit  
**Kind**: property

The frequency of notifications per category.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var notificationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.NotificationUsage]] { get }
```

#### Discussion

The framework interprets the category using the primary genre an app supplies in its `iTunesMetadata.plist`.

## See Also

- [SRDeviceUsageReport.NotificationUsage](srdeviceusagereport/notificationusage.md)
  An object that describes notification frequency and the manner in which the user interacts with notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory)*