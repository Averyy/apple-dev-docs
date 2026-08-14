# MetricManager.ReportedState

**Framework**: MetricKit  
**Kind**: struct

A recorded app state associated with a metric or diagnostic report entry.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct ReportedState
```

#### Discussion

`ReportedState` describes a single state that your app was in during a reporting interval. It carries the domain and label identifying the state, the duration the app spent in that state, and any stable context values your app recorded with the state.

Access reported states in metric reports through [`states`](metricreport/intervalentry/states.md) or [`state`](metricreport/stateentry/state.md). Access them in diagnostic reports through [`states`](diagnosticreport/environment-swift.struct/states.md).

## Topics

### State details
- [let domain: String](metricmanager/reportedstate/domain.md)
  The StateReporting domain this state belongs to
- [let label: String](metricmanager/reportedstate/label.md)
  The state label
- [let duration: Measurement<UnitDuration>](metricmanager/reportedstate/duration.md)
  The duration when the state was active during performance data collection.
### Instance Properties
- [let stableMetadata: [String : ReportableMetadataValue]](metricmanager/reportedstate/stablemetadata.md)
  Context dictionary containing state-specific information

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/reportedstate)*