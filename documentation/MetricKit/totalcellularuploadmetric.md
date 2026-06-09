# TotalCellularUploadMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the total data uploaded over a cellular connection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct TotalCellularUploadMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalCellularUpload(_:)`](metricresult/totalcellularupload(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

This value covers all cellular data regardless of whether the connection used LTE, 5G, or another technology.

This type replaces the `cumulativeCellularUpload` property of [`MXNetworkTransferMetric`](mxnetworktransfermetric.md).

## Topics

### Measurements
- [let value: Measurement<UnitInformationStorage>](totalcellularuploadmetric/value.md)
  The total amount of data uploaded over the cellular connection.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct TotalWiFiUploadMetric](totalwifiuploadmetric.md)
  A metric that measures the total data uploaded over WiFi.
- [struct TotalWiFiDownloadMetric](totalwifidownloadmetric.md)
  A metric that measures the total data downloaded over WiFi.
- [struct TotalCellularDownloadMetric](totalcellulardownloadmetric.md)
  A metric that measures the total data downloaded over a cellular connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalcellularuploadmetric)*