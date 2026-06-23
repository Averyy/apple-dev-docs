# CPUTimeMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the total CPU time used by the app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct CPUTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.cpuTime(_:)`](metricresult/cputime(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

## Topics

### Measurements
- [let value: Measurement<UnitDuration>](cputimemetric/value.md)
  The total amount of CPU the app used.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CPUInstructionsCountMetric](cpuinstructionscountmetric.md)
  A metric that measures the total number of CPU instructions the app executed.
- [struct CPUExceptionDiagnostic](cpuexceptiondiagnostic.md)
  A diagnostic for a fatal or nonfatal CPU exception.
- [struct PeakMemoryMetric](peakmemorymetric.md)
  A metric that measures peak memory footprint.
- [struct SuspendedMemoryMetric](suspendedmemorymetric.md)
  A metric that measures average suspended memory footprint with statistical data.
- [struct MemoryExceptionDiagnostic](memoryexceptiondiagnostic.md)
  A diagnostic MetricKit generates when your app or extension terminates because it exceeds the memory limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/cputimemetric)*