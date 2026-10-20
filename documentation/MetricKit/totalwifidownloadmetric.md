# TotalWiFiDownloadMetric

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric that measures the total data downloaded over WiFi.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct TotalWiFiDownloadMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalWiFiDownload(_:)`](./metricresult/totalwifidownload%28_%29.md) case. It appears only in [`intervalEntries`](./metricreport/intervalentries.md) and is not included in state entries.

## Topics

### Measurements
- [let value: Measurement<UnitInformationStorage>](./totalwifidownloadmetric/value.md)
  The total amount of data downloaded over the WiFi connection.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Network metrics
- [struct TotalWiFiUploadMetric](./totalwifiuploadmetric.md)
  A metric that measures the total data uploaded over WiFi.
- [struct TotalCellularUploadMetric](./totalcellularuploadmetric.md)
  A metric that measures the total data uploaded over a cellular connection.
- [struct TotalCellularDownloadMetric](./totalcellulardownloadmetric.md)
  A metric that measures the total data downloaded over a cellular connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalwifidownloadmetric)*