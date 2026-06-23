# CPUExceptionDiagnostic

**Framework**: MetricKit  
**Kind**: struct

A diagnostic for a fatal or nonfatal CPU exception.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct CPUExceptionDiagnostic
```

#### Discussion

CPU exceptions occur when your app consumes an excessive amount of CPU time in a short period. The diagnostic includes a [`CallStackTree`](callstacktree.md) to identify the responsible code path, along with `totalCPUTime` and `totalSampledTime` measurements.

This type replaces [`MXCPUExceptionDiagnostic`](mxcpuexceptiondiagnostic.md).

## Topics

### Call stack
- [let callStackTree: CallStackTree](cpuexceptiondiagnostic/callstacktree.md)
  The application call stack tree associated with the excessive CPU consumption.
### CPU exception details
- [let totalCPUTime: Measurement<UnitDuration>](cpuexceptiondiagnostic/totalcputime.md)
  Total CPU time consumed in the scope of this CPU exception.
- [let totalSampledTime: Measurement<UnitDuration>](cpuexceptiondiagnostic/totalsampledtime.md)
  Total time that the application was sampled for during the CPU exception.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CPUTimeMetric](cputimemetric.md)
  A metric that measures the total CPU time used by the app.
- [struct CPUInstructionsCountMetric](cpuinstructionscountmetric.md)
  A metric that measures the total number of CPU instructions the app executed.
- [struct PeakMemoryMetric](peakmemorymetric.md)
  A metric that measures peak memory footprint.
- [struct SuspendedMemoryMetric](suspendedmemorymetric.md)
  A metric that measures average suspended memory footprint with statistical data.
- [struct MemoryExceptionDiagnostic](memoryexceptiondiagnostic.md)
  A diagnostic MetricKit generates when your app or extension terminates because it exceeds the memory limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/cpuexceptiondiagnostic)*