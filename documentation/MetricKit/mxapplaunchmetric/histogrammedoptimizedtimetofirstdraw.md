# histogrammedOptimizedTimeToFirstDraw

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

A histogram of the different amounts of time associated with prewarmed app launches.

**Availability**:
- iOS 15.2+ - Deprecated in 27.2
- iPadOS 15.2+ - Deprecated in 27.2
- Mac Catalyst 15.2+ - Deprecated in 27.0
- macOS 12.2+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`OptimizedTimeToFirstDrawMetric`](../optimizedtimetofirstdrawmetric.md) instead.

## Declaration

```swift
var histogrammedOptimizedTimeToFirstDraw: MXHistogram<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) MXHistogram<NSUnitDuration *> * histogrammedOptimizedTimeToFirstDraw;
```

## See Also

### Viewing app launch and resume time
- [var histogrammedTimeToFirstDraw: MXHistogram<UnitDuration>](./histogrammedtimetofirstdraw.md)
  A histogram of the different amounts of time taken to launch the app.
- [var histogrammedApplicationResumeTime: MXHistogram<UnitDuration>](./histogrammedapplicationresumetime.md)
  A histogram of the different amounts of time taken to resume the app from the background.
- [var histogrammedExtendedLaunch: MXHistogram<UnitDuration>](./histogrammedextendedlaunch.md)
  A histogram of the different amounts of time taken to launch the app, including the extended launch tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric/histogrammedoptimizedtimetofirstdraw)*