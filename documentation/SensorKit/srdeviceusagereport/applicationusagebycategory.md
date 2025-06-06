# applicationUsageByCategory

**Framework**: SensorKit  
**Kind**: property

The usage time of apps per category.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var applicationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.ApplicationUsage]] { get }
```

#### Discussion

The framework interprets the category using the primary genre an app supplies in its `iTunesMetadata.plist`.

## See Also

- [SRDeviceUsageReport.ApplicationUsage](srdeviceusagereport/applicationusage.md)
  An object that describes the user’s app activity over a period of time.
- [SRDeviceUsageReport.CategoryKey](srdeviceusagereport/categorykey.md)
  Categories of apps or websites that the user uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusagebycategory)*