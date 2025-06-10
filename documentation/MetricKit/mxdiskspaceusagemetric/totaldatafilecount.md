# totalDataFileCount

**Framework**: MetricKit  
**Kind**: property

The total number of data files in your app’s container(s).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var totalDataFileCount: Int { get }
```

#### Discussion

This includes all of the data files in your application’s container(s) (including `~/Library/Caches`). Additionally, it includes the clone files that are attributed to your application.

## See Also

- [var totalBinaryFileCount: Int](mxdiskspaceusagemetric/totalbinaryfilecount.md)
  The total number of your app’s binary files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totaldatafilecount)*