# MetricKit

**Framework**: MetricKit  
**Kind**: module

Measure your app’s performance using daily metric and diagnostic reports from real users.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 12.0+
- visionOS 1.0+

#### Overview

MetricKit provides on-device app diagnostics and power and performance metrics the system captures. The system delivers metric reports about the previous 24 hours to your app at most once per day. Diagnostic reports arrive immediately in iOS 15 and later, and macOS 12 and later. For apps running in visionOS, the framework supports diagnostics for crashes, hangs, high energy use, and disk writes, but doesn’t report performance metrics. This applies to apps built for visionOS and compatible iPhone and iPad apps running in visionOS.

Use this data to improve the performance of your iOS app, macOS app, or Mac Catalyst app.

In iOS 27 and later and macOS 27 and later, [`MetricManager`](metricmanager.md) delivers [`MetricReport`](metricreport.md) and [`DiagnosticReport`](diagnosticreport.md) values through asynchronous sequences. On visionOS 27 and later, [`MetricManager`](metricmanager.md) delivers diagnostic reports only. MetricKit also supports tracking state-based metrics using the [`StateReporting`](https://developer.apple.com/documentation/StateReporting) framework.

## Topics

### Essentials
- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)
  Receive daily performance and diagnostic reports from real device usage.
- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)
  Work with the metric values, diagnostic data, and environments in MetricKit reports.
- [Track performance by app state using MetricKit](track-performance-by-app-state-using-metrickit.md)
  Collect performance metrics, diagnostic reports, and experiment data related to your app’s current state using the MetricKit framework.
### Performance improvements
- [Improving your app’s performance](../Xcode/improving-your-app-s-performance.md)
  Model, measure, and boost the performance of your app by using a continuous-improvement cycle.
### Metric and diagnostic reports
- [class MetricManager](metricmanager.md)
  An object that delivers metric and diagnostic reports to your app.
- [struct MetricReport](metricreport.md)
  A daily performance report that contains metric values for your app.
- [struct DiagnosticReport](diagnosticreport.md)
  A report describing a single diagnostic event.
### Result types
- [enum MetricResult](metricresult.md)
  An enumeration that represents a single metric value from a metric report entry.
- [struct MetricGroup](metricgroup.md)
  A value that identifies the category a metric belongs to.
- [enum DiagnosticResult](diagnosticresult.md)
  An enumeration that represents a single diagnostic event from a diagnostic report.
### Time-in-use metrics
- [struct TotalForegroundTimeMetric](totalforegroundtimemetric.md)
  A metric that measures the total time the app spent in the foreground.
- [struct TotalBackgroundTimeMetric](totalbackgroundtimemetric.md)
  A metric that measures the total time the app spent active in the background.
- [struct TotalBackgroundAudioTimeMetric](totalbackgroundaudiotimemetric.md)
  A metric that measures the total time the app spent in the background playing audio.
- [struct TotalBackgroundLocationTimeMetric](totalbackgroundlocationtimemetric.md)
  A metric that measures the total time the app spent in the background using location services.
- [struct LocationActivityTimeMetric](locationactivitytimemetric.md)
  A metric that measures time spent using location services at each accuracy level.
- [struct CellularConditionTimeMetric](cellularconditiontimemetric.md)
  A metric that measures time spent at each cellular signal strength.
### Launch and responsiveness metrics
- [struct TimeToFirstDrawMetric](timetofirstdrawmetric.md)
  A metric that measures time to first draw durations for app launches.
- [struct OptimizedTimeToFirstDrawMetric](optimizedtimetofirstdrawmetric.md)
  A metric that measures optimized time to first draw durations for app launches.
- [struct ApplicationResumeTimeMetric](applicationresumetimemetric.md)
  A metric that measures app resume time durations.
- [struct ExtendedLaunchMetric](extendedlaunchmetric.md)
  A metric that measures extended launch task durations.
- [struct HangTimeMetric](hangtimemetric.md)
  A metric that measures app hang time.
- [struct HitchTimeMetric](hitchtimemetric.md)
  A metric that measures animation hitch time.
### CPU and memory metrics
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
- [struct MemoryExceptionDiagnostic](memoryexceptiondiagnostic.md)
  A diagnostic MetricKit generates when your app or extension terminates because it exceeds the memory limit.
