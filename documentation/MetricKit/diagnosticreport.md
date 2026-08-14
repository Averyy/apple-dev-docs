# DiagnosticReport

**Framework**: MetricKit  
**Kind**: struct

A report describing a single diagnostic event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DiagnosticReport
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)
- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

Each iteration of [`diagnosticReports`](metricmanager/diagnosticreports.md) yields one report. Access the diagnostic event through [`result`](diagnosticreport/result.md), which is a [`DiagnosticResult`](diagnosticresult.md) enum. Switch over the result to handle each diagnostic type:

```swift
for await report in manager.diagnosticReports {
    switch report.result {
    case .crash(let diagnostic):
        handleCrash(diagnostic)
    case .hang(let diagnostic):
        handleHang(diagnostic)
    case .cpuException(let diagnostic):
        handleCPUException(diagnostic)
    case .diskWriteException(let diagnostic):
        handleDiskWriteException(diagnostic)
    case .appLaunch(let diagnostic):
        handleAppLaunchDiagnostic(diagnostic)
    @unknown default:
        break
    }
}
```

The [`environment`](diagnosticreport/environment-swift.property.md) property contains device and app metadata, [`states`](diagnosticreport/environment-swift.struct/states.md), and any [`signpostData`](diagnosticreport/environment-swift.struct/signpostdata.md) associated with the event. The states array contains the [`MetricManager.ReportedState`](metricmanager/reportedstate.md) values that are active when the diagnostic event occurs.

MetricKit does not generate a `DiagnosticReport` for every occurrence of a diagnostic event. For example, hang diagnostics are only generated when the device has hang detection enabled or belongs to a sampling group with hang detection active.

Because `DiagnosticReport` conforms to `Codable`, you can serialize it directly with `JSONEncoder`.

## Topics

### Report details
- [let timeRange: DateInterval](diagnosticreport/timerange.md)
  The date interval this report covers.
- [let environment: DiagnosticReport.Environment](diagnosticreport/environment-swift.property.md)
  Environment context for the device and app.
### Diagnostic event
- [let result: DiagnosticResult](diagnosticreport/result.md)
  The diagnostic result for this report.
### Structures
- [DiagnosticReport.Environment](diagnosticreport/environment-swift.struct.md)
  Device, app, and state metadata associated with a diagnostic report.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class MetricManager](metricmanager.md)
  An object that delivers metric and diagnostic reports to your app.
- [struct MetricReport](metricreport.md)
  A daily performance report that contains metric values for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/diagnosticreport)*