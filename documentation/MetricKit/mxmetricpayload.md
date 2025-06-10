# MXMetricPayload

**Framework**: MetricKit  
**Kind**: class

An object that encapsulates a daily metrics report.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXMetricPayload
```

## Topics

### Reading battery metrics
- [var cellularConditionMetrics: MXCellularConditionMetric?](mxmetricpayload/cellularconditionmetrics.md)
  The cellular condition measurements for the reporting period.
- [var cpuMetrics: MXCPUMetric?](mxmetricpayload/cpumetrics.md)
  The CPU metrics for the reporting period.
- [var displayMetrics: MXDisplayMetric?](mxmetricpayload/displaymetrics.md)
  The display metrics for the reporting period.
- [var gpuMetrics: MXGPUMetric?](mxmetricpayload/gpumetrics.md)
  The GPU metrics for the reporting period.
- [var locationActivityMetrics: MXLocationActivityMetric?](mxmetricpayload/locationactivitymetrics.md)
  The location-tracking activity for the reporting period.
- [var networkTransferMetrics: MXNetworkTransferMetric?](mxmetricpayload/networktransfermetrics.md)
  The network-transfer activity for the reporting period.
### Reading performance metrics
- [var applicationExitMetrics: MXAppExitMetric?](mxmetricpayload/applicationexitmetrics.md)
  The app foreground and background exit metrics for the reporting period.
- [var applicationTimeMetrics: MXAppRunTimeMetric?](mxmetricpayload/applicationtimemetrics.md)
  The app foreground and background time metrics for the reporting period.
- [var memoryMetrics: MXMemoryMetric?](mxmetricpayload/memorymetrics.md)
  The memory metrics for the reporting period.
### Reading responsiveness metrics
- [var applicationLaunchMetrics: MXAppLaunchMetric?](mxmetricpayload/applicationlaunchmetrics.md)
  The app launch and resume metrics for the reporting period.
- [var animationMetrics: MXAnimationMetric?](mxmetricpayload/animationmetrics.md)
  The metrics for the responsiveness of app animations for the reporting period.
- [var applicationResponsivenessMetrics: MXAppResponsivenessMetric?](mxmetricpayload/applicationresponsivenessmetrics.md)
  The metrics indicating an app’s responsiveness to user interaction for the reporting period.
### Reading disk access metrics
- [var diskIOMetrics: MXDiskIOMetric?](mxmetricpayload/diskiometrics.md)
  The storage metrics for the reporting period.
### Reading custom metrics
- [var signpostMetrics: [MXSignpostMetric]?](mxmetricpayload/signpostmetrics.md)
  An array of the custom metrics for the reporting period.
### Generating a report
- [func jsonRepresentation() -> Data](mxmetricpayload/jsonrepresentation.md)
  Returns the contents of the payload in JSON format.
- [func dictionaryRepresentation() -> [AnyHashable : Any]](mxmetricpayload/dictionaryrepresentation.md)
  Returns the results of the payload as a dictionary.
### Reading information about the payload
- [var timeStampBegin: Date](mxmetricpayload/timestampbegin.md)
  The starting time of the reporting period.
- [var timeStampEnd: Date](mxmetricpayload/timestampend.md)
  The ending time of the reporting period.
- [var includesMultipleApplicationVersions: Bool](mxmetricpayload/includesmultipleapplicationversions.md)
  A Boolean indicating if the version of the app changed at least once during the reporting period.
- [var latestApplicationVersion: String](mxmetricpayload/latestapplicationversion.md)
  The version of the app on the device at the end of the reporting period.
- [var metaData: MXMetaData?](mxmetricpayload/metadata.md)
  A set of system-level information for the device.
### Instance Properties
- [var diskSpaceUsageMetrics: MXDiskSpaceUsageMetric?](mxmetricpayload/diskspaceusagemetrics.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MXMetricManager](mxmetricmanager.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- [class MXDiagnosticPayload](mxdiagnosticpayload.md)
  An object that encapsulates a diagnostic report.
- [protocol MXMetricManagerSubscriber](mxmetricmanagersubscriber.md)
  A protocol defining a method for receiving a daily metrics report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload)*