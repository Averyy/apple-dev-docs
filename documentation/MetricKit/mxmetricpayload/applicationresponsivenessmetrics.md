# applicationResponsivenessMetrics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The metrics indicating an app’s responsiveness to user interaction for the reporting period.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](../metricresult.md), and read the [`HangTimeMetric`](../hangtimemetric.md) case instead.

## Declaration

```swift
var applicationResponsivenessMetrics: MXAppResponsivenessMetric? { get }
```

```objc
@property (strong, readonly, nullable) MXAppResponsivenessMetric * applicationResponsivenessMetrics;
```

## See Also

### Reading responsiveness metrics
- [var applicationLaunchMetrics: MXAppLaunchMetric?](./applicationlaunchmetrics.md)
  The app launch and resume metrics for the reporting period.
- [var animationMetrics: MXAnimationMetric?](./animationmetrics.md)
  The metrics for the responsiveness of app animations for the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/applicationresponsivenessmetrics)*