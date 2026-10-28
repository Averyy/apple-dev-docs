# MetricResult

**Framework**: MetricKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents a single metric value from a metric report entry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
enum MetricResult
```

## Mentions

- [Analyzing app performance with MetricKit](./analyzing-app-performance-with-metrickit.md)

## Discussion

`MetricResult` unifies all metric types into a single enum. You receive `MetricResult` values by iterating the [`values`](./metricreport/intervalentry/values.md) array on a [`MetricReport.IntervalEntry`](./metricreport/intervalentry.md), or the [`values`](./metricreport/stateentry/values.md) array on a [`MetricReport.StateEntry`](./metricreport/stateentry.md).

```swift
for result in entry.values {
    switch result {
    case .cpuTime(let metric):
        process(metric)
    case .peakMemory(let metric):
        process(metric)
    case .hangTime(let metric):
        process(metric)
    @unknown default:
        break
    }
}
```

Use the [`metricGroup`](./metricresult/metricgroup.md) property to filter or categorize results without exhaustive switching when you only need a subset of metric types.

## Topics

### Metric group
- [var metricGroup: MetricGroup](./metricresult/metricgroup.md)
  The metric group this metric belongs to.
### Responsiveness and animation
- [case hangTime(HangTimeMetric)](./metricresult/hangtime%28_%29.md)
- [case hitchTime(HitchTimeMetric)](./metricresult/hitchtime%28_%29.md)
### App runtime
- [case foregroundTermination(ForegroundTerminationMetric)](./metricresult/foregroundtermination%28_%29.md)
- [case backgroundTermination(BackgroundTerminationMetric)](./metricresult/backgroundtermination%28_%29.md)
- [case totalForegroundTime(TotalForegroundTimeMetric)](./metricresult/totalforegroundtime%28_%29.md)
- [case totalBackgroundTime(TotalBackgroundTimeMetric)](./metricresult/totalbackgroundtime%28_%29.md)
- [case totalBackgroundAudioTime(TotalBackgroundAudioTimeMetric)](./metricresult/totalbackgroundaudiotime%28_%29.md)
- [case totalBackgroundLocationTime(TotalBackgroundLocationTimeMetric)](./metricresult/totalbackgroundlocationtime%28_%29.md)
- [case locationActivityTime(LocationActivityTimeMetric)](./metricresult/locationactivitytime%28_%29.md)
- [case signpostInterval(SignpostIntervalMetric)](./metricresult/signpostinterval%28_%29.md)
### CPU and memory
- [case cpuTime(CPUTimeMetric)](./metricresult/cputime%28_%29.md)
- [case cpuInstructionsCount(CPUInstructionsCountMetric)](./metricresult/cpuinstructionscount%28_%29.md)
- [case peakMemory(PeakMemoryMetric)](./metricresult/peakmemory%28_%29.md)
- [case suspendedMemory(SuspendedMemoryMetric)](./metricresult/suspendedmemory%28_%29.md)
### Network
- [case totalWiFiUpload(TotalWiFiUploadMetric)](./metricresult/totalwifiupload%28_%29.md)
- [case totalWiFiDownload(TotalWiFiDownloadMetric)](./metricresult/totalwifidownload%28_%29.md)
- [case totalCellularUpload(TotalCellularUploadMetric)](./metricresult/totalcellularupload%28_%29.md)
- [case totalCellularDownload(TotalCellularDownloadMetric)](./metricresult/totalcellulardownload%28_%29.md)
- [case cellularConditionTime(CellularConditionTimeMetric)](./metricresult/cellularconditiontime%28_%29.md)
### App launch
- [case timeToFirstDraw(TimeToFirstDrawMetric)](./metricresult/timetofirstdraw%28_%29.md)
- [case applicationResumeTime(ApplicationResumeTimeMetric)](./metricresult/applicationresumetime%28_%29.md)
- [case optimizedTimeToFirstDraw(OptimizedTimeToFirstDrawMetric)](./metricresult/optimizedtimetofirstdraw%28_%29.md)
- [case extendedLaunch(ExtendedLaunchMetric)](./metricresult/extendedlaunch%28_%29.md)
### Storage
- [case logicalDiskWrites(LogicalDiskWritesMetric)](./metricresult/logicaldiskwrites%28_%29.md)
- [case totalFileCount(TotalFileCountMetric)](./metricresult/totalfilecount%28_%29.md)
- [case totalFileSize(TotalFileSizeMetric)](./metricresult/totalfilesize%28_%29.md)
- [case totalDiskSpaceCapacity(TotalDiskSpaceCapacityMetric)](./metricresult/totaldiskspacecapacity%28_%29.md)
### Display and GPU
- [case pixelLuminance(PixelLuminanceMetric)](./metricresult/pixelluminance%28_%29.md)
- [case gpuTime(GPUTimeMetric)](./metricresult/gputime%28_%29.md)
- [case metalFrameRate(MetalFrameRateMetric)](./metricresult/metalframerate%28_%29.md)

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Result types
- [struct MetricGroup](./metricgroup.md)
  A value that identifies the category a metric belongs to.
- [enum DiagnosticResult](./diagnosticresult.md)
  An enumeration that represents a single diagnostic event from a diagnostic report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricresult)*