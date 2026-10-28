# init(enabledStateReportingDomains:)

**Framework**: MetricKit  
**Kind**: init  
**Role**: Initializer

Creates a new `MetricManager` instance with state reporting domains enabled for metrics aggregation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
init(enabledStateReportingDomains: Set<StateReportingDomain>)
```

## Discussion

Pass a set of [`StateReportingDomain`](../statereportingdomain.md) values to enable state-contextualized metrics. When state reporting is enabled, the [`stateEntries`](../metricreport/stateentries.md) property of each [`MetricReport`](../metricreport.md) is populated with metric values segmented by each recorded app state.

```swift
let manager = MetricManager(
    enabledStateReportingDomains: ["com.example.app.session"]
)
```

Use [`init()`](./init%28%29.md) if you don’t need per-state metrics.

## See Also

### Initialization
- [convenience init()](./init%28%29.md)
  Creates a new `MetricManager` instance without state reporting domains.
- [var enabledStateReportingDomains: Set<StateReportingDomain>](./enabledstatereportingdomains.md)
  StateReporting domains enabled for metrics aggregation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/init(enabledstatereportingdomains:))*