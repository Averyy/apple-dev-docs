# MXAppLaunchMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about app launch time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXAppLaunchMetric
```

## Topics

### Viewing app launch and resume time
- [var histogrammedOptimizedTimeToFirstDraw: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedoptimizedtimetofirstdraw.md)
  A histogram of the different amounts of time associated with prewarmed app launches.
- [var histogrammedTimeToFirstDraw: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedtimetofirstdraw.md)
  A histogram of the different amounts of time taken to launch the app.
- [var histogrammedApplicationResumeTime: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedapplicationresumetime.md)
  A histogram of the different amounts of time taken to resume the app from the background.
- [var histogrammedExtendedLaunch: MXHistogram<UnitDuration>](mxapplaunchmetric/histogrammedextendedlaunch.md)
  A histogram of the different amounts of time taken to launch the app, including the extended launch tasks.

## Relationships

### Inherits From
- [MXMetric](mxmetric.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MXAnimationMetric](mxanimationmetric.md)
  An object representing metrics about the responsiveness of animation in the app.
- [class MXAppResponsivenessMetric](mxappresponsivenessmetric.md)
  An object representing metrics about the responsiveness of the app to user interaction.
- [class MXHangDiagnostic](mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric)*