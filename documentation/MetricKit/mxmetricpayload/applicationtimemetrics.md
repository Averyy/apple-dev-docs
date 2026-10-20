# applicationTimeMetrics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The app foreground and background time metrics for the reporting period.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](../metricresult.md), and read the [`TotalForegroundTimeMetric`](../totalforegroundtimemetric.md), [`TotalBackgroundTimeMetric`](../totalbackgroundtimemetric.md), [`TotalBackgroundAudioTimeMetric`](../totalbackgroundaudiotimemetric.md), or [`TotalBackgroundLocationTimeMetric`](../totalbackgroundlocationtimemetric.md) cases instead.

## Declaration

```swift
var applicationTimeMetrics: MXAppRunTimeMetric? { get }
```

```objc
@property (strong, readonly, nullable) MXAppRunTimeMetric * applicationTimeMetrics;
```

## See Also

### Reading performance metrics
- [var applicationExitMetrics: MXAppExitMetric?](./applicationexitmetrics.md)
  The app foreground and background exit metrics for the reporting period.
- [var memoryMetrics: MXMemoryMetric?](./memorymetrics.md)
  The memory metrics for the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/applicationtimemetrics)*