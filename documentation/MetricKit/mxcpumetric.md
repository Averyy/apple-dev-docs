# MXCPUMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about the use of the CPU.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`CPUTimeMetric`](./cputimemetric.md) or [`CPUInstructionsCountMetric`](./cpuinstructionscountmetric.md) cases instead.

## Declaration

```swift
class MXCPUMetric
```

```objc
@interface MXCPUMetric : MXMetric
```

## Topics

### Reading CPU use
- [var cumulativeCPUTime: Measurement<UnitDuration>](./mxcpumetric/cumulativecputime.md)
  The total amount of CPU the app used.
- [var cumulativeCPUInstructions: Measurement<Unit>](./mxcpumetric/cumulativecpuinstructions.md)
  The total number of CPU instructions the app executed during the reporting period.

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
- [class MXDisplayMetric](./mxdisplaymetric.md)
  An object representing metrics about the power used to display the app on the screen.
- [class MXGPUMetric](./mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXLocationActivityMetric](./mxlocationactivitymetric.md)
  An object representing metrics about the use of location-tracking features of a device.
- [class MXNetworkTransferMetric](./mxnetworktransfermetric.md)
  An object representing metrics about network transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpumetric)*