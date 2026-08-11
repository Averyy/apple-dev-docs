# stateEntries

**Framework**: MetricKit  
**Kind**: property

The state entries in this metric report, populated when state reporting is enabled.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
let stateEntries: [MetricReport.StateEntry]
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)
- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

`stateEntries` is only populated when the [`MetricManager`](metricmanager.md) was initialized with [`init(enabledStateReportingDomains:)`](metricmanager/init(enabledstatereportingdomains:).md). Each [`MetricReport.StateEntry`](metricreport/stateentry.md) contains metric values aggregated while the app was in a specific state, scoped to a specific [`MetricManager.ReportedState`](metricmanager/reportedstate.md).

Only a subset of metrics appear in state entries, including hang time, hitch time, app termination counts, signpost intervals, location activity time, and app runtime metrics. CPU time, memory, network, disk I/O, GPU, app launch, and disk space metrics appear only in [`intervalEntries`](metricreport/intervalentries.md).

Use `byStateReportingDomain` on the collection to group entries by domain:

```swift
let byDomain = report.stateEntries.byStateReportingDomain
if let sessionEntries = byDomain[StateReportingDomain(rawValue: "com.example.app.session")] {
    for entry in sessionEntries {
        print(entry.state.label, entry.values)
    }
}
```

## See Also

- [let intervalEntries: [MetricReport.IntervalEntry]](metricreport/intervalentries.md)
  The interval entries in this metric report, including the full-day aggregate.
- [static let encodingFormatKey: CodingUserInfoKey](metricreport/encodingformatkey.md)
  A `CodingUserInfoKey` for selecting the JSON encoding format of a metric report.
- [MetricReport.EncodingFormat](metricreport/encodingformat.md)
  A value that controls the JSON structure used when encoding a metric report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/stateentries)*