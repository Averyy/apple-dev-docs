# TotalWiFiUploadMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the total data uploaded over WiFi.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct TotalWiFiUploadMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalWiFiUpload(_:)`](metricresult/totalwifiupload(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

## Topics

### Measurements
- [let value: Measurement<UnitInformationStorage>](totalwifiuploadmetric/value.md)
  The total amount of data uploaded over the WiFi connection.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct TotalWiFiDownloadMetric](totalwifidownloadmetric.md)
  A metric that measures the total data downloaded over WiFi.
- [struct TotalCellularUploadMetric](totalcellularuploadmetric.md)
  A metric that measures the total data uploaded over a cellular connection.
- [struct TotalCellularDownloadMetric](totalcellulardownloadmetric.md)
  A metric that measures the total data downloaded over a cellular connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalwifiuploadmetric)*