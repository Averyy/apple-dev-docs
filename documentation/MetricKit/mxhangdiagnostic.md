# MXHangDiagnostic

**Framework**: MetricKit  
**Kind**: class

An object representing a diagnostic report for an app that is too busy to handle user input responsively.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXHangDiagnostic
```

## Topics

### Reading total app hang time
- [var hangDuration: Measurement<UnitDuration>](mxhangdiagnostic/hangduration.md)
  The amount of time the app is busy and unable to respond to user interaction.
### Viewing the call stack
- [var callStackTree: MXCallStackTree](mxhangdiagnostic/callstacktree.md)
  The call stack for the app hang report.

## Relationships

### Inherits From
- [MXDiagnostic](mxdiagnostic.md)
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
- [class MXAppResponsivenessMetric](mxappresponsivenessmetric.md)
  An object representing metrics about the responsiveness of the app to user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxhangdiagnostic)*