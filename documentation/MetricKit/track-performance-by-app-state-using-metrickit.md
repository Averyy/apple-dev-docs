# Track performance by app state using MetricKit

**Framework**: MetricKit

Collect performance metrics, diagnostic reports, and experiment data related to your app’s current state using the MetricKit framework.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

MetricKit provides the data you need to understand how your app performs in the real world, from launch times and UI responsiveness to crash diagnostics. This sample app shows you how to integrate MetricKit into a SwiftUI app to collect performance metrics, correlate them with experiments and user activities, and inspect the resulting reports.

The app is an expense report manager that lets you create reports, scan receipts, and view expenses in different layouts. As you use the app on your device, MetricKit collects performance data in the background. The sample saves incoming metric and diagnostic reports as JSON files in the Files app.

![An iOS app displaying a daily expense breakdown across two spending categories. The presentation can be adjusted to show daily, weekly, monthly, or yearly breakdowns.](/images/com.apple.metrickit/track-performance-by-app-state-using-metrickit-1@2x.png)

> **Note**: MetricKit delivers reports on a system-determined schedule. To generate reports during development, choose Debug > Simulate MetricKit Payloads in Xcode.

#### Configure the Sample Code Project

To build and run this sample, you need:

- Xcode 27 or later
- A device running iOS 27 or later (MetricKit doesn’t deliver reports on simulated devices)

To configure the project:

1. Open the project in Xcode.
2. Select the MetricKit Sample target, and choose your development team under **Signing & Capabilities**.
3. Build and run the app on your device.

The app creates sample expense data on first launch. Receipt images and metric payloads are stored in the app’s Documents directory, accessible through the Files app.

#### Create a Metrics Collector

The sample centralizes all MetricKit integration in a `MetricsCollector` class. This class initializes a [`MetricManager`](metricmanager.md) with the state reporting domains the app uses — one for experiments and one for user activity:

```swift
@Observable
class MetricsCollector {
    private let metricManager: MetricManager

    init() {
        self.metricManager = MetricManager(enabledStateReportingDomains: [
            Experiments.domain,
            UserActivity.domain
        ])
    }
}
```

The app entry point creates the collector, starts listening for reports, and injects it into the SwiftUI environment, allowing views throughout the app to report state transitions:

```swift
@main
struct MetricKit_SampleApp: App {
    private let metricsCollector = MetricsCollector()

    var body: some Scene {
        WindowGroup {
            // ...
        }
        .environment(metricsCollector)
    }
}
```

#### Receive Metric and Diagnostic Reports

The sample listens for two types of reports using async sequences on [`MetricManager`](metricmanager.md). Metric reports contain aggregated performance data, and diagnostic reports contain information about crashes, hangs, and other issues.

```swift
func startListening() {
    metricTask = Task { [weak self] in
        guard let self else { return }
        for await report in metricManager.metricReports {
            await handleMetricReport(report)
        }
    }

    diagnosticTask = Task { [weak self] in
        guard let self else { return }
        for await report in metricManager.diagnosticReports {
            await handleDiagnosticReport(report)
        }
    }
}
```

Each report handler encodes the report to JSON and writes it to the app’s Documents directory. Because the project enables the `UIFileSharingEnabled` key in its information property list, the saved reports are accessible through the Files app on the device. The sample configures its `JSONEncoder` to organize metric data by state reporting domain, which groups the metrics alongside the experiment and user activity state that was active when the system collected them:

```swift
encoder.userInfo[MetricReport.encodingFormatKey] = MetricReport.EncodingFormat.byStateReportingDomain
```

#### Track Experiment Variants with State Reporting

The sample uses state reporting to correlate performance data with specific experiment variants. By tracking which variant is active, the resulting metric reports reveal whether a particular layout causes performance regressions.

The sample defines a `@ReportableMetadata` macro to describe the experiment context, and a [`StateReportingDomain`](statereportingdomain.md) to group experiment data:

```swift
@ReportableMetadata
struct ExperimentContext {
    let experimentID: String
    let variant: String
}

enum Experiments {
    static let domain: StateReportingDomain = "com.example.metrickitsample.experiments"

    enum ExpenseDetailLayout: String {
        static let id = "expense-report-detail"
        case cardLayout = "card-layout"
        case listLayout = "list-layout"
    }
}
```

The `MetricsCollector` creates a state reporter for the experiments domain, and exposes methods that transition the reporter between active and cleared states:

```swift
private let expenseReportDetailViewExperimentReporter = MetricManager.stateReporter(
    for: Experiments.domain.rawValue,
    stableMetadata: ExperimentContext.self
)

func reportExpenseDetailLayoutVariant(variant: Experiments.ExpenseDetailLayout) {
	expenseReportDetailViewExperimentReporter.reportTransition(
		to: "Active",
		stableMetadata: ExperimentContext(
			experimentID: Experiments.ExpenseDetailLayout.id,
			variant: variant.rawValue
		)
	)
}
```

The expense report detail view reports the active variant when the view appears and updates it when the person toggles the layout. The person can also change the active variant from the MetricKit Sample settings in the Settings app, which provides a “Use Card Layout” toggle under the “A/B Test” group. The view reports a transition immediately when the preference changes, so that the metric data reflects the variant that was active at the time the system collected performance measurements.

```swift
.task(id: useCardLayout) {
	let variant: Experiments.ExpenseDetailLayout = useCardLayout ? .cardLayout : .listLayout
	metricsCollector.reportExpenseDetailLayoutVariant(variant: variant)
}
```

