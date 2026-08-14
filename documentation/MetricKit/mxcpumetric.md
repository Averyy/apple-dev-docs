# MXCPUMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about the use of the CPU.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXCPUMetric
```

## Topics

### Reading CPU use
- [var cumulativeCPUTime: Measurement<UnitDuration>](mxcpumetric/cumulativecputime.md)
  The total amount of CPU the app used.
- [var cumulativeCPUInstructions: Measurement<Unit>](mxcpumetric/cumulativecpuinstructions.md)
  The total number of CPU instructions the app executed during the reporting period.

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

- [class MXCellularConditionMetric](mxcellularconditionmetric.md)
  An object representing metrics about the condition of the cellular network.
- [class MXDisplayMetric](mxdisplaymetric.md)
  An object representing metrics about the power used to display the app on the screen.
- [class MXGPUMetric](mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXLocationActivityMetric](mxlocationactivitymetric.md)
  An object representing metrics about the use of location-tracking features of a device.
- [class MXNetworkTransferMetric](mxnetworktransfermetric.md)
  An object representing metrics about network transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpumetric)*