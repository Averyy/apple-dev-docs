# Monitoring app performance with MetricKit

**Framework**: MetricKit

Receive daily performance and diagnostic reports from real device usage.

#### Overview

MetricKit collects performance data from real devices running your app. It provides profiling data to your app once per day, giving you a picture of how your app performs in conditions you can’t easily reproduce during development. You can collect statistics like CPU usage, memory consumption, network activity, launch time, disk I/O, and more, all through a single API.

When you use the [`StateReporting`](https://developer.apple.com/documentation/StateReporting) framework to describe your app’s behavior, MetricKit can attribute metrics like hitch time or slow app launch to a particular feature, an app-configurable setting, or any other labeled states that you define. With performance data broken down by states, you have more evidence to make targeted, confident decisions for the next version of your app.

#### Understand the Reporting Model

[`MetricManager`](metricmanager.md) is the entry point for receiving metric data. Depending on what you need to measure, you create instances of [`MetricManager`](metricmanager.md) that are scoped to a module, a feature, or the lifetime of your app. For each instance, you can observe two asynchronous sequences: [`metricReports`](metricmanager/metricreports.md) for daily aggregated performance data and [`diagnosticReports`](metricmanager/diagnosticreports.md) for event-based diagnostic reports. These reports conform to [`Codable`](https://developer.apple.com/documentation/Swift/Codable), so you can encode them for upload to a backend database or archive them locally.

A [`MetricReport`](metricreport.md) contains measurements organized into two kinds of entries, [`intervalEntries`](metricreport/intervalentries.md) and [`stateEntries`](metricreport/stateentries.md). [`intervalEntries`](metricreport/intervalentries.md) contains metrics aggregated over time, including a full-day entry for the reporting period. Each [`MetricReport.IntervalEntry`](metricreport/intervalentry.md) also includes a [`states`](metricreport/intervalentry/states.md) array that records which states were active during that interval. [`stateEntries`](metricreport/stateentries.md) contains the same metrics segmented by the states your app reports through the [`StateReporting`](https://developer.apple.com/documentation/StateReporting) framework. The two views are complementary: interval entries give you a time-based picture with state information, and state entries reveal how performance varies across distinct user experiences. Both [`stateEntries`](metricreport/stateentries.md) and the [`states`](metricreport/intervalentry/states.md) arrays are empty when your app does not adopt the [`StateReporting`](https://developer.apple.com/documentation/StateReporting) framework or when no states are active during the reporting period.

A [`DiagnosticReport`](diagnosticreport.md) contains discrete, event-based data. Access each report’s context through its [`DiagnosticReport.Environment`](diagnosticreport/environment-swift.struct.md), which includes information such as application version, operating system version, and device type. The results within each report are [`DiagnosticResult`](diagnosticresult.md) enum values such as [`DiagnosticResult.crash(_:)`](diagnosticresult/crash(_:).md), [`DiagnosticResult.hang(_:)`](diagnosticresult/hang(_:).md), [`DiagnosticResult.cpuException(_:)`](diagnosticresult/cpuexception(_:).md), [`DiagnosticResult.diskWriteException(_:)`](diagnosticresult/diskwriteexception(_:).md), and [`DiagnosticResult.appLaunch(_:)`](diagnosticresult/applaunch(_:).md).

MetricKit collects data continuously and delivers it once per day when conditions permit. The [`timeRange`](metricreport/timerange.md) tells you the exact interval the report covers, and because each report reflects a full day’s worth of real usage, it’s more likely to encounter edge cases that are difficult to reproduce in a local test environment.

#### Set Up a Metric Manager

Create and store your `MetricManager` in a long-lived property so the subscription remains active:

```swift
let manager = MetricManager()
```

To receive per-state metric entries, pass your [`StateReportingDomain`](statereportingdomain.md) values at initialization:

```swift
extension StateReportingDomain {
    static let experiments: StateReportingDomain = "com.example.app.experiments"
}

let manager = MetricManager(enabledStateReportingDomains: [.experiments])
```

A [`StateReportingDomain`](statereportingdomain.md) identifies a logical grouping of related states, such as an experiment group or a feature area. Separate domains allow multiple states to be active at the same time, such as a game tracking gameplay mode in one domain and graphics quality in another. A player moving between single-player and multi-player does not affect the graphics quality state. That state is tracked independently in its own domain. You only receive per-state data for domains you explicitly register, and a manager you initialize without domains receives only interval entries. Use a single [`MetricManager`](metricmanager.md) instance that registers all the domains your app needs, which reduces overhead and simplifies observation.

Use the [`ReportableMetadata()`](https://developer.apple.com/documentation/StateReporting/ReportableMetadata()) attribute to define a state type, then call [`reporter(for:stableMetadata:volatileMetadata:)`](https://developer.apple.com/documentation/StateReporting/StateReporter/reporter(for:stableMetadata:volatileMetadata:)) to get a reporter and [`reportTransition(to:stableMetadata:volatileMetadata:)`](https://developer.apple.com/documentation/StateReporting/StateReporter/reportTransition(to:stableMetadata:volatileMetadata:)) to signal state changes:

```swift
import StateReporting

@ReportableMetadata
struct GraphicsConfiguration {
    let resolution: Int
    let shadow: String
    let texture: String
}

let reporter = StateReporter.reporter(
    for: "com.example.app.graphics",
    stableMetadata: GraphicsConfiguration.self
)

reporter.reportTransition(
    to: "low",
    stableMetadata: GraphicsConfiguration(resolution: 720, shadow: "low", texture: "low")
)

// Signals that the graphics state is over.
reporter.reportTransition(to: nil)
```

[`ReportableMetadata()`](https://developer.apple.com/documentation/StateReporting/ReportableMetadata()) automatically generates the [`metadataDictionary`](https://developer.apple.com/documentation/StateReporting/ReportableMetadata/metadataDictionary) conformance from the struct’s stored properties. Each property becomes part of the state data MetricKit records.

MetricKit only surfaces stable metadata. You can also pass `volatileMetadata` to your [`StateReporter`](https://developer.apple.com/documentation/StateReporting/StateReporter), which is available to other diagnostic tools such as Instruments, but is not visible to MetricKit. For more information, see [`StateReporting`](https://developer.apple.com/documentation/StateReporting).

The system enforces limits on the number of unique states MetricKit aggregates in a single reporting period. When your app exceeds this limit, [`hasExceededStateLimit`](metricreport/environment-swift.struct/hasexceededstatelimit.md) is `true` in the resulting report. Metrics for states beyond the limit appear in the full-day interval entry rather than in [`stateEntries`](metricreport/stateentries.md). Check this flag when processing reports and design your reporting scheme to handle the case where some state entries may not appear. Keep property names and string values in your `@ReportableMetadata` types concise. The system enforces length constraints on both, and concise names reduce noise when analyzing performance data. Design states around distinct, stable user experiences - meaningful state definitions make performance data easier to interpret when you analyze reports.

#### Observe Metric Reports

Use `for await` to consume each [`MetricReport`](metricreport.md) as it arrives. Each report provides two complementary views of your performance data: [`stateEntries`](metricreport/stateentries.md) with metrics segmented by app state, and [`intervalEntries`](metricreport/intervalentries.md) with metrics aggregated over time windows. Iterate both to capture the full picture:

```swift
let manager = MetricManager(
    enabledStateReportingDomains: [StateReportingDomain("com.example.app.experiments")]
)

for await report in manager.metricReports {
    // Metrics segmented by app state.
    for entry in report.stateEntries {
        for value in entry.values {
            switch value {
            case let .hangTime(metric): uploadMetric(metric.histogram, state: entry.state.label)
            @unknown default: break
            }
        }
    }

    // Metrics aggregated over time intervals.
    for entry in report.intervalEntries {
        for value in entry.values {
            switch value {
            case let .cpuTime(metric): uploadMetric(metric.value)
            case let .peakMemory(metric): uploadMetric(metric.value)
            @unknown default: break
            }
        }
    }
}
```

Include an `@unknown default` case in each switch statement to handle any additional metrics.

> **Note**: To generate reports during development without waiting for the daily delivery schedule, choose Debug > Simulate MetricKit Payloads in Xcode. Simulated reports contain sample data, not actual data from your app, for all domains registered with that [`MetricManager`](metricmanager.md) instance. Use simulated reports to understand the structure of MetricKit reports and to test your in-app implementation for report handling.

To process each report in multiple independent workflows, dispatch concurrent work within a single iteration using `async let`:

```swift
for await report in manager.metricReports {
    async let upload: Void = uploadToCloudKit(report: report)
    async let save: Void = saveToFilesApp(report: report)

    _ = await (upload, save)
}
```

Both tasks start immediately and run in parallel. The next iteration waits for both to complete. For a dynamic number of concurrent tasks, use [`withTaskGroup(of:returning:isolation:body:)`](https://developer.apple.com/documentation/Swift/withTaskGroup(of:returning:isolation:body:)) instead.

When you don’t register any state reporting domains, [`stateEntries`](metricreport/stateentries.md) is empty and all performance data appears in the full-day interval entry, accessible through [`fullDayEntry`](https://developer.apple.com/documentation/Swift/Array/fullDayEntry), with an empty [`states`](metricreport/intervalentry/states.md) array.

#### Observe Diagnostic Reports

[`diagnosticReports`](metricmanager/diagnosticreports.md) delivers one [`DiagnosticReport`](diagnosticreport.md) per event. Each report represents a single occurrence of a crash, hang, or exception:

```swift
for await report in manager.diagnosticReports {
    switch report.result {
    case let .crash(diagnostic):
        upload(diagnostic.callStackTree, version: report.environment.applicationVersion)
    case let .hang(diagnostic):
        log(diagnostic.hangDuration)
    case let .cpuException(diagnostic):
        log(diagnostic.totalCPUTime)
    case let .diskWriteException(diagnostic):
        log(diagnostic.totalBytesWritten)
    @unknown default:
        break
    }
}
```

A [`DiagnosticResult.crash(_:)`](diagnosticresult/crash(_:).md) result carries a [`CrashDiagnostic`](crashdiagnostic.md) with a [`callStackTree`](crashdiagnostic/callstacktree.md), essential for diagnosing crashes that happen in production. A [`DiagnosticResult.hang(_:)`](diagnosticresult/hang(_:).md) result carries a [`HangDiagnostic`](hangdiagnostic.md) with the call stack at the time of the hang, pointing directly to which code blocks the main thread.

The [`environment`](diagnosticreport/environment-swift.property.md) property’s [`states`](diagnosticreport/environment-swift.struct/states.md) array contains the StateReporting states active immediately before the event. This context helps you reproduce issues that only occur under specific app conditions.

#### Capture Custom Metrics with Signposts

Signposts let you measure the duration of specific operations you define in your app, such as network requests, database queries, image processing pipelines, or any other work you want to track in production. MetricKit aggregates these measurements and delivers them as [`MetricResult.signpostInterval(_:)`](metricresult/signpostinterval(_:).md) values in your daily `MetricReport`.

Use [`logHandle(category:)`](metricmanager/loghandle(category:).md) to get an [`OSLog`](https://developer.apple.com/documentation/os/OSLog) object tied to the MetricKit collection pipeline:

```swift
let networkLog = MetricManager.logHandle(category: "NetworkRequests")
```

Surround each custom operation with the signpost wrapper [`mxSignpost(_:dso:log:name:signpostID:_:_:)`](mxsignpost(_:dso:log:name:signpostid:_:_:).md), enabling the full [`SignpostIntervalMetric`](signpostintervalmetric.md) result:

```swift
mxSignpost(.begin, log: networkLog, name: "fetchUserProfile")
await fetchUserProfile()
mxSignpost(.end, log: networkLog, name: "fetchUserProfile")
```

The associated [`SignpostIntervalMetric`](signpostintervalmetric.md) tells you how the operation performed: its name and category, how many times it ran, and a `Histogram` of observed durations:

```swift
case let .signpostInterval(metric):
    print("Operation: \(metric.signpostName) (\(metric.signpostCategory))")
    print("Total occurrences: \(metric.totalCount)")
    for bucket in metric.signpostDuration.buckets {
        print("\(bucket.lowerBound)–\(bucket.upperBound): \(bucket.count)")
    }
```

[`SignpostIntervalMetric`](signpostintervalmetric.md) also exposes optional resource-consumption properties — [`cpuTime`](signpostintervalmetric/cputime.md), [`logicalWrites`](signpostintervalmetric/logicalwrites.md), [`averageMemory`](signpostintervalmetric/averagememory.md), [`hitchTimeRatio`](signpostintervalmetric/hitchtimeratio.md), [`totalHitchTime`](signpostintervalmetric/totalhitchtime.md), and [`totalAnimationTime`](signpostintervalmetric/totalanimationtime.md) — which MetricKit populates when it has enough data to report them.

You can also use [`OSSignposter`](https://developer.apple.com/documentation/os/OSSignposter) with the handle from [`logHandle(category:)`](metricmanager/loghandle(category:).md), but it doesn’t populate the [`SignpostIntervalMetric`](signpostintervalmetric.md) measurement properties. Use [`mxSignpost(_:dso:log:name:signpostID:_:_:)`](mxsignpost(_:dso:log:name:signpostid:_:_:).md) to populate properties like CPU time, memory usage, and logical writes. To tag a signpost as an animation interval and populate [`hitchTimeRatio`](signpostintervalmetric/hitchtimeratio.md), [`totalHitchTime`](signpostintervalmetric/totalhitchtime.md), and [`totalAnimationTime`](signpostintervalmetric/totalanimationtime.md), use [`mxSignpostAnimationIntervalBegin(dso:log:name:signpostID:_:_:)`](mxsignpostanimationintervalbegin(dso:log:name:signpostid:_:_:).md) instead.

#### Measure Extended Launch

Wrap launch-critical asynchronous work in [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-48k2s.md) to extend the MetricKit launch measurement. Standard launch metrics end at `applicationDidFinishLaunching`. Many apps also perform asynchronous work that forms part of the perceived launch experience, such as data bootstrapping, configuration fetching, or initial content loading. Tracking this work captures the full time users wait before the app is ready:

```swift
await manager.trackLaunchTask(id: "bootstrapData") {
    await bootstrapApplication()
}
```

The `onTrackingError` closure receives a [`MetricManager.LaunchTaskError`](metricmanager/launchtaskerror.md) when MetricKit cannot record the measurement, letting you log the issue without interrupting the launch work. MetricKit reports the result as [`MetricResult.extendedLaunch(_:)`](metricresult/extendedlaunch(_:).md) in the daily report.

## See Also

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)
  Work with the metric values, diagnostic data, and environments in MetricKit reports.
- [Track performance by app state using MetricKit](track-performance-by-app-state-using-metrickit.md)
  Collect performance metrics, diagnostic reports, and experiment data related to your app’s current state using the MetricKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/monitoring-app-performance-with-metrickit)*