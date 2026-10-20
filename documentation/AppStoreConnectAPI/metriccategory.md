# MetricCategory

**Framework**: App Store Connect API  
**Kind**: typealias  
**Role**: Type

Categories of metric reports for apps that you distribute through the App Store.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
string MetricCategory
```

## Possible Values

- `HANG`: The number of seconds per hour that the main thread of the app is unresponsive for more than 250 ms (the maximum time an app can respond to a typical event before a person perceives it as slow).
- `LAUNCH`: The average launch time (the time between a person tapping your app icon and the system drawing a screen other than the launch screen), measured in milliseconds.
- `MEMORY`: The amount of memory the app uses, in megabytes.
- `DISK`: The number of megabytes per day that the app writes to long-term storage.
- `BATTERY`: The amount of battery power the app uses over a 24-hour period when the device is disconnected from power.
- `TERMINATION`: The average number of app terminations that people don’t initiate, including background terminations, per day.
- `ANIMATION`: The hitch rate of your app over time. The hitch rate tracks animation interruptions across all animated interactions, including scrolling, transitions, and other continuous motion.
- `STORAGE`: The data usage and binary size of your app.

## Mentions

- [App Store Connect API 4.4 release notes](./app-store-connect-api-4-4-release-notes.md)

## See Also

### Objects and types
- [object AppPerfPowerMetricsLinkagesResponse](./appperfpowermetricslinkagesresponse.md)
- [object AppPerformanceOverviewsLinkagesResponse](./appperformanceoverviewslinkagesresponse.md)
- [object DiagnosticInsight](./diagnosticinsight.md)
  An AI-generated analysis of a recurring performance issue identified in your app’s diagnostic logs, with suggested fixes.
- [object DiagnosticLog](./diagnosticlog.md)
  A raw performance log file associated with a diagnostic signature, downloadable for detailed analysis.
- [object DiagnosticLogCallStackNode](./diagnosticlogcallstacknode.md)
  Diagnostic information that describes a single line in a call stack.
- [object diagnosticLogs](./diagnosticlogs.md)
  A response containing log data for a diagnostic signature.
- [object DiagnosticSignature](./diagnosticsignature.md)
  A unique pattern identifying a recurring crash, hang, or disk-write exception in your app’s diagnostic logs.
- [object DiagnosticSignatureLogsLinkagesResponse](./diagnosticsignaturelogslinkagesresponse.md)
- [object DiagnosticSignaturesResponse](./diagnosticsignaturesresponse.md)
  A response containing a list of unique performance issue signatures identified in your app’s diagnostic data.
- [object MetricsInsight](./metricsinsight.md)
  Results of an analysis of metric data for a single metric category for your app.
- [object PerformanceOverview](./performanceoverview.md)
  An aggregated performance overview for an app, summarizing the performance data that Xcode reports.
- [object PerformanceSignature](./performancesignature.md)
  A performance signature that identifies a recurring performance issue in an app, with its occurrence count and weight.
- [object PerfPowerMetric](./perfpowermetric.md)
  Unused.
- [object xcodeMetrics](./xcodemetrics.md)
  A response that contains power and performance measurements for your app.
- [object xcodeOverview](./xcodeoverview.md)
  The performance overview that Xcode presents for an app, including app metadata, insights, and top performance signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/metriccategory)*