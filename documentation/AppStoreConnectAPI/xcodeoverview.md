# xcodeOverview

**Framework**: App Store Connect API  
**Kind**: dictionary

The performance overview that Xcode presents for an app, including app metadata, insights, and top performance signatures.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object xcodeOverview
```

## Topics

### Objects
- [object xcodeOverview.AppMetadata](xcodeoverview/appmetadata-data.dictionary.md)
  Metadata about the app that a performance overview describes.
- [object xcodeOverview.Insights](xcodeoverview/insights-data.dictionary.md)
  Performance insights for an app, including regressions and metrics that are trending up.
- [object xcodeOverview.Signatures](xcodeoverview/signatures-data.dictionary.md)
  The top performance signatures for an app, such as its top hang, launch, and disk-write points.
### Dictionaries
- [object xcodeOverview.Categories](xcodeoverview/categories-data.dictionary.md)

## Properties

- `version` (string): The app version that the performance overview describes.
- `appMetadata` (xcodeOverview.AppMetadata): Metadata that identifies the app the overview describes.
- `insights` (xcodeOverview.Insights): The performance insights for the app, grouped into regressions and improving trends.
- `categories` ([xcodeOverview.Categories]): The metric categories included in the overview.
- `signatures` (xcodeOverview.Signatures): The most significant performance signatures for the app, grouped by type.
- `telemetryIdentifier` (string): A unique identifier for correlating the overview with telemetry data.

## See Also

- [object AppPerfPowerMetricsLinkagesResponse](appperfpowermetricslinkagesresponse.md)
- [object AppPerformanceOverviewsLinkagesResponse](appperformanceoverviewslinkagesresponse.md)
- [object DiagnosticInsight](diagnosticinsight.md)
  An AI-generated analysis of a recurring performance issue identified in your app’s diagnostic logs, with suggested fixes.
- [object DiagnosticLog](diagnosticlog.md)
  A raw performance log file associated with a diagnostic signature, downloadable for detailed analysis.
- [object DiagnosticLogCallStackNode](diagnosticlogcallstacknode.md)
  Diagnostic information that describes a single line in a call stack.
- [object diagnosticLogs](diagnosticlogs.md)
  A response containing log data for a diagnostic signature.
- [object DiagnosticSignature](diagnosticsignature.md)
  A unique pattern identifying a recurring crash, hang, or disk-write exception in your app’s diagnostic logs.
- [object DiagnosticSignatureLogsLinkagesResponse](diagnosticsignaturelogslinkagesresponse.md)
- [object DiagnosticSignaturesResponse](diagnosticsignaturesresponse.md)
  A response containing a list of unique performance issue signatures identified in your app’s diagnostic data.
- [type MetricCategory](metriccategory.md)
  Categories of metric reports for apps that you distribute through the App Store.
- [object MetricsInsight](metricsinsight.md)
  Results of an analysis of metric data for a single metric category for your app.
- [object PerformanceOverview](performanceoverview.md)
  An aggregated performance overview for an app, summarizing the performance data that Xcode reports.
- [object PerformanceSignature](performancesignature.md)
  A performance signature that identifies a recurring performance issue in an app, with its occurrence count and weight.
- [object PerfPowerMetric](perfpowermetric.md)
  Unused.
- [object xcodeMetrics](xcodemetrics.md)
  A response that contains power and performance measurements for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodeoverview)*