# notificationUsageByCategory

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The frequency of notifications per category.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var notificationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.NotificationUsage]] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,NSArray<SRNotificationUsage *> *> * notificationUsageByCategory;
```

## Discussion

The framework interprets the category using the primary genre an app supplies in its `iTunesMetadata.plist`.

## See Also

### Analyzing Notification Use
- [SRDeviceUsageReport.NotificationUsage](./notificationusage.md)
  An object that describes notification frequency and the manner in which the user interacts with notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory)*