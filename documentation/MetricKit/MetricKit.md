# MetricKit

**Framework**: MetricKit  
**Kind**: module

Aggregate and analyze per-device reports on exception and crash diagnostics and on power and performance metrics.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 12.0+
- visionOS 1.0+

#### Overview

With MetricKit, you can receive on-device app diagnostics and power and performance metrics the system captures. The system delivers metric reports about the previous 24 hours to a registered app at most once per day, and delivers diagnostic reports immediately in iOS 15 and later and macOS 12 and later. This framework supports diagnostics for crashes, hangs, energy, and disk writes for apps running in visionOS but doesn’t report metrics for apps running in visionOS. This includes apps built for visionOS or compatible iPhone and iPad apps running in visionOS.

Use the data in the reports to help improve the performance of your iOS app, macOS app, or Mac app built with Mac Catalyst. The framework includes the following:

- A manager class and a subscriber protocol
- Payload classes for reported data
- Classes for each category of metrics and diagnostics
- Classes for measurement units, such as bars of cellular connectivity
- Classes for representing accumulated data, such as histograms
- A class for capturing stack traces in diagnostics

## Topics

### Essentials
- [class MXMetricManager](mxmetricmanager.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- [class MXMetricPayload](mxmetricpayload.md)
  An object that encapsulates a daily metrics report.
- [class MXDiagnosticPayload](mxdiagnosticpayload.md)
  An object that encapsulates a diagnostic report.
- [protocol MXMetricManagerSubscriber](mxmetricmanagersubscriber.md)
  A protocol defining a method for receiving a daily metrics report.
### Performance improvements
- [Improving your app’s performance](../Xcode/improving-your-app-s-performance.md)
  Model, measure, and boost the performance of your app by using a continuous-improvement cycle.
### Battery metrics
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
- [class MXCPUExceptionDiagnostic](mxcpuexceptiondiagnostic.md)
  An object representing a diagnostic report for a fatal or nonfatal CPU exception.
### Performance metrics
- [class MXAppLaunchDiagnostic](mxapplaunchdiagnostic.md)
  A diagnostic subclass that encapsulates app launch diagnostic reports.
- [class MXAppExitMetric](mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXAppRunTimeMetric](mxappruntimemetric.md)
  An object representing metrics about the amount of time the app is active.
- [class MXMemoryMetric](mxmemorymetric.md)
  An object representing metrics about the app’s memory use.
- [class MXCrashDiagnostic](mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.
### Responsiveness metrics
- [class MXAnimationMetric](mxanimationmetric.md)
  An object representing metrics about the responsiveness of animation in the app.
- [class MXAppLaunchMetric](mxapplaunchmetric.md)
  An object representing metrics about app launch time.
- [class MXAppResponsivenessMetric](mxappresponsivenessmetric.md)
  An object representing metrics about the responsiveness of the app to user interaction.
- [class MXHangDiagnostic](mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.
### Disk usage metrics
- [class MXDiskIOMetric](mxdiskiometric.md)
  An object representing metrics about disk usage.
- [class MXDiskSpaceUsageMetric](mxdiskspaceusagemetric.md)
  An object representing metrics about your app’s disk space usage.
- [class MXDiskWriteExceptionDiagnostic](mxdiskwriteexceptiondiagnostic.md)
  An object representing a diagnostic report for a disk write exception.
### Custom metrics
- [class MXSignpostMetric](mxsignpostmetric.md)
  An object representing a custom metric.
### Data types
- [class MXCallStackTree](mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](mxmetadata.md)
  An object containing system-level information about the device.
- [class MXAverage](mxaverage.md)
  A unit of measure for an average.
- [class MXHistogram](mxhistogram.md)
  An object representing a histogram of data values of the same type of unit.
- [class MXDiagnostic](mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [class MXMetric](mxmetric.md)
  An abstract data class for a metric.
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
- [struct MXError](mxerror.md)
  Error domain for error handling of app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MetricKit)*