# MXCellularConditionMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about the condition of the cellular network.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`CellularConditionTimeMetric`](./cellularconditiontimemetric.md) case instead.

## Declaration

```swift
class MXCellularConditionMetric
```

```objc
@interface MXCellularConditionMetric : MXMetric
```

## Topics

### Viewing cellular connectivity metrics
- [var histogrammedCellularConditionTime: MXHistogram<MXUnitSignalBars>](./mxcellularconditionmetric/histogrammedcellularconditiontime.md)
  An object representing the distribution of the different levels of connectivity to the cellular network.
- [class MXUnitSignalBars](./mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.

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
- [class MXCPUMetric](./mxcpumetric.md)
  An object representing metrics about the use of the CPU.
- [class MXDisplayMetric](./mxdisplaymetric.md)
  An object representing metrics about the power used to display the app on the screen.
- [class MXGPUMetric](./mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXLocationActivityMetric](./mxlocationactivitymetric.md)
  An object representing metrics about the use of location-tracking features of a device.
- [class MXNetworkTransferMetric](./mxnetworktransfermetric.md)
  An object representing metrics about network transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcellularconditionmetric)*