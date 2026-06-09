# DiagnosticSignature

**Framework**: App Store Connect API  
**Kind**: dictionary

A unique pattern identifying a recurring crash, hang, or disk-write exception in your app’s diagnostic logs.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object DiagnosticSignature
```

## Topics

### Objects
- [object DiagnosticSignature.Attributes](diagnosticsignature/attributes-data.dictionary.md)
  Attributes that describe a Diagnostic Signatures resource.
### Dictionaries
- [object DiagnosticSignature.Relationships](diagnosticsignature/relationships-data.dictionary.md)

## Properties

- `attributes` (DiagnosticSignature.Attributes): Attributes that describe the diagnostic signature resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a diagnostic signature.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (DiagnosticSignature.Relationships)
- `type` (string) *(required)*: The resource type.

## See Also

- [object xcodeMetrics](xcodemetrics.md)
  A response that contains power and performance measurements for your app.
- [object DiagnosticInsight](diagnosticinsight.md)
  An AI-generated analysis of a recurring performance issue identified in your app’s diagnostic logs, with suggested fixes.
- [object DiagnosticSignaturesResponse](diagnosticsignaturesresponse.md)
  A response containing a list of unique performance issue signatures identified in your app’s diagnostic data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/diagnosticsignature)*