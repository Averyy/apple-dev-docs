# PeakMemoryMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures peak memory footprint.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct PeakMemoryMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.peakMemory(_:)`](metricresult/peakmemory(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

## Topics

### Measurements
- [let value: Measurement<UnitInformationStorage>](peakmemorymetric/value.md)
  Peak memory footprint.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct CPUTimeMetric](cputimemetric.md)
  A metric that measures the total CPU time used by the app.
- [struct CPUInstructionsCountMetric](cpuinstructionscountmetric.md)
  A metric that measures the total number of CPU instructions the app executed.
- [struct CPUExceptionDiagnostic](cpuexceptiondiagnostic.md)
  A diagnostic for a fatal or nonfatal CPU exception.
- [struct SuspendedMemoryMetric](suspendedmemorymetric.md)
  A metric that measures average suspended memory footprint with statistical data.
- [struct MemoryExceptionDiagnostic](memoryexceptiondiagnostic.md)
  A diagnostic MetricKit generates when your app or extension terminates because it exceeds the memory limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/peakmemorymetric)*