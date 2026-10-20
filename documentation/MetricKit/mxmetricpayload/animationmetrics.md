# animationMetrics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The metrics for the responsiveness of app animations for the reporting period.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](../metricresult.md), and read the [`HitchTimeMetric`](../hitchtimemetric.md) case instead.

## Declaration

```swift
var animationMetrics: MXAnimationMetric? { get }
```

```objc
@property (strong, readonly, nullable) MXAnimationMetric * animationMetrics;
```

## See Also

### Reading responsiveness metrics
- [var applicationLaunchMetrics: MXAppLaunchMetric?](./applicationlaunchmetrics.md)
  The app launch and resume metrics for the reporting period.
- [var applicationResponsivenessMetrics: MXAppResponsivenessMetric?](./applicationresponsivenessmetrics.md)
  The metrics indicating an app’s responsiveness to user interaction for the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/animationmetrics)*