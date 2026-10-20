# MetricReport.IntervalEntry

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric entry that covers a specific time interval.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct IntervalEntry
```

## Mentions

- [Monitoring app performance with MetricKit](../monitoring-app-performance-with-metrickit.md)

#### Discussion

`IntervalEntry` contains all metric values for a given time interval. Access it through [`intervalEntries`](./intervalentries.md).

Use the [`fullDayEntry`](../../Swift/array/fulldayentry.md) convenience property on the collection to retrieve the entry with the full 24-hour aggregate:

```swift
let entry = report.intervalEntries.fullDayEntry
for result in entry.values {
    switch result {
    case .cpuTime(let metric): process(metric)
    @unknown default: break
    }
}
```

When you enable state reporting, `intervalEntries` contains shorter sub-interval entries in addition to the full-day entry.

Each `IntervalEntry` provides a `duration` but no start timestamp, so you can’t associate an entry with a specific time of day. To determine when the overall reporting period occurred, use `timeRange` on the parent [`MetricReport`](../metricreport.md).

## Topics

### Interval details
- [let duration: Measurement<UnitDuration>](./intervalentry/duration.md)
  The duration of this collection interval.
- [let states: [MetricManager.ReportedState]](./intervalentry/states.md)
  All states that were active during this collection interval.
### Metric values
- [let values: [MetricResult]](./intervalentry/values.md)
  The metric values for this entry.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/intervalentry)*