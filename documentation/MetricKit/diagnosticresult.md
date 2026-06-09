# DiagnosticResult

**Framework**: MetricKit  
**Kind**: enum

An enumeration that represents a single diagnostic event from a diagnostic report.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum DiagnosticResult
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)
- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

`DiagnosticResult` unifies all diagnostic event types into a single enum. Each associated value is a typed diagnostic struct that carries a [`CallStackTree`](callstacktree.md) and additional event-specific properties such as hang duration, total CPU time, or launch duration.

Access the result through [`result`](diagnosticreport/result.md) after iterating over [`diagnosticReports`](metricmanager/diagnosticreports.md). Switch over the result to handle each diagnostic type:

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

This type replaces the `crashDiagnostics`, `hangDiagnostics`, `cpuExceptionDiagnostics`, `diskWriteExceptionDiagnostics`, and `appLaunchDiagnostics` properties of [`MXDiagnosticPayload`](mxdiagnosticpayload.md).

## Topics

### Call stack
- [struct CallStackTree](callstacktree.md)
  A tree structure representing a collection of call stacks captured during a diagnostic event.
### Diagnostic results
- [struct CrashDiagnostic](crashdiagnostic.md)
  A diagnostic report that describes a crash that occurred.
- [struct HangDiagnostic](hangdiagnostic.md)
  A diagnostic for an app that was too busy to handle user input responsively.
- [struct CPUExceptionDiagnostic](cpuexceptiondiagnostic.md)
  A diagnostic for a fatal or nonfatal CPU exception.
- [struct DiskWriteExceptionDiagnostic](diskwriteexceptiondiagnostic.md)
  A diagnostic for a disk write exception.
- [struct AppLaunchDiagnostic](applaunchdiagnostic.md)
  A diagnostic report for an app launch.
- [struct MemoryExceptionDiagnostic](memoryexceptiondiagnostic.md)
  A diagnostic for a fatal memory exception.
### Enumeration Cases
- [case appLaunch(AppLaunchDiagnostic)](diagnosticresult/applaunch(_:).md)
- [case cpuException(CPUExceptionDiagnostic)](diagnosticresult/cpuexception(_:).md)
- [case crash(CrashDiagnostic)](diagnosticresult/crash(_:).md)
- [case diskWriteException(DiskWriteExceptionDiagnostic)](diagnosticresult/diskwriteexception(_:).md)
- [DiagnosticResult.hang(_:)](diagnosticresult/hang(_:).md)
- [case memoryException(MemoryExceptionDiagnostic)](diagnosticresult/memoryexception(_:).md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MetricResult](metricresult.md)
  An enumeration that represents a single metric value from a metric report entry.
- [struct MetricGroup](metricgroup.md)
  A value that identifies the category a metric belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/diagnosticresult)*