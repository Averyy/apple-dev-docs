# TotalFileSizeMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the sizes of files attributed to the app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct TotalFileSizeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalFileSize(_:)`](metricresult/totalfilesize(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

This value is a daily snapshot, not a cumulative sum over the reporting interval.

## Topics

### Measurements
- [let binaryFileSize: Measurement<UnitInformationStorage>](totalfilesizemetric/binaryfilesize.md)
  The total size of disk space your app’s binary files occupy.
- [let cacheFolderSize: Measurement<UnitInformationStorage>](totalfilesizemetric/cachefoldersize.md)
  The total size of your application’s cache folder.
- [let cloneSize: Measurement<UnitInformationStorage>](totalfilesizemetric/clonesize.md)
  The total size of all clone files that are attributed to your app.
- [let dataFileSize: Measurement<UnitInformationStorage>](totalfilesizemetric/datafilesize.md)
  The total size of disk space your app uses for storing data files.

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
- [struct TotalFileCountMetric](totalfilecountmetric.md)
  A metric that measures the number of files attributed to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalfilesizemetric)*