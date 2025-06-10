# totalBinaryFileSize

**Framework**: MetricKit  
**Kind**: property

The total size of disk space your app’s binary files occupy.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var totalBinaryFileSize: Measurement<UnitInformationStorage> { get }
```

#### Discussion

Binary files include the application’s executables, frameworks, and other constant files that are generated during the build process.

## See Also

- [var totalCacheFolderSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalcachefoldersize.md)
  The total size of your application’s cache folder.
- [var totalCloneSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalclonesize.md)
  The total size of all clone files that are attributed to your app.
- [var totalDataFileSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totaldatafilesize.md)
  The total size of disk space your app uses for storing data files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totalbinaryfilesize)*