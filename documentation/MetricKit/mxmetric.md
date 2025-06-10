# MXMetric

**Framework**: MetricKit  
**Kind**: class

An abstract data class for a metric.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXMetric
```

## Topics

### Generate a report
- [func dictionaryRepresentation() -> [AnyHashable : Any]](mxmetric/dictionaryrepresentation.md)
  Returns the contents of a metric as a dictionary.
- [func jsonRepresentation() -> Data](mxmetric/jsonrepresentation.md)
  Returns the contents of the metric in JSON format.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MXAnimationMetric](mxanimationmetric.md)
- [MXAppExitMetric](mxappexitmetric.md)
- [MXAppLaunchMetric](mxapplaunchmetric.md)
- [MXAppResponsivenessMetric](mxappresponsivenessmetric.md)
- [MXAppRunTimeMetric](mxappruntimemetric.md)
- [MXCPUMetric](mxcpumetric.md)
- [MXCellularConditionMetric](mxcellularconditionmetric.md)
- [MXDiskIOMetric](mxdiskiometric.md)
- [MXDiskSpaceUsageMetric](mxdiskspaceusagemetric.md)
- [MXDisplayMetric](mxdisplaymetric.md)
- [MXGPUMetric](mxgpumetric.md)
- [MXLocationActivityMetric](mxlocationactivitymetric.md)
- [MXMemoryMetric](mxmemorymetric.md)
- [MXNetworkTransferMetric](mxnetworktransfermetric.md)
- [MXSignpostMetric](mxsignpostmetric.md)
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

- [class MXCallStackTree](mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](mxmetadata.md)
  An object containing system-level information about the device.
- [class MXAverage](mxaverage.md)
  A unit of measure for an average.
- [class MXHistogram](mxhistogram.md)
  An object representing a histogram of data values of the same type of unit.
- [class MXDiagnostic](mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
- [struct MXError](mxerror.md)
  Error domain for error handling of app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetric)*