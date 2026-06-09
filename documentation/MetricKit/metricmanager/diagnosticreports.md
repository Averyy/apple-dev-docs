# diagnosticReports

**Framework**: MetricKit  
**Kind**: property

An asynchronous sequence that delivers diagnostic reports as individual events.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var diagnosticReports: some AsyncSequence<DiagnosticReport, Never> { get }
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

Iterate `diagnosticReports` in a long-lived `Task` to receive [`DiagnosticReport`](diagnosticreport.md) values. Each iteration yields a single diagnostic event, such as a crash, hang, or CPU exception. The sequence never throws.

```swift
Task {
    for await report in manager.diagnosticReports {
        switch report.result {
        case .crash(let diagnostic): handleCrash(diagnostic)
        case .hang(let diagnostic): handleHang(diagnostic)
        @unknown default: break
        }
    }
}
```

## See Also

- [var metricReports: some AsyncSequence<MetricReport, Never>](metricmanager/metricreports.md)
  An asynchronous sequence that delivers daily metric reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/diagnosticreports)*