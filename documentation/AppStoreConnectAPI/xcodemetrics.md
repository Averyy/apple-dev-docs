# xcodeMetrics

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains power and performance measurements for your app.

**Availability**:
- App Store Connect API 1.8+

## Declaration

```swift
object xcodeMetrics
```

## Mentions

- [App Store Connect API 2.0 release notes](app-store-connect-api-2-0-release-notes.md)

## Topics

### Objects
- [object xcodeMetrics.Insights](xcodemetrics/insights-data.dictionary.md)
  Analysis of power and performance data collected for your app that includes regressions and trends.
- [object xcodeMetrics.ProductData](xcodemetrics/productdata-data.dictionary.md)
  The metrics information of an app on a specific platform.

## Properties

- `insights` (xcodeMetrics.Insights): Analysis of data collected about the power and performance of your app that includes regressions and trends.
- `productData` ([xcodeMetrics.ProductData]): An array of metrics data containing power and performance measurements for your app, organized by platform.
- `version` (string): The current App Store Connect API version.

## See Also

- [object DiagnosticInsight](diagnosticinsight.md)
  An AI-generated analysis of a recurring performance issue identified in your app’s diagnostic logs, with suggested fixes.
- [object DiagnosticSignaturesResponse](diagnosticsignaturesresponse.md)
  A response containing a list of unique performance issue signatures identified in your app’s diagnostic data.
- [object DiagnosticSignature](diagnosticsignature.md)
  A unique pattern identifying a recurring crash, hang, or disk-write exception in your app’s diagnostic logs.
- [object diagnosticLogs](diagnosticlogs.md)
  A response containing log data for a diagnostic signature.
- [object DiagnosticLog](diagnosticlog.md)
  A raw performance log file associated with a diagnostic signature, downloadable for detailed analysis.
- [object DiagnosticLogCallStackNode](diagnosticlogcallstacknode.md)
  Diagnostic information that describes a single line in a call stack.
- [object MetricsInsight](metricsinsight.md)
  Results of an analysis of metric data for a single metric category for your app.
- [type MetricCategory](metriccategory.md)
  Categories of metric reports for apps that you distribute through the App Store.
- [object PerfPowerMetric](perfpowermetric.md)
  Unused.
- [object AppPerfPowerMetricsLinkagesResponse](appperfpowermetricslinkagesresponse.md)
- [object DiagnosticSignatureLogsLinkagesResponse](diagnosticsignaturelogslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcodemetrics)*