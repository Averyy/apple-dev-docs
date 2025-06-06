# histogrammedApplicationResumeTime

**Framework**: MetricKit  
**Kind**: property

A histogram of the different amounts of time taken to resume the app from the background.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var histogrammedApplicationResumeTime: MXHistogram<UnitDuration> { get }
```

## See Also

- [var histogrammedOptimizedTimeToFirstDraw: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedoptimizedtimetofirstdraw.md)
  A histogram of the different amounts of time associated with prewarmed app launches.
- [var histogrammedTimeToFirstDraw: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedtimetofirstdraw.md)
  A histogram of the different amounts of time taken to launch the app.
- [var histogrammedExtendedLaunch: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedextendedlaunch.md)
  A histogram of the different amounts of time taken to launch the app, including the extended launch tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric/histogrammedapplicationresumetime)*