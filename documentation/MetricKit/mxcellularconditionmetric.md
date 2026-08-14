# MXCellularConditionMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about the condition of the cellular network.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXCellularConditionMetric
```

## Topics

### Viewing cellular connectivity metrics
- [var histogrammedCellularConditionTime: MXHistogram<MXUnitSignalBars>](mxcellularconditionmetric/histogrammedcellularconditiontime.md)
  An object representing the distribution of the different levels of connectivity to the cellular network.
- [class MXUnitSignalBars](mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.

## Relationships

### Inherits From
- [MXMetric](mxmetric.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MXCPUMetric](mxcpumetric.md)
  An object representing metrics about the use of the CPU.
- [class MXDisplayMetric](mxdisplaymetric.md)
  An object representing metrics about the power used to display the app on the screen.
- [class MXGPUMetric](mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXLocationActivityMetric](mxlocationactivitymetric.md)
  An object representing metrics about the use of location-tracking features of a device.
- [class MXNetworkTransferMetric](mxnetworktransfermetric.md)
  An object representing metrics about network transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcellularconditionmetric)*