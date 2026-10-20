# cumulativeCellularDownload

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total amount of data downloaded over the cellular connection.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`TotalCellularDownloadMetric`](../totalcellulardownloadmetric.md) instead.

## Declaration

```swift
var cumulativeCellularDownload: Measurement<UnitInformationStorage> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitInformationStorage *> * cumulativeCellularDownload;
```

## See Also

### Reading wireless data use
- [var cumulativeCellularUpload: Measurement<UnitInformationStorage>](./cumulativecellularupload.md)
  The total amount of data uploaded over the cellular connection.
- [var cumulativeWifiDownload: Measurement<UnitInformationStorage>](./cumulativewifidownload.md)
  The total amount of data downloaded over the WiFi connection.
- [var cumulativeWifiUpload: Measurement<UnitInformationStorage>](./cumulativewifiupload.md)
  The total amount of data uploaded over the WiFi connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxnetworktransfermetric/cumulativecellulardownload)*