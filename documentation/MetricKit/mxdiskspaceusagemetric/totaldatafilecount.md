# totalDataFileCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total number of data files in your app’s container(s).

**Availability**:
- iOS 26.0+ - Deprecated in 27.2
- iPadOS 26.0+ - Deprecated in 27.2
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.2
- visionOS 26.0+ - Deprecated in 27.2

> **Deprecated**: Use [`TotalFileCountMetric`](../totalfilecountmetric.md) instead.

## Declaration

```swift
var totalDataFileCount: Int { get }
```

```objc
@property (readonly) NSInteger totalDataFileCount;
```

#### Discussion

This includes all of the data files in your application’s container(s) (including `~/Library/Caches`). Additionally, it includes the clone files that are attributed to your application.

## See Also

### Reading file counts
- [var totalBinaryFileCount: Int](./totalbinaryfilecount.md)
  The total number of your app’s binary files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totaldatafilecount)*