# MXMetricManager API

**Framework**: MetricKit

Measure app performance and diagnostics using MXMetricManager and related types.

## Topics

### Metric and diagnostic reports
- [class MXMetricManager](mxmetricmanager.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- [class MXMetricPayload](mxmetricpayload.md)
  An object that encapsulates a daily metrics report.
- [class MXDiagnosticPayload](mxdiagnosticpayload.md)
  An object that encapsulates a diagnostic report.
- [protocol MXMetricManagerSubscriber](mxmetricmanagersubscriber.md)
  A protocol defining a method for receiving a daily metrics report.
### Battery and resource metrics
- [class MXCellularConditionMetric](mxcellularconditionmetric.md)
  An object representing metrics about the condition of the cellular network.
- [class MXCPUMetric](mxcpumetric.md)
  An object representing metrics about the use of the CPU.
- [class MXDisplayMetric](mxdisplaymetric.md)
  An object representing metrics about the power used to display the app on the screen.
- [class MXGPUMetric](mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXLocationActivityMetric](mxlocationactivitymetric.md)
  An object representing metrics about the use of location-tracking features of a device.
- [class MXNetworkTransferMetric](mxnetworktransfermetric.md)
  An object representing metrics about network transfers.
### App performance metrics
- [class MXAppRunTimeMetric](mxappruntimemetric.md)
  An object representing metrics about the amount of time the app is active.
- [class MXAppExitMetric](mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXForegroundExitData](mxforegroundexitdata.md)
  An object representing counts for the different types of foreground app exits.
- [class MXBackgroundExitData](mxbackgroundexitdata.md)
  An object representing counts for the different types of background app exits.
- [class MXMemoryMetric](mxmemorymetric.md)
  An object representing metrics about the app’s memory use.
### Responsiveness metrics
- [class MXAnimationMetric](mxanimationmetric.md)
  An object representing metrics about the responsiveness of animation in the app.
- [class MXAppLaunchMetric](mxapplaunchmetric.md)
  An object representing metrics about app launch time.
- [class MXAppResponsivenessMetric](mxappresponsivenessmetric.md)
  An object representing metrics about the responsiveness of the app to user interaction.
- [struct MXLaunchTaskID](mxlaunchtaskid.md)
  The task identifier to track launch measurements.
### Disk metrics
- [class MXDiskIOMetric](mxdiskiometric.md)
  An object representing metrics about disk usage.
- [class MXDiskSpaceUsageMetric](mxdiskspaceusagemetric.md)
  An object representing metrics about your app’s disk space usage.
### Performance diagnostics
- [class MXAppLaunchDiagnostic](mxapplaunchdiagnostic.md)
  A diagnostic subclass that encapsulates app launch diagnostic reports.
- [class MXCPUExceptionDiagnostic](mxcpuexceptiondiagnostic.md)
  An object representing a diagnostic report for a fatal or nonfatal CPU exception.
- [class MXCrashDiagnostic](mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.
- [class MXHangDiagnostic](mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.
- [class MXDiskWriteExceptionDiagnostic](mxdiskwriteexceptiondiagnostic.md)
  An object representing a diagnostic report for a disk write exception.
### Signpost metrics
- [class MXSignpostMetric](mxsignpostmetric.md)
  An object representing a custom metric.
- [class MXSignpostIntervalData](mxsignpostintervaldata.md)
  A data object representing the captured data for a custom metric.
- [func mxSignpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpost(_:dso:log:name:signpostid:_:_:).md)
  Posts a single custom metric, the start time of a custom metric, or the end time of a custom metric to the log system.
- [func mxSignpostAnimationIntervalBegin(dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpostanimationintervalbegin(dso:log:name:signpostid:_:_:).md)
  Posts the start time of an animation interval to the log system.
### Supporting types
- [class MXCallStackTree](mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](mxmetadata.md)
  An object containing system-level information about the device.
- [class MXAverage](mxaverage.md)
  A unit of measure for an average.
- [class MXHistogram](mxhistogram.md)
  An object representing a histogram of data values of the same type of unit.
- [class MXHistogramBucket](mxhistogrambucket.md)
  An object representing a bucket of data in a histogram.
- [class MXDiagnostic](mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [class MXMetric](mxmetric.md)
  An abstract data class for a metric.
- [struct MXError](mxerror.md)
  Error domain for error handling of app metrics.
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.
- [class MXUnitAveragePixelLuminance](mxunitaveragepixelluminance.md)
  A unit of measure of pixel luminosity on an OLED display.
- [class MXUnitSignalBars](mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager-api)*