# states

**Framework**: MetricKit  
**Kind**: property

All states that were active leading up to this diagnostic event.

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

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)
- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

This array contains all the StateReporting states that occurred before the diagnostic event. The array may be empty if no StateReporting context was active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/diagnosticreport/environment-swift.struct/states)*