# MXDiskIOMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about disk usage.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXDiskIOMetric
```

## Topics

### Reading disk use
- [var cumulativeLogicalWrites: Measurement<UnitInformationStorage>](mxdiskiometric/cumulativelogicalwrites.md)
  The total amount of data written to disk or other long term storage.

## Relationships

### Inherits From
- [MXMetric](mxmetric.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MXDiskSpaceUsageMetric](mxdiskspaceusagemetric.md)
  An object representing metrics about your app’s disk space usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskiometric)*