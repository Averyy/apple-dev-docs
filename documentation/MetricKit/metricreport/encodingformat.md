# MetricReport.EncodingFormat

**Framework**: MetricKit  
**Kind**: enum

A value that controls the JSON structure used when encoding a metric report.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
enum EncodingFormat
```

#### Discussion

Set [`encodingFormatKey`](metricreport/encodingformatkey.md) in a `JSONEncoder`’s `userInfo` dictionary to choose the encoding format before archiving reports:

```swift
let encoder = JSONEncoder()
encoder.userInfo[MetricReport.encodingFormatKey] = MetricReport.EncodingFormat.byStateReportingDomain
let data = try encoder.encode(report)
```

The `.byStateReportingDomain` format organizes metric values by [`MetricGroup`](metricgroup.md), which can be more convenient for log pipelines that process one category at a time.

## Topics

### Encoding formats
- [MetricReport.EncodingFormat.default](metricreport/encodingformat/default.md)
  Default format with state entries and interval entries as arrays.
- [MetricReport.EncodingFormat.byStateReportingDomain](metricreport/encodingformat/bystatereportingdomain.md)
  Format with entries organized by StateReporting domain.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let intervalEntries: [MetricReport.IntervalEntry]](metricreport/intervalentries.md)
  The interval entries in this metric report, including the full-day aggregate.
- [let stateEntries: [MetricReport.StateEntry]](metricreport/stateentries.md)
  The state entries in this metric report, populated when state reporting is enabled.
- [static let encodingFormatKey: CodingUserInfoKey](metricreport/encodingformatkey.md)
  A `CodingUserInfoKey` for selecting the JSON encoding format of a metric report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/encodingformat)*