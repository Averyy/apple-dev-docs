# cellularConditionMetrics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The cellular condition measurements for the reporting period.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](../metricresult.md), and read the [`CellularConditionTimeMetric`](../cellularconditiontimemetric.md) case instead.

## Declaration

```swift
var cellularConditionMetrics: MXCellularConditionMetric? { get }
```

```objc
@property (strong, readonly, nullable) MXCellularConditionMetric * cellularConditionMetrics;
```

## See Also

### Reading battery metrics
- [var cpuMetrics: MXCPUMetric?](./cpumetrics.md)
  The CPU metrics for the reporting period.
- [var displayMetrics: MXDisplayMetric?](./displaymetrics.md)
  The display metrics for the reporting period.
- [var gpuMetrics: MXGPUMetric?](./gpumetrics.md)
  The GPU metrics for the reporting period.
- [var locationActivityMetrics: MXLocationActivityMetric?](./locationactivitymetrics.md)
  The location-tracking activity for the reporting period.
- [var networkTransferMetrics: MXNetworkTransferMetric?](./networktransfermetrics.md)
  The network-transfer activity for the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/cellularconditionmetrics)*