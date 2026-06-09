# MemoryExceptionDiagnostic

**Framework**: MetricKit  
**Kind**: struct

A diagnostic for a fatal memory exception.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct MemoryExceptionDiagnostic
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

## Topics

### Call stack
- [let callStackTree: CallStackTree](memoryexceptiondiagnostic/callstacktree.md)
  The call stack tree that caused the memory exception.

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
- [struct CPUExceptionDiagnostic](cpuexceptiondiagnostic.md)
  A diagnostic for a fatal or nonfatal CPU exception.
- [struct PeakMemoryMetric](peakmemorymetric.md)
  A metric that measures peak memory footprint.
- [struct SuspendedMemoryMetric](suspendedmemorymetric.md)
  A metric that measures average suspended memory footprint with statistical data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/memoryexceptiondiagnostic)*