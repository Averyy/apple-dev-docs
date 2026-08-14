# intervalEntries

**Framework**: MetricKit  
**Kind**: property

The interval entries in this metric report, including the full-day aggregate.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
let intervalEntries: [MetricReport.IntervalEntry]
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

Use the [`fullDayEntry`](https://developer.apple.com/documentation/swift/array/fulldayentry) convenience property on the collection to access the entry covering the entire 24-hour reporting period. This is the entry with the longest [`duration`](metricreport/intervalentry/duration.md):

```swift
let entry = report.intervalEntries.fullDayEntry
for result in entry.values {
    switch result {
    case .cpuTime(let metric): process(metric)
    @unknown default: break
    }
}
```

When state reporting is enabled, `intervalEntries` may also include shorter sub-interval entries alongside the full-day entry. Use `byStateReportingDomain` on the collection to group all states across all interval entries by domain.

## See Also

- [let stateEntries: [MetricReport.StateEntry]](metricreport/stateentries.md)
  The state entries in this metric report, populated when state reporting is enabled.
- [static let encodingFormatKey: CodingUserInfoKey](metricreport/encodingformatkey.md)
  A `CodingUserInfoKey` for selecting the JSON encoding format of a metric report.
- [MetricReport.EncodingFormat](metricreport/encodingformat.md)
  A value that controls the JSON structure used when encoding a metric report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/intervalentries)*