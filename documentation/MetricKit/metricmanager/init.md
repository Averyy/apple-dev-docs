# init()

**Framework**: MetricKit  
**Kind**: init

Creates a new `MetricManager` instance without state reporting domains.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init()
```

#### Discussion

Use this initializer when you only need interval-based metric data and diagnostic reports, without per-state metrics. Hold the returned instance in a property for as long as you need reports:

```swift
let manager = MetricManager()
```

To receive metrics segmented by app state, use [`init(enabledStateReportingDomains:)`](metricmanager/init(enabledstatereportingdomains:).md) instead.

## See Also

- [init(enabledStateReportingDomains: Set<StateReportingDomain>)](metricmanager/init(enabledstatereportingdomains:).md)
  Creates a new `MetricManager` instance with state reporting domains enabled for metrics aggregation.
- [var enabledStateReportingDomains: Set<StateReportingDomain>](metricmanager/enabledstatereportingdomains.md)
  StateReporting domains enabled for metrics aggregation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/init())*