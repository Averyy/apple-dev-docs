# TotalDiskSpaceCapacityMetric

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric that measures disk capacity and usage on the device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
struct TotalDiskSpaceCapacityMetric
```

## Discussion

This metric corresponds to the [`MetricResult.totalDiskSpaceCapacity(_:)`](./metricresult/totaldiskspacecapacity%28_%29.md) case. It appears only in [`intervalEntries`](./metricreport/intervalentries.md) and is not included in state entries.

This value is a daily snapshot, not a cumulative sum over the reporting interval.

## Topics

### Measurements
- [let capacity: Measurement<UnitInformationStorage>](./totaldiskspacecapacitymetric/capacity.md)
  The total disk space capacity of the current device.
- [let spaceUsed: Measurement<UnitInformationStorage>](./totaldiskspacecapacitymetric/spaceused.md)
  The total amount of used disk storage on the current device.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Disk metrics
- [struct LogicalDiskWritesMetric](./logicaldiskwritesmetric.md)
  A metric that measures the total data written to disk.
- [struct DiskWriteExceptionDiagnostic](./diskwriteexceptiondiagnostic.md)
  A diagnostic for a disk write exception.
- [struct TotalFileCountMetric](./totalfilecountmetric.md)
  A metric that measures the number of files attributed to the app.
- [struct TotalFileSizeMetric](./totalfilesizemetric.md)
  A metric that measures the sizes of files attributed to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totaldiskspacecapacitymetric)*