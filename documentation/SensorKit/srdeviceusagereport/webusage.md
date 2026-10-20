# SRDeviceUsageReport.WebUsage

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

An object that describes a user’s website usage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class WebUsage
```

```objc
@interface SRWebUsage : NSObject
```

#### Overview

Each instance of this class represents a website in a particular app category. For more information, see [`webUsageByCategory`](./webusagebycategory.md).

## Topics

### Timing Web Use
- [var totalUsageTime: TimeInterval](./webusage/totalusagetime.md)
  The amount of web usage time that the report spans.

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

### Analyzing Web Use
- [var webUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.WebUsage]]](./webusagebycategory.md)
  The amount of time the user accesses domains per category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage)*