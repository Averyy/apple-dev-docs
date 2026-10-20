# MXAppLaunchMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about app launch time.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`TimeToFirstDrawMetric`](./timetofirstdrawmetric.md), [`OptimizedTimeToFirstDrawMetric`](./optimizedtimetofirstdrawmetric.md), [`ApplicationResumeTimeMetric`](./applicationresumetimemetric.md), or [`ExtendedLaunchMetric`](./extendedlaunchmetric.md) cases instead.

## Declaration

```swift
class MXAppLaunchMetric
```

```objc
@interface MXAppLaunchMetric : MXMetric
```

## Topics

### Viewing app launch and resume time
- [var histogrammedOptimizedTimeToFirstDraw: MXHistogram<UnitDuration>](./mxapplaunchmetric/histogrammedoptimizedtimetofirstdraw.md)
  A histogram of the different amounts of time associated with prewarmed app launches.
- [var histogrammedTimeToFirstDraw: MXHistogram<UnitDuration>](./mxapplaunchmetric/histogrammedtimetofirstdraw.md)
  A histogram of the different amounts of time taken to launch the app.
- [var histogrammedApplicationResumeTime: MXHistogram<UnitDuration>](./mxapplaunchmetric/histogrammedapplicationresumetime.md)
  A histogram of the different amounts of time taken to resume the app from the background.
- [var histogrammedExtendedLaunch: MXHistogram<UnitDuration>](./mxapplaunchmetric/histogrammedextendedlaunch.md)
  A histogram of the different amounts of time taken to launch the app, including the extended launch tasks.

## Relationships

### Inherits From
- [MXMetric](./mxmetric.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Responsiveness metrics
- [class MXAnimationMetric](./mxanimationmetric.md)
  An object representing metrics about the responsiveness of animation in the app.
- [class MXAppResponsivenessMetric](./mxappresponsivenessmetric.md)
  An object representing metrics about the responsiveness of the app to user interaction.
- [struct MXLaunchTaskID](./mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric)*