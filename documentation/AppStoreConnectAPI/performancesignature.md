# PerformanceSignature

**Framework**: App Store Connect API  
**Kind**: dictionary

A performance signature that identifies a recurring performance issue in an app, with its occurrence count and weight.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object PerformanceSignature
```

## Topics

### Objects
- [object PerformanceSignature.MetricsSummary](performancesignature/metricssummary-data.dictionary.md)
  A summary of the metric values for a performance signature across reference versions.

## Properties

- `signatureId` (string): The unique identifier of the performance signature.
- `signature` (string): The symbolicated call site that the signature represents.
- `count` (integer): The number of occurrences that the signature represents.
- `weight` (number): The relative contribution of the signature to the metric.
- `sourceFile` (string): The source file that contains the code the signature refers to.
- `lineNumber` (integer): The line number in the source file that the signature refers to.
- `trendInfo` (DiagnosticInsightDirection): The direction of the metric’s trend for the signature.
- `metricsSummary` (PerformanceSignature.MetricsSummary): A summary of the metric values across reference versions.

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
- [object PerfPowerMetric](perfpowermetric.md)
  Unused.
- [object xcodeMetrics](xcodemetrics.md)
  A response that contains power and performance measurements for your app.
- [object xcodeOverview](xcodeoverview.md)
  The performance overview that Xcode presents for an app, including app metadata, insights, and top performance signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/performancesignature)*