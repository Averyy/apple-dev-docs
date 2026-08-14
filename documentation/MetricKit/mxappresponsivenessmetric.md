# MXAppResponsivenessMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about the responsiveness of the app to user interaction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
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
- [class MXAppLaunchMetric](mxapplaunchmetric.md)
  An object representing metrics about app launch time.
- [struct MXLaunchTaskID](mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappresponsivenessmetric)*