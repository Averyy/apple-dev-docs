# init(enabledStateReportingDomains:)

**Framework**: MetricKit  
**Kind**: init

Creates a new `MetricManager` instance with state reporting domains enabled for metrics aggregation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
init(enabledStateReportingDomains: Set<StateReportingDomain>)
```

#### Discussion

Pass a set of [`StateReportingDomain`](statereportingdomain.md) values to enable state-contextualized metrics. When state reporting is enabled, the [`stateEntries`](metricreport/stateentries.md) property of each [`MetricReport`](metricreport.md) is populated with metric values segmented by each recorded app state.

```swift
let manager = MetricManager(
    enabledStateReportingDomains: ["com.example.app.session"]
)
```

Use [`init()`](metricmanager/init().md) if you don’t need per-state metrics.

## See Also

- [convenience init()](metricmanager/init.md)
  Creates a new `MetricManager` instance without state reporting domains.
- [var enabledStateReportingDomains: Set<StateReportingDomain>](metricmanager/enabledstatereportingdomains.md)
  StateReporting domains enabled for metrics aggregation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/init(enabledstatereportingdomains:))*