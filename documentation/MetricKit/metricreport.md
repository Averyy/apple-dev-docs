# MetricReport

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A daily performance report that contains metric values for your app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct MetricReport
```

## Mentions

- [Analyzing app performance with MetricKit](./analyzing-app-performance-with-metrickit.md)
- [Monitoring app performance with MetricKit](./monitoring-app-performance-with-metrickit.md)

#### Discussion

`MetricReport` is a value type that conforms to `Sendable` and `Codable`, so you can pass it across actor boundaries and serialize it with `JSONEncoder` directly.

Each report covers a 24-hour reporting period. Access metric data through [`intervalEntries`](./metricreport/intervalentries.md), which contains one or more [`MetricReport.IntervalEntry`](./metricreport/intervalentry.md) values. Use the [`MetricReport.IntervalEntry`](./metricreport/intervalentry.md) collection’s [`fullDayEntry`](../Swift/array/fulldayentry.md) property to retrieve the full-day aggregate, then iterate its [`values`](./metricreport/intervalentry/values.md) array and switch over each [`MetricResult`](./metricresult.md):

```swift
if let entry = report.intervalEntries.fullDayEntry {
    for result in entry.values {
        switch result {
        case .cpuTime(let metric):
            record(metric)
        case .peakMemory(let metric):
            record(metric)
        @unknown default:
            break
        }
    }
}
```

When state reporting is enabled via [`init(enabledStateReportingDomains:)`](./metricmanager/init%28enabledstatereportingdomains%29.md), the report also populates [`stateEntries`](./metricreport/stateentries.md) with [`MetricResult`](./metricresult.md) values scoped to each recorded app state. Only a subset of metric types appear in state entries, including hang time, hitch time, app termination counts, signpost intervals, and app runtime metrics. Metrics such as CPU time, memory, network, disk I/O, GPU, app launch, and disk space appear only in [`intervalEntries`](./metricreport/intervalentries.md).

## Topics

### Report details
- [let timeRange: DateInterval](./metricreport/timerange.md)
  The date interval this report covers.
- [let environment: MetricReport.Environment?](./metricreport/environment-swift.property.md)
  Environment context for the device and app.
### Metric data
- [let intervalEntries: [MetricReport.IntervalEntry]](./metricreport/intervalentries.md)
  The interval entries in this metric report, including the full-day aggregate.
- [let stateEntries: [MetricReport.StateEntry]](./metricreport/stateentries.md)
  The state entries in this metric report, populated when state reporting is enabled.
- [static let encodingFormatKey: CodingUserInfoKey](./metricreport/encodingformatkey.md)
  A `CodingUserInfoKey` for selecting the JSON encoding format of a metric report.
- [MetricReport.EncodingFormat](./metricreport/encodingformat.md)
  A value that controls the JSON structure used when encoding a metric report.
### Structures
- [MetricReport.Environment](./metricreport/environment-swift.struct.md)
  Device and app metadata associated with a metric report.
- [MetricReport.IntervalEntry](./metricreport/intervalentry.md)
  A metric entry that covers a specific time interval.
- [MetricReport.StateEntry](./metricreport/stateentry.md)
  A metric entry scoped to a specific recorded app state.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Metric and diagnostic reports
- [class MetricManager](./metricmanager.md)
  An object that delivers metric and diagnostic reports to your app.
- [struct DiagnosticReport](./diagnosticreport.md)
  A report describing a single diagnostic event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport)*