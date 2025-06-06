# webUsageByCategory

**Framework**: SensorKit  
**Kind**: property

The amount of time the user accesses domains per category.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var webUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.WebUsage]] { get }
```

#### Discussion

The framework interprets the category in the same manner as displayed in Screen Time.

## See Also

- [SRDeviceUsageReport.WebUsage](srdeviceusagereport/webusage.md)
  An object that describes a user’s website usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusagebycategory)*