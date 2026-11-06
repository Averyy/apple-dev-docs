# totalBinaryFileCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total number of your app’s binary files.

**Availability**:
- iOS 26.0+ - Deprecated in 27.3
- iPadOS 26.0+ - Deprecated in 27.3
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.3
- visionOS 26.0+ - Deprecated in 27.3

> **Deprecated**: Use [`TotalFileCountMetric`](../totalfilecountmetric.md) instead.

## Declaration

```swift
var totalBinaryFileCount: Int { get }
```

```objc
@property (readonly) NSInteger totalBinaryFileCount;
```

## Discussion

Binary files include the application’s executables, frameworks, and other constant files that are generated during the build process.

## See Also

### Reading file counts
- [var totalDataFileCount: Int](./totaldatafilecount.md)
  The total number of data files in your app’s container(s).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totalbinaryfilecount)*