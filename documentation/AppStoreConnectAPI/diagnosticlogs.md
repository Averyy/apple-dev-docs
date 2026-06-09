# diagnosticLogs

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing log data for a diagnostic signature.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object diagnosticLogs
```

## Topics

### Objects
- [object diagnosticLogs.ProductData](diagnosticlogs/productdata-data.dictionary.md)
  The logs and insights for a diagnostic signature.

## Properties

- `productData` ([diagnosticLogs.ProductData]): An array of log data for a specific diagnostic signature.
- `version` (string): The version of the App Store Connect API.

## See Also

- [object xcodeMetrics](xcodemetrics.md)
  A response that contains power and performance measurements for your app.
- [object DiagnosticInsight](diagnosticinsight.md)
  An AI-generated analysis of a recurring performance issue identified in your app’s diagnostic logs, with suggested fixes.
- [object DiagnosticSignaturesResponse](diagnosticsignaturesresponse.md)
  A response containing a list of unique performance issue signatures identified in your app’s diagnostic data.
- [object DiagnosticSignature](diagnosticsignature.md)
  A unique pattern identifying a recurring crash, hang, or disk-write exception in your app’s diagnostic logs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/diagnosticlogs)*