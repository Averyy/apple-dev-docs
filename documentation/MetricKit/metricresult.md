# MetricResult

**Framework**: MetricKit  
**Kind**: enum

An enumeration that represents a single metric value from a metric report entry.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
enum MetricResult
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

`MetricResult` unifies all metric types into a single enum. You receive `MetricResult` values by iterating the [`values`](metricreport/intervalentry/values.md) array on a [`MetricReport.IntervalEntry`](metricreport/intervalentry.md), or the [`values`](metricreport/stateentry/values.md) array on a [`MetricReport.StateEntry`](metricreport/stateentry.md).

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

Use the [`metricGroup`](metricresult/metricgroup.md) property to filter or categorize results without exhaustive switching when you only need a subset of metric types.

## Topics

### Metric group
- [var metricGroup: MetricGroup](metricresult/metricgroup.md)
  The metric group this metric belongs to.
### Responsiveness and animation
- [case hangTime(HangTimeMetric)](metricresult/hangtime(_:).md)
- [case hitchTime(HitchTimeMetric)](metricresult/hitchtime(_:).md)
- [case scrollHitchTime(ScrollHitchTimeMetric)](metricresult/scrollhitchtime(_:).md)
### App runtime
- [case foregroundTermination(ForegroundTerminationMetric)](metricresult/foregroundtermination(_:).md)
- [case backgroundTermination(BackgroundTerminationMetric)](metricresult/backgroundtermination(_:).md)
- [case totalForegroundTime(TotalForegroundTimeMetric)](metricresult/totalforegroundtime(_:).md)
- [case totalBackgroundTime(TotalBackgroundTimeMetric)](metricresult/totalbackgroundtime(_:).md)
- [case totalBackgroundAudioTime(TotalBackgroundAudioTimeMetric)](metricresult/totalbackgroundaudiotime(_:).md)
- [case totalBackgroundLocationTime(TotalBackgroundLocationTimeMetric)](metricresult/totalbackgroundlocationtime(_:).md)
- [case locationActivityTime(LocationActivityTimeMetric)](metricresult/locationactivitytime(_:).md)
- [case signpostInterval(SignpostIntervalMetric)](metricresult/signpostinterval(_:).md)
### CPU and memory
- [case cpuTime(CPUTimeMetric)](metricresult/cputime(_:).md)
- [case cpuInstructionsCount(CPUInstructionsCountMetric)](metricresult/cpuinstructionscount(_:).md)
- [case peakMemory(PeakMemoryMetric)](metricresult/peakmemory(_:).md)
- [case suspendedMemory(SuspendedMemoryMetric)](metricresult/suspendedmemory(_:).md)
### Network
- [case totalWiFiUpload(TotalWiFiUploadMetric)](metricresult/totalwifiupload(_:).md)
- [case totalWiFiDownload(TotalWiFiDownloadMetric)](metricresult/totalwifidownload(_:).md)
- [case totalCellularUpload(TotalCellularUploadMetric)](metricresult/totalcellularupload(_:).md)
- [case totalCellularDownload(TotalCellularDownloadMetric)](metricresult/totalcellulardownload(_:).md)
- [case cellularConditionTime(CellularConditionTimeMetric)](metricresult/cellularconditiontime(_:).md)
### App launch
- [case timeToFirstDraw(TimeToFirstDrawMetric)](metricresult/timetofirstdraw(_:).md)
- [case applicationResumeTime(ApplicationResumeTimeMetric)](metricresult/applicationresumetime(_:).md)
- [case optimizedTimeToFirstDraw(OptimizedTimeToFirstDrawMetric)](metricresult/optimizedtimetofirstdraw(_:).md)
- [case extendedLaunch(ExtendedLaunchMetric)](metricresult/extendedlaunch(_:).md)
### Storage
- [case logicalDiskWrites(LogicalDiskWritesMetric)](metricresult/logicaldiskwrites(_:).md)
- [case totalFileCount(TotalFileCountMetric)](metricresult/totalfilecount(_:).md)
- [case totalFileSize(TotalFileSizeMetric)](metricresult/totalfilesize(_:).md)
- [case totalDiskSpaceCapacity(TotalDiskSpaceCapacityMetric)](metricresult/totaldiskspacecapacity(_:).md)
### Display and GPU
- [case pixelLuminance(PixelLuminanceMetric)](metricresult/pixelluminance(_:).md)
- [case gpuTime(GPUTimeMetric)](metricresult/gputime(_:).md)
- [case metalFrameRate(MetalFrameRateMetric)](metricresult/metalframerate(_:).md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MetricGroup](metricgroup.md)
  A value that identifies the category a metric belongs to.
- [enum DiagnosticResult](diagnosticresult.md)
  An enumeration that represents a single diagnostic event from a diagnostic report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricresult)*