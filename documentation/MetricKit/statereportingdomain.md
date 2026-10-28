# StateReportingDomain

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A value that identifies a reporting scope for segmenting metric data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct StateReportingDomain
```

## Mentions

- [Monitoring app performance with MetricKit](./monitoring-app-performance-with-metrickit.md)

## Discussion

`StateReportingDomain` is `RawRepresentable` and `ExpressibleByStringLiteral`, so create values using string literals. Use reverse DNS notation to avoid naming collisions:

```swift
let manager = MetricManager(
    enabledStateReportingDomains: ["com.example.app.session"]
)
```

Pass a set of `StateReportingDomain` values to [`init(enabledStateReportingDomains:)`](./metricmanager/init%28enabledstatereportingdomains%29.md) to receive metrics segmented by each domain’s recorded states. Use `StateReporter.reporter(for:stableMetadata:)` from the `StateReporting` framework to obtain a `StateReporter`. Call `reportTransition(to:stableMetadata:)` on it to emit state transitions for MetricKit to aggregate.

## Relationships

### Conforms To
- [CodingKeyRepresentable](../Swift/codingkeyrepresentable.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### App state reporting
- [struct LaunchTaskID](./launchtaskid.md)
  An identifier for a task measured as part of an extended app launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/statereportingdomain)*