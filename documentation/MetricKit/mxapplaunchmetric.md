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
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MXAnimationMetric](mxanimationmetric.md)
  An object representing metrics about the responsiveness of animation in the app.
- [class MXAppResponsivenessMetric](mxappresponsivenessmetric.md)
  An object representing metrics about the responsiveness of the app to user interaction.
- [struct MXLaunchTaskID](mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric)*