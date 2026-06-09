# enabledStateReportingDomains

**Framework**: MetricKit  
**Kind**: property

StateReporting domains enabled for metrics aggregation

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
final var enabledStateReportingDomains: Set<StateReportingDomain> { get }
```

#### Discussion

When set, metrics will be delivered with StateReporting stable state context, broken down by the application states recorded in the specified domains. This manager will receive metric entries matching the enabled domains as well as non-state-aggregated metric entries.

#### Example

```swift
let manager = MetricManager(enabledStateReportingDomains: [
    "com.myapp.gameplay",
    "com.myapp.experiments"
])

// Emit states using StateReporting directly
let reporter = StateReporter.reporter(for: "com.myapp.gameplay", stableState: GameState.self)

for await report in manager.metricReports {
    for entry in report.stateEntries {
        let domain = entry.state.domain
    }

    // Full day aggregate
    let fullDay = report.intervalEntries.fullDayEntry
}
```

## See Also

- [convenience init()](metricmanager/init.md)
  Creates a new `MetricManager` instance without state reporting domains.
- [init(enabledStateReportingDomains: Set<StateReportingDomain>)](metricmanager/init(enabledstatereportingdomains:).md)
  Creates a new `MetricManager` instance with state reporting domains enabled for metrics aggregation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/enabledstatereportingdomains)*