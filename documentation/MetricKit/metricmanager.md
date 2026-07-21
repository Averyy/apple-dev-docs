# MetricManager

**Framework**: MetricKit  
**Kind**: class

An object that delivers metric and diagnostic reports to your app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class MetricManager
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

`MetricManager` is an instantiable class rather than a shared singleton. Create an instance and hold it for as long as you need reports. Share that instance across your app rather than creating multiple instances with the same domains. If you create more than one `MetricManager`, two tasks concurrently iterating the same sequence both receive a non-deterministic subset of reports rather than a full copy.

Metric reports arrive through [`metricReports`](metricmanager/metricreports.md), and diagnostic reports through [`diagnosticReports`](metricmanager/diagnosticreports.md). Both are typed `AsyncSequence` properties that never throw, so you iterate them with `for await` in long-lived tasks:

```swift
let manager = MetricManager()

Task {
    for await report in manager.metricReports {
        process(report)
    }
}
Task {
    for await report in manager.diagnosticReports {
        process(report)
    }
}
```

To receive metrics segmented by app state, pass a set of [`StateReportingDomain`](statereportingdomain.md) values to [`init(enabledStateReportingDomains:)`](metricmanager/init(enabledstatereportingdomains:).md). When state reporting is enabled, [`stateEntries`](metricreport/stateentries.md) carries metrics grouped by each recorded state in addition to the standard [`intervalEntries`](metricreport/intervalentries.md).

## Topics

### Initialization
- [convenience init()](metricmanager/init.md)
  Creates a new `MetricManager` instance without state reporting domains.
- [init(enabledStateReportingDomains: Set<StateReportingDomain>)](metricmanager/init(enabledstatereportingdomains:).md)
  Creates a new `MetricManager` instance with state reporting domains enabled for metrics aggregation.
- [var enabledStateReportingDomains: Set<StateReportingDomain>](metricmanager/enabledstatereportingdomains.md)
  StateReporting domains enabled for metrics aggregation
### Reports
- [var metricReports: some AsyncSequence<MetricReport, Never>](metricmanager/metricreports.md)
  An asynchronous sequence that delivers daily metric reports.
- [var diagnosticReports: some AsyncSequence<DiagnosticReport, Never>](metricmanager/diagnosticreports.md)
  An asynchronous sequence that delivers diagnostic reports as individual events.
### Custom metric logs
- [static func logHandle(category: String) -> OSLog](metricmanager/loghandle(category:).md)
  Returns an `OSLog` handle for creating custom signpost metrics that MetricKit aggregates.
### Extended launch
- [func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)?, () async throws(Failure) -> Result) async throws(Failure) -> Result](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-48k2s.md)
  Measures the duration of an asynchronous extended launch task.
- [func trackLaunchTask<Result, Failure>(id: LaunchTaskID, onTrackingError: ((MetricManager.LaunchTaskError) -> Void)?, () throws(Failure) -> Result) throws(Failure) -> Result](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-jnu1.md)
  Measures the duration of a synchronous extended launch task.
- [MetricManager.LaunchTaskError](metricmanager/launchtaskerror.md)
  An error that describes a problem that occurred while tracking an extended launch task.
- [struct LaunchTaskID](launchtaskid.md)
  An identifier for a task measured as part of an extended app launch.
### State-contextualized metrics
- [MetricManager.ReportedState](metricmanager/reportedstate.md)
  A recorded app state associated with a metric or diagnostic report entry.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MetricReport](metricreport.md)
  A daily performance report that contains metric values for your app.
- [struct DiagnosticReport](diagnosticreport.md)
  A report describing a single diagnostic event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager)*