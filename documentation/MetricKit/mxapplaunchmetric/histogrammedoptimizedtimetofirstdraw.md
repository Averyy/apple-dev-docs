# histogrammedOptimizedTimeToFirstDraw

**Framework**: MetricKit  
**Kind**: property

A histogram of the different amounts of time associated with prewarmed app launches.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- macOS 12.2+
- visionOS 1.0+

## Declaration

```swift
var histogrammedOptimizedTimeToFirstDraw: MXHistogram<UnitDuration> { get }
```

## See Also

- [var histogrammedTimeToFirstDraw: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedtimetofirstdraw.md)
  A histogram of the different amounts of time taken to launch the app.
- [var histogrammedApplicationResumeTime: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedapplicationresumetime.md)
  A histogram of the different amounts of time taken to resume the app from the background.
- [var histogrammedExtendedLaunch: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedextendedlaunch.md)
  A histogram of the different amounts of time taken to launch the app, including the extended launch tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric/histogrammedoptimizedtimetofirstdraw)*