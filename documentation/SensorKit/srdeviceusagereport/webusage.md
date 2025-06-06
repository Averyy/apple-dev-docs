# SRDeviceUsageReport.WebUsage

**Framework**: SensorKit  
**Kind**: class

An object that describes a user’s website usage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class WebUsage
```

#### Overview

Each instance of this class represents a website in a particular app category. For more information, see [`webUsageByCategory`](srdeviceusagereport/webusagebycategory.md).

## Topics

### Timing Web Use
- [var totalUsageTime: TimeInterval](srdeviceusagereport/webusage/totalusagetime.md)
  The amount of web usage time that the report spans.

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

- [var webUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.WebUsage]]](srdeviceusagereport/webusagebycategory.md)
  The amount of time the user accesses domains per category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage)*