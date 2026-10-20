# TotalCellularUploadMetric

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric that measures the total data uploaded over a cellular connection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
struct TotalCellularUploadMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalCellularUpload(_:)`](./metricresult/totalcellularupload%28_%29.md) case. It appears only in [`intervalEntries`](./metricreport/intervalentries.md) and is not included in state entries.

This value covers all cellular data regardless of whether the connection used LTE, 5G, or another technology.

## Topics

### Measurements
- [let value: Measurement<UnitInformationStorage>](./totalcellularuploadmetric/value.md)
  The total amount of data uploaded over the cellular connection.

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
- [struct TotalWiFiDownloadMetric](./totalwifidownloadmetric.md)
  A metric that measures the total data downloaded over WiFi.
- [struct TotalCellularDownloadMetric](./totalcellulardownloadmetric.md)
  A metric that measures the total data downloaded over a cellular connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalcellularuploadmetric)*