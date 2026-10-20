# AppLaunchDiagnostic

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A diagnostic report for an app launch.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct AppLaunchDiagnostic
```

#### Discussion

This captures a [`CallStackTree`](./callstacktree.md) and a `launchDuration` measurement for app launches that exceed the diagnostic threshold.

## Topics

### Call stack
- [let callStackTree: CallStackTree](./applaunchdiagnostic/callstacktree.md)
  The application call stack tree associated with the launch issue.
### Launch details
- [let launchDuration: Measurement<UnitDuration>](./applaunchdiagnostic/launchduration.md)
  Duration of the launch that triggered this diagnostic.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Crash and hang diagnostics
- [struct CrashDiagnostic](./crashdiagnostic.md)
  A diagnostic report that describes a crash that occurred.
- [struct HangDiagnostic](./hangdiagnostic.md)
  A diagnostic for an app that was too busy to handle user input responsively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/applaunchdiagnostic)*