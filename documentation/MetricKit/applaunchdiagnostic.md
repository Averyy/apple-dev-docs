# AppLaunchDiagnostic

**Framework**: MetricKit  
**Kind**: struct

A diagnostic report for an app launch.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct AppLaunchDiagnostic
```

#### Discussion

This captures a [`CallStackTree`](callstacktree.md) and a `launchDuration` measurement for app launches that exceed the diagnostic threshold.

## Topics

### Call stack
- [let callStackTree: CallStackTree](applaunchdiagnostic/callstacktree.md)
  The application call stack tree associated with the launch issue.
### Launch details
- [let launchDuration: Measurement<UnitDuration>](applaunchdiagnostic/launchduration.md)
  Duration of the launch that triggered this diagnostic.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CrashDiagnostic](crashdiagnostic.md)
  A diagnostic report that describes a crash that occurred.
- [struct HangDiagnostic](hangdiagnostic.md)
  A diagnostic for an app that was too busy to handle user input responsively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/applaunchdiagnostic)*