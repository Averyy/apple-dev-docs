# MXNetworkTransferMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about network transfers.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`TotalWiFiDownloadMetric`](./totalwifidownloadmetric.md), [`TotalWiFiUploadMetric`](./totalwifiuploadmetric.md), [`TotalCellularDownloadMetric`](./totalcellulardownloadmetric.md), or [`TotalCellularUploadMetric`](./totalcellularuploadmetric.md) cases instead.

## Declaration

```swift
class MXNetworkTransferMetric
```

```objc
@interface MXNetworkTransferMetric : MXMetric
```

## Topics

### Reading wireless data use
- [var cumulativeCellularDownload: Measurement<UnitInformationStorage>](./mxnetworktransfermetric/cumulativecellulardownload.md)
  The total amount of data downloaded over the cellular connection.
- [var cumulativeCellularUpload: Measurement<UnitInformationStorage>](./mxnetworktransfermetric/cumulativecellularupload.md)
  The total amount of data uploaded over the cellular connection.
- [var cumulativeWifiDownload: Measurement<UnitInformationStorage>](./mxnetworktransfermetric/cumulativewifidownload.md)
  The total amount of data downloaded over the WiFi connection.
- [var cumulativeWifiUpload: Measurement<UnitInformationStorage>](./mxnetworktransfermetric/cumulativewifiupload.md)
  The total amount of data uploaded over the WiFi connection.

## Relationships

### Inherits From
- [MXMetric](./mxmetric.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Battery and resource metrics
- [class MXCellularConditionMetric](./mxcellularconditionmetric.md)
  An object representing metrics about the condition of the cellular network.
- [class MXCPUMetric](./mxcpumetric.md)
  An object representing metrics about the use of the CPU.
- [class MXDisplayMetric](./mxdisplaymetric.md)
  An object representing metrics about the power used to display the app on the screen.
- [class MXGPUMetric](./mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXLocationActivityMetric](./mxlocationactivitymetric.md)
  An object representing metrics about the use of location-tracking features of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxnetworktransfermetric)*