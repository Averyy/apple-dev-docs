# histogrammedExtendedLaunch

**Framework**: MetricKit  
**Kind**: property

A histogram of the different amounts of time taken to launch the app, including the extended launch tasks.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var histogrammedExtendedLaunch: MXHistogram<UnitDuration> { get }
```

## See Also

- [var histogrammedOptimizedTimeToFirstDraw: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedoptimizedtimetofirstdraw.md)
  A histogram of the different amounts of time associated with prewarmed app launches.
- [var histogrammedTimeToFirstDraw: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedtimetofirstdraw.md)
  A histogram of the different amounts of time taken to launch the app.
- [var histogrammedApplicationResumeTime: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedapplicationresumetime.md)
  A histogram of the different amounts of time taken to resume the app from the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric/histogrammedextendedlaunch)*