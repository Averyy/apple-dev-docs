# MemoryExceptionDiagnostic

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A diagnostic MetricKit generates when your app or extension terminates because it exceeds the memory limit.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
struct MemoryExceptionDiagnostic
```

## Mentions

- [Analyzing app performance with MetricKit](./analyzing-app-performance-with-metrickit.md)

## Topics

### Call stack
- [let callStackTree: CallStackTree](./memoryexceptiondiagnostic/callstacktree.md)
  The call stack tree that caused the memory exception.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### CPU and memory metrics
- [struct CPUTimeMetric](./cputimemetric.md)
  A metric that measures the total CPU time used by the app.
- [struct CPUInstructionsCountMetric](./cpuinstructionscountmetric.md)
  A metric that measures the total number of CPU instructions the app executed.
- [struct CPUExceptionDiagnostic](./cpuexceptiondiagnostic.md)
  A diagnostic for a fatal or nonfatal CPU exception.
- [struct PeakMemoryMetric](./peakmemorymetric.md)
  A metric that measures peak memory footprint.
- [struct SuspendedMemoryMetric](./suspendedmemorymetric.md)
  A metric that measures average suspended memory footprint with statistical data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/memoryexceptiondiagnostic)*