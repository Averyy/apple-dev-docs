# MXAnimationMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about the responsiveness of animation in the app.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`HitchTimeMetric`](./hitchtimemetric.md) case instead.

## Declaration

```swift
class MXAnimationMetric
```

```objc
@interface MXAnimationMetric : MXMetric
```

## Topics

### Reading the ratio of scrolling hitch time
- [var scrollHitchTimeRatio: Measurement<Unit>](./mxanimationmetric/scrollhitchtimeratio.md)
  The ratio of the time spent hitching while scrolling.
### Reading the ratio of hitch time
- [var hitchTimeRatio: Measurement<Unit>](./mxanimationmetric/hitchtimeratio.md)
  The ratio of time spent hitching during tracked animations.

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
- [class MXAppLaunchMetric](./mxapplaunchmetric.md)
  An object representing metrics about app launch time.
- [class MXAppResponsivenessMetric](./mxappresponsivenessmetric.md)
  An object representing metrics about the responsiveness of the app to user interaction.
- [struct MXLaunchTaskID](./mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxanimationmetric)*