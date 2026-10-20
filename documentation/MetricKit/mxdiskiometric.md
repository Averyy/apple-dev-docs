# MXDiskIOMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about disk usage.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`LogicalDiskWritesMetric`](./logicaldiskwritesmetric.md) case instead.

## Declaration

```swift
class MXDiskIOMetric
```

```objc
@interface MXDiskIOMetric : MXMetric
```

## Topics

### Reading disk use
- [var cumulativeLogicalWrites: Measurement<UnitInformationStorage>](./mxdiskiometric/cumulativelogicalwrites.md)
  The total amount of data written to disk or other long term storage.

## Relationships

### Inherits From
- [MXMetric](./mxmetric.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Disk metrics
- [class MXDiskSpaceUsageMetric](./mxdiskspaceusagemetric.md)
  An object representing metrics about your app’s disk space usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskiometric)*