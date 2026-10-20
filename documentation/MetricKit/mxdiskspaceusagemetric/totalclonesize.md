# totalCloneSize

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total size of all clone files that are attributed to your app.

**Availability**:
- iOS 26.0+ - Deprecated in 27.2
- iPadOS 26.0+ - Deprecated in 27.2
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.2
- visionOS 26.0+ - Deprecated in 27.2

> **Deprecated**: Use [`TotalFileSizeMetric`](../totalfilesizemetric.md) instead.

## Declaration

```swift
var totalCloneSize: Measurement<UnitInformationStorage> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitInformationStorage *> * totalCloneSize;
```

## See Also

### Reading file sizes
- [var totalBinaryFileSize: Measurement<UnitInformationStorage>](./totalbinaryfilesize.md)
  The total size of disk space your app’s binary files occupy.
- [var totalCacheFolderSize: Measurement<UnitInformationStorage>](./totalcachefoldersize.md)
  The total size of your application’s cache folder.
- [var totalDataFileSize: Measurement<UnitInformationStorage>](./totaldatafilesize.md)
  The total size of disk space your app uses for storing data files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totalclonesize)*