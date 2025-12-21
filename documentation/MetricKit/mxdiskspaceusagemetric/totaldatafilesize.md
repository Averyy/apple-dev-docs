# totalDataFileSize

**Framework**: MetricKit  
**Kind**: property

The total size of disk space your app uses for storing data files.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var totalDataFileSize: Measurement<UnitInformationStorage> { get }
```

#### Discussion

This includes all of the data files in your application’s container(s) (including [`cachesDirectory`](https://developer.apple.com/documentation/Foundation/URL/cachesDirectory)). Additionally, it includes the clone files that are attributed to your application.

## See Also

- [var totalBinaryFileSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalbinaryfilesize.md)
  The total size of disk space your app’s binary files occupy.
- [var totalCacheFolderSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalcachefoldersize.md)
  The total size of your application’s cache folder.
- [var totalCloneSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalclonesize.md)
  The total size of all clone files that are attributed to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totaldatafilesize)*