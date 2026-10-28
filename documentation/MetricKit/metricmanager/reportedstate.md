# MetricManager.ReportedState

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A recorded app state associated with a metric or diagnostic report entry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct ReportedState
```

## Discussion

`ReportedState` describes a single state that your app was in during a reporting interval. It carries the domain and label identifying the state, the duration the app spent in that state, and any stable context values your app recorded with the state.

Access reported states in metric reports through [`states`](../metricreport/intervalentry/states.md) or [`state`](../metricreport/stateentry/state.md). Access them in diagnostic reports through [`states`](../diagnosticreport/environment-swift.struct/states.md).

## Topics

### State details
- [let domain: String](./reportedstate/domain.md)
  The StateReporting domain this state belongs to
- [let label: String](./reportedstate/label.md)
  The state label
- [let duration: Measurement<UnitDuration>](./reportedstate/duration.md)
  The duration when the state was active during performance data collection.
### Instance Properties
- [let stableMetadata: [String : ReportableMetadataValue]](./reportedstate/stablemetadata.md)
  Context dictionary containing state-specific information

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/reportedstate)*