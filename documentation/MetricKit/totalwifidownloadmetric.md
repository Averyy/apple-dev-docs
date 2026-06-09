# TotalWiFiDownloadMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the total data downloaded over WiFi.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct TotalWiFiDownloadMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalWiFiDownload(_:)`](metricresult/totalwifidownload(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

This type replaces the `cumulativeWifiDownload` property of [`MXNetworkTransferMetric`](mxnetworktransfermetric.md).

## Topics

### Measurements
- [let value: Measurement<UnitInformationStorage>](totalwifidownloadmetric/value.md)
  The total amount of data downloaded over the WiFi connection.

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
- [struct TotalCellularUploadMetric](totalcellularuploadmetric.md)
  A metric that measures the total data uploaded over a cellular connection.
- [struct TotalCellularDownloadMetric](totalcellulardownloadmetric.md)
  A metric that measures the total data downloaded over a cellular connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalwifidownloadmetric)*