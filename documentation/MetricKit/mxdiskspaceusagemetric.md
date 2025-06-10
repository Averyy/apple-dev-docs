# MXDiskSpaceUsageMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about your app’s disk space usage.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MXDiskSpaceUsageMetric
```

#### Overview

This object provides insights on how your app utilizes disk space and related storage technologies, such as cache folders and clone files.

Disk space is a limited resource shared by many apps. Optimize your app’s disk space usage to provide a better customer experience. People can inspect your app’s disk footprint in Settings, and excessive usage may force them to remove your app to install new apps or perform system updates.

> **Note**: MetricKit reports MXDiskSpaceUsageMetric on devices running iOS 26 or later.

##### Disk Space Measurements

Modern file systems such APFS provide enhanced features to maximize space utilization, such as file cloning. The disk space usage metric reports size accurately without double counting the cloned files.

For example, if you copy a file using [`copyItem(at:to:)`](https://developer.apple.com/documentation/Foundation/FileManager/copyItem(at:to:)), the file system shows two separate files. However, due to the file system optimization, the copied file shares the same storage space with the original file. If you manually calculate the size of all your files, your calculation may also include the copied file, resulting in a larger size than expected.

##### Storing App Specific Files

Use the [`totalCacheFolderSize`](mxdiskspaceusagemetric/totalcachefoldersize.md) property of MXDiskSpaceUsageMetric to gain insights into how the operating system manages your app’s cached content in the field. Placing files in the appropriate directories, such as the [`cachesDirectory`](https://developer.apple.com/documentation/Foundation/URL/cachesDirectory) and [`temporaryDirectory`](https://developer.apple.com/documentation/Foundation/URL/temporaryDirectory) (see [`File System Basics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html)), allows the system to intelligently manage and purge content when necessary, ensuring optimal disk space utilization and a better user experience.

## Topics

### Reading file counts
- [var totalBinaryFileCount: Int](mxdiskspaceusagemetric/totalbinaryfilecount.md)
  The total number of your app’s binary files.
- [var totalDataFileCount: Int](mxdiskspaceusagemetric/totaldatafilecount.md)
  The total number of data files in your app’s container(s).
### Reading file sizes
- [var totalBinaryFileSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalbinaryfilesize.md)
  The total size of disk space your app’s binary files occupy.
- [var totalCacheFolderSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalcachefoldersize.md)
  The total size of your application’s cache folder.
- [var totalCloneSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totalclonesize.md)
  The total size of all clone files that are attributed to your app.
- [var totalDataFileSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totaldatafilesize.md)
  The total size of disk space your app uses for storing data files.
### Reading disk capacity and space
- [var totalDiskSpaceCapacity: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totaldiskspacecapacity.md)
  The total disk space capacity of the current device.
- [var totalDiskSpaceUsedSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totaldiskspaceusedsize.md)
  The total amount of used disk storage on the current device.

## Relationships

### Inherits From
- [MXMetric](mxmetric.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MXDiskIOMetric](mxdiskiometric.md)
  An object representing metrics about disk usage.
- [class MXDiskWriteExceptionDiagnostic](mxdiskwriteexceptiondiagnostic.md)
  An object representing a diagnostic report for a disk write exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric)*