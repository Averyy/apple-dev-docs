# MXAppResponsivenessMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about the responsiveness of the app to user interaction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MXAppResponsivenessMetric
```

## Topics

### Viewing application unresponsive durations
- [var histogrammedApplicationHangTime: MXHistogram<UnitDuration>](mxappresponsivenessmetric/histogrammedapplicationhangtime.md)
  A histogram of the different durations of time in which the app is too busy to handle user interaction responsively.

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
- [class MXAppLaunchMetric](mxapplaunchmetric.md)
  An object representing metrics about app launch time.
- [class MXHangDiagnostic](mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappresponsivenessmetric)*