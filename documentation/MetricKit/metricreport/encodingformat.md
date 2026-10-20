# MetricReport.EncodingFormat

**Framework**: MetricKit  
**Kind**: enum  
**Role**: Enumeration

A value that controls the JSON structure used when encoding a metric report.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
enum EncodingFormat
```

#### Discussion

Set [`encodingFormatKey`](./encodingformatkey.md) in a `JSONEncoder`’s `userInfo` dictionary to choose the encoding format before archiving reports:

```swift
let encoder = JSONEncoder()
encoder.userInfo[MetricReport.encodingFormatKey] = MetricReport.EncodingFormat.byStateReportingDomain
let data = try encoder.encode(report)
```

The `.byStateReportingDomain` format organizes metric values by [`MetricGroup`](../metricgroup.md), which can be more convenient for log pipelines that process one category at a time.

## Topics

### Encoding formats
- [MetricReport.EncodingFormat.default](./encodingformat/default.md)
  Default format with state entries and interval entries as arrays.
- [MetricReport.EncodingFormat.byStateReportingDomain](./encodingformat/bystatereportingdomain.md)
  Format with entries organized by StateReporting domain.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Metric data
- [let intervalEntries: [MetricReport.IntervalEntry]](./intervalentries.md)
  The interval entries in this metric report, including the full-day aggregate.
- [let stateEntries: [MetricReport.StateEntry]](./stateentries.md)
  The state entries in this metric report, populated when state reporting is enabled.
- [static let encodingFormatKey: CodingUserInfoKey](./encodingformatkey.md)
  A `CodingUserInfoKey` for selecting the JSON encoding format of a metric report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/encodingformat)*