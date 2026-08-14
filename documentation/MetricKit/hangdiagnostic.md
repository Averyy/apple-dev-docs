# HangDiagnostic

**Framework**: MetricKit  
**Kind**: struct

A diagnostic for an app that was too busy to handle user input responsively.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct HangDiagnostic
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

This carries a [`CallStackTree`](callstacktree.md) captured at the time of the hang, and a `hangDuration` measurement that reports how long the main thread was blocked.

## Topics

### Call stack
- [let callStackTree: CallStackTree](hangdiagnostic/callstacktree.md)
  The application call stack tree associated with the hang.
### Hang details
- [let hangDuration: Measurement<UnitDuration>](hangdiagnostic/hangduration.md)
  Total hang duration for this diagnostic.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct CrashDiagnostic](crashdiagnostic.md)
  A diagnostic report that describes a crash that occurred.
- [struct AppLaunchDiagnostic](applaunchdiagnostic.md)
  A diagnostic report for an app launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/hangdiagnostic)*