### GPU and display metrics
- [struct GPUTimeMetric](gputimemetric.md)
  A metric that measures the total GPU time used by the app.
- [struct MetalFrameRateMetric](metalframeratemetric.md)
  A metric that measures Metal frame rate statistics for a specific `CAMetalLayer`.
- [struct PixelLuminanceMetric](pixelluminancemetric.md)
  A metric that measures the average luminosity of pixels on an OLED display.
- [class AveragePixelLuminance](averagepixelluminance.md)
  A unit for average pixel luminance measurements.
### Network metrics
- [struct TotalWiFiUploadMetric](totalwifiuploadmetric.md)
  A metric that measures the total data uploaded over WiFi.
- [struct TotalWiFiDownloadMetric](totalwifidownloadmetric.md)
  A metric that measures the total data downloaded over WiFi.
- [struct TotalCellularUploadMetric](totalcellularuploadmetric.md)
  A metric that measures the total data uploaded over a cellular connection.
- [struct TotalCellularDownloadMetric](totalcellulardownloadmetric.md)
  A metric that measures the total data downloaded over a cellular connection.
### Disk metrics
- [struct LogicalDiskWritesMetric](logicaldiskwritesmetric.md)
  A metric that measures the total data written to disk.
- [struct DiskWriteExceptionDiagnostic](diskwriteexceptiondiagnostic.md)
  A diagnostic for a disk write exception.
- [struct TotalDiskSpaceCapacityMetric](totaldiskspacecapacitymetric.md)
  A metric that measures disk capacity and usage on the device.
- [struct TotalFileCountMetric](totalfilecountmetric.md)
  A metric that measures the number of files attributed to the app.
- [struct TotalFileSizeMetric](totalfilesizemetric.md)
  A metric that measures the sizes of files attributed to the app.
### Termination metrics
- [struct ForegroundTerminationMetric](foregroundterminationmetric.md)
  A metric that counts app terminations from the foreground by category.
- [struct BackgroundTerminationMetric](backgroundterminationmetric.md)
  A metric that counts app terminations from the background by category.
### Signpost and custom metrics
- [struct SignpostIntervalMetric](signpostintervalmetric.md)
  A metric that measures the duration and count of custom signpost intervals.
- [func mxSignpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpost(_:dso:log:name:signpostid:_:_:).md)
  Posts a single custom metric, the start time of a custom metric, or the end time of a custom metric to the log system.
- [func mxSignpostAnimationIntervalBegin(dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpostanimationintervalbegin(dso:log:name:signpostid:_:_:).md)
  Posts the start time of an animation interval to the log system.
### Crash and hang diagnostics
- [struct CrashDiagnostic](crashdiagnostic.md)
  A diagnostic report that describes a crash that occurred.
- [struct HangDiagnostic](hangdiagnostic.md)
  A diagnostic for an app that was too busy to handle user input responsively.
- [struct AppLaunchDiagnostic](applaunchdiagnostic.md)
  A diagnostic report for an app launch.
### App state reporting
- [struct StateReportingDomain](statereportingdomain.md)
  A value that identifies a reporting scope for segmenting metric data.
- [struct LaunchTaskID](launchtaskid.md)
  An identifier for a task measured as part of an extended app launch.
### Call stack data
- [struct CallStackTree](callstacktree.md)
  A tree structure representing a collection of call stacks captured during a diagnostic event.
- [struct CallStackThread](callstackthread.md)
  A single stack thread within a call stack tree.
- [struct CallStackFrame](callstackframe.md)
  A single frame within a call stack thread.
- [struct SignpostRecord](signpostrecord.md)
  A record of a signpost event associated with a diagnostic report.
### Supporting types
- [struct Histogram](histogram.md)
  A distribution of values organized into buckets.
- [struct AverageStatistics](averagestatistics.md)
  A value that encapsulates an average measurement with supporting statistical data.
- [class SignalBars](signalbars.md)
  A unit for cellular signal strength measurements in bars.
- [class HitchTimeRatio](hitchtimeratio.md)
  A unit for animation hitch time ratio measurements.
- [struct OSVersion](osversion.md)
  The version of the operating system on the device.
### MXMetricManager API
- [MXMetricManager API](mxmetricmanager-api.md)
  Measure app performance and diagnostics using MXMetricManager and related types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MetricKit)*