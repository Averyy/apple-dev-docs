# LogicalDiskWritesMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the total data written to disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct LogicalDiskWritesMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.logicalDiskWrites(_:)`](metricresult/logicaldiskwrites(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

This type replaces the `cumulativeLogicalWrites` property of [`MXDiskIOMetric`](mxdiskiometric.md).

## Topics

### Measurements
- [let value: Measurement<UnitInformationStorage>](logicaldiskwritesmetric/value.md)
  The total amount of data written to disk or other long term storage.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DiskWriteExceptionDiagnostic](diskwriteexceptiondiagnostic.md)
  A diagnostic for a disk write exception.
- [struct TotalDiskSpaceCapacityMetric](totaldiskspacecapacitymetric.md)
  A metric that measures disk capacity and usage on the device.
- [struct TotalFileCountMetric](totalfilecountmetric.md)
  A metric that measures the number of files attributed to the app.
- [struct TotalFileSizeMetric](totalfilesizemetric.md)
  A metric that measures the sizes of files attributed to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/logicaldiskwritesmetric)*