#### Report User Activity State

The sample tracks which workflow a person is performing so that metric reports reflect performance data in the context of specific activities. By reporting which tab is active, the resulting reports reveal whether performance issues are isolated to a particular area of the app.

The sample defines a `@ReportableMetadata` type and a [`StateReportingDomain`](statereportingdomain.md) for user activity, with constants for each tracked mode:

```swift
@ReportableMetadata
struct UserActivityMetadata: Sendable {
    let listSize: String
}

enum UserActivity {
    static let domain = StateReportingDomain("com.example.metrickitsample.tabs")

    enum Mode {
        static let reports = "reports"
        static let spending = "spending"
    }
}
```

The main tab view reports a transition whenever the selected tab changes, using the `.onChange` modifier with `initial: true` to also capture the initial state:

```swift
.onChange(of: selectedTab, initial: true) {
    switch selectedTab {
    case .reports:
        metricsCollector.reportUserActivity(screen: UserActivity.Mode.reports, reportCount: reports.count)
    case .spending:
        metricsCollector.reportUserActivity(screen: UserActivity.Mode.spending, reportCount: reports.count)
    }
}
```

The `metricsCollector` reports a state transition each time the person switches between the Reports and Spending tabs, allowing the system to attribute performance data to the active workflow.

#### Measure Launch Performance

The sample measures the time spent creating initial sample data during app launch by wrapping the operation in a call to [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-jnu1.md). The framework includes this timing data in subsequent metric reports, which helps identify slow launch operations:

```swift
metricsCollector.trackLaunchTask(idString: "create-seed-data") {
    DataContainer.seedIfNeeded()
}
```

#### Measure Document Capture with Signpost Metrics

The sample uses [`SignpostIntervalMetric`](signpostintervalmetric.md) to measure resource usage during the receipt scanning workflow. By wrapping the document camera session in a signpost interval, MetricKit aggregates CPU time, memory, logical writes, and duration across scanning sessions and includes them in metric reports.

The `MetricsCollector` obtains a log handle from [`MetricManager`](metricmanager.md) and provides methods to begin and end the signpost interval:

```swift
private let documentCaptureLog = MetricManager.logHandle(category: "DocumentCapture")

func beginDocumentCapture() {
    mxSignpost(.begin, log: documentCaptureLog, name: "ReceiptScan")
}

func endDocumentCapture() {
    mxSignpost(.end, log: documentCaptureLog, name: "ReceiptScan")
}
```

The log handle that [`logHandle(category:)`](metricmanager/loghandle(category:).md) returns is persistent. So, MetricKit collects and aggregates all the signposts that this log handle emits. The signpost name and category identify this interval in the resulting [`SignpostIntervalMetric`](signpostintervalmetric.md) objects. You can also use [`OSSignposter`](https://developer.apple.com/documentation/os/ossignposter) with this handle, but only [`mxSignpost(_:dso:log:name:signpostID:_:_:)`](mxsignpost(_:dso:log:name:signpostid:_:_:).md) populates the [`SignpostIntervalMetric`](signpostintervalmetric.md) measurement properties such as CPU time, memory usage, and logical writes.

The expense report detail view begins the interval when the person taps the button to scan a receipt, and ends it when the scanner sheet dismisses:

```swift
Button("Add Expense", systemImage: "document.viewfinder") {
    metricsCollector.beginDocumentCapture()
    showingScanner = true
}

// ...

.sheet(isPresented: $showingScanner, onDismiss: {
    metricsCollector.endDocumentCapture()
}) {
    DocumentCameraView { images in
        // ...
    }
}
```

The resulting metric reports include an [`SignpostIntervalMetric`](signpostintervalmetric.md) entry containing cumulative CPU time, peak memory, cumulative logical writes, and a histogram of interval durations.

The sample also triggers a fatal error when a person attempts to submit an expense report with no expenses. This intentional crash generates a crash diagnostic report.

#### Identify Crash Diagnostics in Reports

Each [`DiagnosticReport`](diagnosticreport.md) contains a `result` property of type [`DiagnosticResult`](diagnosticresult.md), which is an enum indicating the kind of diagnostic:

```swift
public enum DiagnosticResult {
    case crash(CrashDiagnostic)
    case hang(HangDiagnostic)
    case cpuException(CPUExceptionDiagnostic)
    case diskWriteException(DiskWriteExceptionDiagnostic)
    case appLaunch(AppLaunchDiagnostic)
    case memoryException(MemoryExceptionDiagnostic)
}
```

To detect whether a diagnostic report contains a crash, use pattern matching on the `result`:

```swift
private func handleDiagnosticReport(_ report: DiagnosticReport) async {
    saveDiagnosticReport(report)

    if case .crash(let crashDiagnostic) = report.result {
        // Handle crash-specific logic
    }
}
```

The [`CrashDiagnostic`](crashdiagnostic.md) type provides details about the crash, including the termination reason, Mach exception type, Unix signal, and the call stack tree at the time of the crash.

The sample demonstrates how to use this pattern to prompt someone for additional context in debug builds. When a crash diagnostic is detected, the app presents a modal dialog asking the person to describe what they were doing when the crash occurred. This kind of supplemental information can be valuable during development, where stack traces alone may not explain how a person reached a particular code path.

## See Also

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)
  Receive daily performance and diagnostic reports from real device usage.
- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)
  Work with the metric values, diagnostic data, and environments in MetricKit reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/track-performance-by-app-state-using-metrickit)*