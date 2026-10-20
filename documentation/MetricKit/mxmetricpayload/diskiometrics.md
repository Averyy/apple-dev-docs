# diskIOMetrics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The storage metrics for the reporting period.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](../metricresult.md), and read the [`LogicalDiskWritesMetric`](../logicaldiskwritesmetric.md) case instead.

## Declaration

```swift
var diskIOMetrics: MXDiskIOMetric? { get }
```

```objc
@property (strong, readonly, nullable) MXDiskIOMetric * diskIOMetrics;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/diskiometrics)*