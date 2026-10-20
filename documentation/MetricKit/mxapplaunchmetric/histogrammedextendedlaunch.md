# histogrammedExtendedLaunch

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

A histogram of the different amounts of time taken to launch the app, including the extended launch tasks.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- macOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`ExtendedLaunchMetric`](../extendedlaunchmetric.md) instead.

## Declaration

```swift
var histogrammedExtendedLaunch: MXHistogram<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) MXHistogram<NSUnitDuration *> * histogrammedExtendedLaunch;
```

## See Also

### Viewing app launch and resume time
- [var histogrammedOptimizedTimeToFirstDraw: MXHistogram<UnitDuration>](./histogrammedoptimizedtimetofirstdraw.md)
  A histogram of the different amounts of time associated with prewarmed app launches.
- [var histogrammedTimeToFirstDraw: MXHistogram<UnitDuration>](./histogrammedtimetofirstdraw.md)
  A histogram of the different amounts of time taken to launch the app.
- [var histogrammedApplicationResumeTime: MXHistogram<UnitDuration>](./histogrammedapplicationresumetime.md)
  A histogram of the different amounts of time taken to resume the app from the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric/histogrammedextendedlaunch)*