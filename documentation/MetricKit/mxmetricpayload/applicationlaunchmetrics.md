# applicationLaunchMetrics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The app launch and resume metrics for the reporting period.

**Availability**:
- iOS 13.0+ - Deprecated in 27.3
- iPadOS 13.0+ - Deprecated in 27.3
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3

> **Deprecated**: Use [`MetricResult`](../metricresult.md), and read the [`TimeToFirstDrawMetric`](../timetofirstdrawmetric.md), [`OptimizedTimeToFirstDrawMetric`](../optimizedtimetofirstdrawmetric.md), [`ApplicationResumeTimeMetric`](../applicationresumetimemetric.md), or [`ExtendedLaunchMetric`](../extendedlaunchmetric.md) cases instead.

## Declaration

```swift
var applicationLaunchMetrics: MXAppLaunchMetric? { get }
```

```objc
@property (strong, readonly, nullable) MXAppLaunchMetric * applicationLaunchMetrics;
```

## See Also

### Reading responsiveness metrics
- [var animationMetrics: MXAnimationMetric?](./animationmetrics.md)
  The metrics for the responsiveness of app animations for the reporting period.
- [var applicationResponsivenessMetrics: MXAppResponsivenessMetric?](./applicationresponsivenessmetrics.md)
  The metrics indicating an app’s responsiveness to user interaction for the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/applicationlaunchmetrics)*