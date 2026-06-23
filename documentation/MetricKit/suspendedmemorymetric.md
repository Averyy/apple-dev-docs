# SuspendedMemoryMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures average suspended memory footprint with statistical data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct SuspendedMemoryMetric
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

This metric corresponds to the [`MetricResult.suspendedMemory(_:)`](metricresult/suspendedmemory(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

## Topics

### Measurements
- [let value: AverageStatistics<UnitInformationStorage>](suspendedmemorymetric/value.md)
  Average suspended memory footprint with statistical data.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [struct MemoryExceptionDiagnostic](memoryexceptiondiagnostic.md)
  A diagnostic MetricKit generates when your app or extension terminates because it exceeds the memory limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/suspendedmemorymetric)*