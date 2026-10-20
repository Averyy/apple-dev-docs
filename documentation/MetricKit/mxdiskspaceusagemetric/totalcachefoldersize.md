# totalCacheFolderSize

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total size of your application’s cache folder.

**Availability**:
- iOS 26.0+ - Deprecated in 27.2
- iPadOS 26.0+ - Deprecated in 27.2
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.2
- visionOS 26.0+ - Deprecated in 27.2

> **Deprecated**: Use [`TotalFileSizeMetric`](../totalfilesizemetric.md) instead.

## Declaration

```swift
var totalCacheFolderSize: Measurement<UnitInformationStorage> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitInformationStorage *> * totalCacheFolderSize;
```

#### Discussion

The value of this metric represents total size of [`cachesDirectory`](../../Foundation/url/cachesdirectory.md).

Placing files in the appropriate directories, such as the [`cachesDirectory`](../../Foundation/url/cachesdirectory.md) and [`temporaryDirectory`](../../Foundation/url/temporarydirectory.md), allows the system to manage and purge content when necessary, ensuring optimal disk space utilization and a better experience (see [File System Basics](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html)).

## See Also

### Reading file sizes
- [var totalBinaryFileSize: Measurement<UnitInformationStorage>](./totalbinaryfilesize.md)
  The total size of disk space your app’s binary files occupy.
- [var totalCloneSize: Measurement<UnitInformationStorage>](./totalclonesize.md)
  The total size of all clone files that are attributed to your app.
- [var totalDataFileSize: Measurement<UnitInformationStorage>](./totaldatafilesize.md)
  The total size of disk space your app uses for storing data files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totalcachefoldersize)*