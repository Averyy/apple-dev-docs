# MetricReport.StateEntry

**Framework**: MetricKit  
**Kind**: struct

A metric entry scoped to a specific recorded app state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct StateEntry
```

#### Discussion

`StateEntry` is only present when state reporting is enabled via [`init(enabledStateReportingDomains:)`](metricmanager/init(enabledstatereportingdomains:).md). Access state entries through [`stateEntries`](metricreport/stateentries.md).

Each entry corresponds to one [`MetricManager.ReportedState`](metricmanager/reportedstate.md) and contains the metric values aggregated while the app was in that state. Only a subset of metrics appear in state entries, including hang time, hitch time, app termination counts, signpost intervals, location activity time, and app runtime metrics.

## Topics

### State details
- [let state: MetricManager.ReportedState](metricreport/stateentry/state.md)
  StateReporting information during which this entry was collected.
### Metric values
- [let values: [MetricResult]](metricreport/stateentry/values.md)
  The metric values for this entry.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/stateentry)*