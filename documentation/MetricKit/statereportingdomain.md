# StateReportingDomain

**Framework**: MetricKit  
**Kind**: struct

A value that identifies a reporting scope for segmenting metric data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct StateReportingDomain
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

`StateReportingDomain` is `RawRepresentable` and `ExpressibleByStringLiteral`, so create values using string literals. Use reverse DNS notation to avoid naming collisions:

```swift
let manager = MetricManager(
    enabledStateReportingDomains: ["com.example.app.session"]
)
```

Pass a set of `StateReportingDomain` values to [`init(enabledStateReportingDomains:)`](metricmanager/init(enabledstatereportingdomains:).md) to receive metrics segmented by each domain’s recorded states. Use `StateReporter.reporter(for:stableMetadata:)` from the `StateReporting` framework to obtain a `StateReporter`. Call `reportTransition(to:stableMetadata:)` on it to emit state transitions for MetricKit to aggregate.

## Relationships

### Conforms To
- [CodingKeyRepresentable](../Swift/CodingKeyRepresentable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct LaunchTaskID](launchtaskid.md)
  An identifier for a task measured as part of an extended app launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/statereportingdomain)*