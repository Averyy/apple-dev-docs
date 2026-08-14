# TotalFileCountMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the number of files attributed to the app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct TotalFileCountMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalFileCount(_:)`](metricresult/totalfilecount(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

This value is a daily snapshot, not a cumulative sum over the reporting interval.

## Topics

### Measurements
- [let binaryFileCount: Int](totalfilecountmetric/binaryfilecount.md)
  The total number of your app’s binary files.
- [let dataFileCount: Int](totalfilecountmetric/datafilecount.md)
  The total number of data files in your app’s container(s).

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct LogicalDiskWritesMetric](logicaldiskwritesmetric.md)
  A metric that measures the total data written to disk.
- [struct DiskWriteExceptionDiagnostic](diskwriteexceptiondiagnostic.md)
  A diagnostic for a disk write exception.
- [struct TotalDiskSpaceCapacityMetric](totaldiskspacecapacitymetric.md)
  A metric that measures disk capacity and usage on the device.
- [struct TotalFileSizeMetric](totalfilesizemetric.md)
  A metric that measures the sizes of files attributed to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalfilecountmetric)*