# MXAnimationMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about the responsiveness of animation in the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MXAnimationMetric
```

## Topics

### Reading the ratio of scrolling hitch time
- [var scrollHitchTimeRatio: Measurement<Unit>](mxanimationmetric/scrollhitchtimeratio.md)
  The ratio of the time spent hitching while scrolling.
### Reading the ratio of hitch time
- [var hitchTimeRatio: Measurement<Unit>](mxanimationmetric/hitchtimeratio.md)
  The ratio of time spent hitching during tracked animations.

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

- [class MXAppLaunchMetric](mxapplaunchmetric.md)
  An object representing metrics about app launch time.
- [class MXAppResponsivenessMetric](mxappresponsivenessmetric.md)
  An object representing metrics about the responsiveness of the app to user interaction.
- [struct MXLaunchTaskID](mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxanimationmetric)*