# diskSpaceUsageMetrics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

An object containing disk space usage metrics for this application.

**Availability**:
- iOS 26.0+ - Deprecated in 27.3
- iPadOS 26.0+ - Deprecated in 27.3
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.3
- visionOS 26.0+ - Deprecated in 27.3

> **Deprecated**: Use [`MetricResult`](../metricresult.md), and read the [`TotalFileCountMetric`](../totalfilecountmetric.md), [`TotalFileSizeMetric`](../totalfilesizemetric.md), or [`TotalDiskSpaceCapacityMetric`](../totaldiskspacecapacitymetric.md) cases instead.

## Declaration

```swift
var diskSpaceUsageMetrics: MXDiskSpaceUsageMetric? { get }
```

```objc
@property (strong, readonly, nullable) MXDiskSpaceUsageMetric * diskSpaceUsageMetrics;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/diskspaceusagemetrics)*