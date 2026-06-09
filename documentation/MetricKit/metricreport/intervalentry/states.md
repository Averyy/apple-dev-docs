# states

**Framework**: MetricKit  
**Kind**: property

All states that were active during this collection interval.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
let states: [MetricManager.ReportedState]
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

This array contains all the StateReporting states that occurred within the interval. The array may be empty if no StateReporting context was active during the interval.

## See Also

- [let duration: Measurement<UnitDuration>](metricreport/intervalentry/duration.md)
  The duration of this collection interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/intervalentry/states)*