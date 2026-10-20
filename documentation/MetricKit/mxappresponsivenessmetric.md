# MXAppResponsivenessMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about the responsiveness of the app to user interaction.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`HangTimeMetric`](./hangtimemetric.md) case instead.

## Declaration

```swift
class MXAppResponsivenessMetric
```

```objc
@interface MXAppResponsivenessMetric : MXMetric
```

## Topics

### Viewing application unresponsive durations
- [var histogrammedApplicationHangTime: MXHistogram<UnitDuration>](./mxappresponsivenessmetric/histogrammedapplicationhangtime.md)
  A histogram of the different durations of time in which the app is too busy to handle user interaction responsively.

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
- [class MXAppLaunchMetric](./mxapplaunchmetric.md)
  An object representing metrics about app launch time.
- [struct MXLaunchTaskID](./mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappresponsivenessmetric)*