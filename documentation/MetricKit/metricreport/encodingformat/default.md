# MetricReport.EncodingFormat.default

**Framework**: MetricKit  
**Kind**: case

Default format with state entries and interval entries as arrays.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
case `default`
```

#### Discussion

State entries are provided as an array, interval entries are provided as an array with states as arrays within each entry.

## See Also

- [MetricReport.EncodingFormat.byStateReportingDomain](metricreport/encodingformat/bystatereportingdomain.md)
  Format with entries organized by StateReporting domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/encodingformat/default)*