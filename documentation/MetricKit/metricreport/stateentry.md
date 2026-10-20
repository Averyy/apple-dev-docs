# MetricReport.StateEntry

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric entry scoped to a specific recorded app state.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct StateEntry
```

#### Discussion

`StateEntry` is only present when state reporting is enabled via [`init(enabledStateReportingDomains:)`](../metricmanager/init%28enabledstatereportingdomains%29.md). Access state entries through [`stateEntries`](./stateentries.md).

Each entry corresponds to one [`MetricManager.ReportedState`](../metricmanager/reportedstate.md) and contains the metric values aggregated while the app was in that state. Only a subset of metrics appear in state entries, including hang time, hitch time, app termination counts, signpost intervals, location activity time, and app runtime metrics.

## Topics

### State details
- [let state: MetricManager.ReportedState](./stateentry/state.md)
  StateReporting information during which this entry was collected.
### Metric values
- [let values: [MetricResult]](./stateentry/values.md)
  The metric values for this entry.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/stateentry)*