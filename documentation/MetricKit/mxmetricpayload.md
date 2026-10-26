# MXMetricPayload

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object that encapsulates a daily metrics report.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricReport`](./metricreport.md) instead.

## Declaration

```swift
class MXMetricPayload
```

```objc
@interface MXMetricPayload : NSObject
```

## Topics

### Reading battery metrics
- [var cellularConditionMetrics: MXCellularConditionMetric?](./mxmetricpayload/cellularconditionmetrics.md)
  The cellular condition measurements for the reporting period.
- [var cpuMetrics: MXCPUMetric?](./mxmetricpayload/cpumetrics.md)
  The CPU metrics for the reporting period.
- [var displayMetrics: MXDisplayMetric?](./mxmetricpayload/displaymetrics.md)
  The display metrics for the reporting period.
- [var gpuMetrics: MXGPUMetric?](./mxmetricpayload/gpumetrics.md)
  The GPU metrics for the reporting period.
- [var locationActivityMetrics: MXLocationActivityMetric?](./mxmetricpayload/locationactivitymetrics.md)
  The location-tracking activity for the reporting period.
- [var networkTransferMetrics: MXNetworkTransferMetric?](./mxmetricpayload/networktransfermetrics.md)
  The network-transfer activity for the reporting period.
### Reading performance metrics
- [var applicationExitMetrics: MXAppExitMetric?](./mxmetricpayload/applicationexitmetrics.md)
  The app foreground and background exit metrics for the reporting period.
- [var applicationTimeMetrics: MXAppRunTimeMetric?](./mxmetricpayload/applicationtimemetrics.md)
  The app foreground and background time metrics for the reporting period.
- [var memoryMetrics: MXMemoryMetric?](./mxmetricpayload/memorymetrics.md)
  The memory metrics for the reporting period.
### Reading responsiveness metrics
- [var applicationLaunchMetrics: MXAppLaunchMetric?](./mxmetricpayload/applicationlaunchmetrics.md)
  The app launch and resume metrics for the reporting period.
- [var animationMetrics: MXAnimationMetric?](./mxmetricpayload/animationmetrics.md)
  The metrics for the responsiveness of app animations for the reporting period.
- [var applicationResponsivenessMetrics: MXAppResponsivenessMetric?](./mxmetricpayload/applicationresponsivenessmetrics.md)
  The metrics indicating an app’s responsiveness to user interaction for the reporting period.
### Reading disk access metrics
- [var diskIOMetrics: MXDiskIOMetric?](./mxmetricpayload/diskiometrics.md)
  The storage metrics for the reporting period.
### Reading custom metrics
- [var signpostMetrics: [MXSignpostMetric]?](./mxmetricpayload/signpostmetrics.md)
  An array of the custom metrics for the reporting period.
### Generating a report
- [func jsonRepresentation() -> Data](./mxmetricpayload/jsonrepresentation%28%29.md)
  Returns the contents of the payload in JSON format.
- [func dictionaryRepresentation() -> [AnyHashable : Any]](./mxmetricpayload/dictionaryrepresentation%28%29.md)
  Returns the results of the payload as a dictionary.
### Reading information about the payload
- [var timeStampBegin: Date](./mxmetricpayload/timestampbegin.md)
  The starting time of the reporting period.
- [var timeStampEnd: Date](./mxmetricpayload/timestampend.md)
  The ending time of the reporting period.
- [var includesMultipleApplicationVersions: Bool](./mxmetricpayload/includesmultipleapplicationversions.md)
  A Boolean indicating if the version of the app changed at least once during the reporting period.
- [var latestApplicationVersion: String](./mxmetricpayload/latestapplicationversion.md)
  The version of the app on the device at the end of the reporting period.
- [var metaData: MXMetaData?](./mxmetricpayload/metadata.md)
  A set of system-level information for the device.
### Initializers
- [init?(coder: NSCoder)](./mxmetricpayload/init%28coder%29.md)
### Instance Properties
- [var diskSpaceUsageMetrics: MXDiskSpaceUsageMetric?](./mxmetricpayload/diskspaceusagemetrics.md)
  An object containing disk space usage metrics for this application.
### Instance Methods
- [- DictionaryRepresentation](./mxmetricpayload/dictionaryrepresentation-1nrgx.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Metric and diagnostic reports
- [class MXMetricManager](./mxmetricmanager.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- [class MXDiagnosticPayload](./mxdiagnosticpayload.md)
  An object that encapsulates a diagnostic report.
- [protocol MXMetricManagerSubscriber](./mxmetricmanagersubscriber.md)
  A protocol defining a method for receiving a daily metrics report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload)*