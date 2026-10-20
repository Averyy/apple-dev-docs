# states

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

All states that were active during this collection interval.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
let states: [MetricManager.ReportedState]
```

## Mentions

- [Monitoring app performance with MetricKit](../../monitoring-app-performance-with-metrickit.md)

#### Discussion

This array contains all the StateReporting states that occurred within the interval. The array may be empty if no StateReporting context was active during the interval.

## See Also

### Interval details
- [let duration: Measurement<UnitDuration>](./duration.md)
  The duration of this collection interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/intervalentry/states)*