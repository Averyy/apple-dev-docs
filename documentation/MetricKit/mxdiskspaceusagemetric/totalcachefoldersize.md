# totalCacheFolderSize

**Framework**: MetricKit  
**Kind**: property

The total size of your application’s cache folder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var totalCacheFolderSize: Measurement<UnitInformationStorage> { get }
```

#### Discussion

The value of this metric represents total size of [`cachesDirectory`](https://developer.apple.com/documentation/Foundation/URL/cachesDirectory).

Placing files in the appropriate directories, such as the [`cachesDirectory`](https://developer.apple.com/documentation/Foundation/URL/cachesDirectory) and [`temporaryDirectory`](https://developer.apple.com/documentation/Foundation/URL/temporaryDirectory), allows the system to manage and purge content when necessary, ensuring optimal disk space utilization and a better experience (see [`File System Basics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html)).

## See Also

- [var totalBinaryFileSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalbinaryfilesize.md)
  The total size of disk space your app’s binary files occupy.
- [var totalCloneSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalclonesize.md)
  The total size of all clone files that are attributed to your app.
- [var totalDataFileSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totaldatafilesize.md)
  The total size of disk space your app uses for storing data files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totalcachefoldersize)*