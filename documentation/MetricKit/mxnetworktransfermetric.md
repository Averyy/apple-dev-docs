# MXNetworkTransferMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about network transfers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXNetworkTransferMetric
```

## Topics

### Reading wireless data use
- [var cumulativeCellularDownload: Measurement<UnitInformationStorage>](mxnetworktransfermetric/cumulativecellulardownload.md)
  The total amount of data downloaded over the cellular connection.
- [var cumulativeCellularUpload: Measurement<UnitInformationStorage>](mxnetworktransfermetric/cumulativecellularupload.md)
  The total amount of data uploaded over the cellular connection.
- [var cumulativeWifiDownload: Measurement<UnitInformationStorage>](mxnetworktransfermetric/cumulativewifidownload.md)
  The total amount of data downloaded over the WiFi connection.
- [var cumulativeWifiUpload: Measurement<UnitInformationStorage>](mxnetworktransfermetric/cumulativewifiupload.md)
  The total amount of data uploaded over the WiFi connection.

## Relationships

### Inherits From
- [MXMetric](mxmetric.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MXCellularConditionMetric](mxcellularconditionmetric.md)
  An object representing metrics about the condition of the cellular network.
- [class MXCPUMetric](mxcpumetric.md)
  An object representing metrics about the use of the CPU.
- [class MXDisplayMetric](mxdisplaymetric.md)
  An object representing metrics about the power used to display the app on the screen.
- [class MXGPUMetric](mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXLocationActivityMetric](mxlocationactivitymetric.md)
  An object representing metrics about the use of location-tracking features of a device.
- [class MXCPUExceptionDiagnostic](mxcpuexceptiondiagnostic.md)
  An object representing a diagnostic report for a fatal or nonfatal CPU exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxnetworktransfermetric)*