# metricReports

**Framework**: MetricKit  
**Kind**: property

An asynchronous sequence that delivers daily metric reports.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
final var metricReports: some AsyncSequence<MetricReport, Never> { get }
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

Iterate `metricReports` in a long-lived `Task` to receive [`MetricReport`](metricreport.md) values as they become available. The sequence never throws.

```swift
Task {
    for await report in manager.metricReports {
        process(report)
    }
}
```

## See Also

- [var diagnosticReports: some AsyncSequence<DiagnosticReport, Never>](metricmanager/diagnosticreports.md)
  An asynchronous sequence that delivers diagnostic reports as individual events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/metricreports)*