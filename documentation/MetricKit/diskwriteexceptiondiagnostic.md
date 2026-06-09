# DiskWriteExceptionDiagnostic

**Framework**: MetricKit  
**Kind**: struct

A diagnostic for a disk write exception.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DiskWriteExceptionDiagnostic
```

#### Discussion

Disk write exceptions occur when your app writes data to disk at an excessive rate. The diagnostic includes a [`CallStackTree`](callstacktree.md) to identify the responsible code path, and `totalBytesWritten` to quantify the I/O.

This type replaces [`MXDiskWriteExceptionDiagnostic`](mxdiskwriteexceptiondiagnostic.md).

## Topics

### Call stack
- [let callStackTree: CallStackTree](diskwriteexceptiondiagnostic/callstacktree.md)
  The application call stack tree associated with the excessive disk writes.
### Disk write details
- [let totalBytesWritten: Measurement<UnitInformationStorage>](diskwriteexceptiondiagnostic/totalbyteswritten.md)
  Total bytes written during the exception period.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct LogicalDiskWritesMetric](logicaldiskwritesmetric.md)
  A metric that measures the total data written to disk.
- [struct TotalDiskSpaceCapacityMetric](totaldiskspacecapacitymetric.md)
  A metric that measures disk capacity and usage on the device.
- [struct TotalFileCountMetric](totalfilecountmetric.md)
  A metric that measures the number of files attributed to the app.
- [struct TotalFileSizeMetric](totalfilesizemetric.md)
  A metric that measures the sizes of files attributed to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/diskwriteexceptiondiagnostic)*