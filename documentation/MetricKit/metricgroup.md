# MetricGroup

**Framework**: MetricKit  
**Kind**: struct

A value that identifies the category a metric belongs to.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct MetricGroup
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

Use `MetricGroup` with [`metricGroup`](metricresult/metricgroup.md) to filter or group results without exhaustive switching. For example, to process only CPU-related metrics:

```swift
for result in entry.values where result.metricGroup == .cpu {
    // handle CPU metrics
}
```

## Topics

### Metric Groups
- [static let cpu: MetricGroup](metricgroup/cpu.md)
- [static let memory: MetricGroup](metricgroup/memory.md)
- [static let diskIO: MetricGroup](metricgroup/diskio.md)
- [static let networkTransfer: MetricGroup](metricgroup/networktransfer.md)
- [static let display: MetricGroup](metricgroup/display.md)
- [static let animation: MetricGroup](metricgroup/animation.md)
- [static let applicationResponsiveness: MetricGroup](metricgroup/applicationresponsiveness.md)
- [static let cellularCondition: MetricGroup](metricgroup/cellularcondition.md)
- [static let locationActivity: MetricGroup](metricgroup/locationactivity.md)
- [static let gpu: MetricGroup](metricgroup/gpu.md)
- [static let signpost: MetricGroup](metricgroup/signpost.md)
- [static let appLaunch: MetricGroup](metricgroup/applaunch.md)
- [static let appRuntime: MetricGroup](metricgroup/appruntime.md)
- [static let appTermination: MetricGroup](metricgroup/apptermination.md)
- [static let diskSpaceUsage: MetricGroup](metricgroup/diskspaceusage.md)
- [static let frameStatistics: MetricGroup](metricgroup/framestatistics.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum MetricResult](metricresult.md)
  An enumeration that represents a single metric value from a metric report entry.
- [enum DiagnosticResult](diagnosticresult.md)
  An enumeration that represents a single diagnostic event from a diagnostic report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricgroup)*