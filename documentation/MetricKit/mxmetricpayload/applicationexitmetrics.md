# applicationExitMetrics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The app foreground and background exit metrics for the reporting period.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](../metricresult.md), and read the [`ForegroundTerminationMetric`](../foregroundterminationmetric.md) or [`BackgroundTerminationMetric`](../backgroundterminationmetric.md) cases instead.

## Declaration

```swift
var applicationExitMetrics: MXAppExitMetric? { get }
```

```objc
@property (strong, readonly, nullable) MXAppExitMetric * applicationExitMetrics;
```

## See Also

### Reading performance metrics
- [var applicationTimeMetrics: MXAppRunTimeMetric?](./applicationtimemetrics.md)
  The app foreground and background time metrics for the reporting period.
- [var memoryMetrics: MXMemoryMetric?](./memorymetrics.md)
  The memory metrics for the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/applicationexitmetrics)*