# histogrammedApplicationResumeTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

A histogram of the different amounts of time taken to resume the app from the background.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`ApplicationResumeTimeMetric`](../applicationresumetimemetric.md) instead.

## Declaration

```swift
var histogrammedApplicationResumeTime: MXHistogram<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) MXHistogram<NSUnitDuration *> * histogrammedApplicationResumeTime;
```

## See Also

### Viewing app launch and resume time
- [var histogrammedOptimizedTimeToFirstDraw: MXHistogram<UnitDuration>](./histogrammedoptimizedtimetofirstdraw.md)
  A histogram of the different amounts of time associated with prewarmed app launches.
- [var histogrammedTimeToFirstDraw: MXHistogram<UnitDuration>](./histogrammedtimetofirstdraw.md)
  A histogram of the different amounts of time taken to launch the app.
- [var histogrammedExtendedLaunch: MXHistogram<UnitDuration>](./histogrammedextendedlaunch.md)
  A histogram of the different amounts of time taken to launch the app, including the extended launch tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric/histogrammedapplicationresumetime)*