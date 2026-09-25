# PerfPowerMetric

**Framework**: App Store Connect API  
**Kind**: dictionary

Unused.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object PerfPowerMetric
```

## Topics

### Objects
- [object PerfPowerMetric.Attributes](perfpowermetric/attributes-data.dictionary.md)
  Attributes that describe a Power and Performance Metrics resource.

## Properties

- `attributes` (PerfPowerMetric.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*

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
- [object xcodeMetrics](xcodemetrics.md)
  A response that contains power and performance measurements for your app.
- [object xcodeOverview](xcodeoverview.md)
  The performance overview that Xcode presents for an app, including app metadata, insights, and top performance signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/perfpowermetric)*