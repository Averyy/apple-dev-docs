# MXCPUExceptionDiagnostic

**Framework**: MetricKit  
**Kind**: class

An object representing a diagnostic report for a fatal or nonfatal CPU exception.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXCPUExceptionDiagnostic
```

#### Overview

A CPU exception occurs when your app uses an excessive amount of CPU time over a short period.

## Topics

### Viewing the call stack
- [var callStackTree: MXCallStackTree](mxcpuexceptiondiagnostic/callstacktree.md)
  The app call stack associated with the CPU exception.
### Viewing app CPU time
- [var totalCPUTime: Measurement<UnitDuration>](mxcpuexceptiondiagnostic/totalcputime.md)
  The total CPU time used during the exception.
- [var totalSampledTime: Measurement<UnitDuration>](mxcpuexceptiondiagnostic/totalsampledtime.md)
  The total time the app was sampled during the exception.

## Relationships

### Inherits From
- [MXDiagnostic](mxdiagnostic.md)
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
- [class MXNetworkTransferMetric](mxnetworktransfermetric.md)
  An object representing metrics about network transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpuexceptiondiagnostic)*