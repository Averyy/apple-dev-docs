# TotalDiskSpaceCapacityMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures disk capacity and usage on the device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct TotalDiskSpaceCapacityMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalDiskSpaceCapacity(_:)`](metricresult/totaldiskspacecapacity(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

This value is a daily snapshot, not a cumulative sum over the reporting interval.

This type replaces the `totalDiskSpaceCapacity` and `totalDiskSpaceUsedSize` properties of [`MXDiskSpaceUsageMetric`](mxdiskspaceusagemetric.md).

## Topics

### Measurements
- [let capacity: Measurement<UnitInformationStorage>](totaldiskspacecapacitymetric/capacity.md)
  The total disk space capacity of the current device.
- [let spaceUsed: Measurement<UnitInformationStorage>](totaldiskspacecapacitymetric/spaceused.md)
  The total amount of used disk storage on the current device.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct LogicalDiskWritesMetric](logicaldiskwritesmetric.md)
  A metric that measures the total data written to disk.
- [struct DiskWriteExceptionDiagnostic](diskwriteexceptiondiagnostic.md)
  A diagnostic for a disk write exception.
- [struct TotalFileCountMetric](totalfilecountmetric.md)
  A metric that measures the number of files attributed to the app.
- [struct TotalFileSizeMetric](totalfilesizemetric.md)
  A metric that measures the sizes of files attributed to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totaldiskspacecapacitymetric)*