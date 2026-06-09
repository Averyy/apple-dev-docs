# Power and Performance Metrics and Logs

**Framework**: App Store Connect API

Get power and performance metrics, logs, and signatures.

#### Overview

The `perfPowerMetricsresource` resource is a read-only resource where you get the power and performance metrics and diagnostics for App Store versions of your app. Use this information to improve your app’s performance. Customers can opt-in to share this information with you on their devices.

A *metric* is a measurement of the power and performance impact of an app running on a device. The [`MetricCategory`](metriccategory.md) type lists the categories of measurements the system makes; for example, the `LAUNCH` metric measures how long it takes an app to present its first frame. Use the [`Get power and performance metrics for an app`](get-v1-apps-_id_-perfpowermetrics.md) and [`Get power and performance metrics for a build`](get-v1-builds-_id_-perfpowermetrics.md) endpoints to get the metrics reports for the most recent version of your app or for a specific build.

An *insight* is an automatically generated analysis that shows a trend based on a set of metrics data. Insights compare the performance of the most recent app version with previous versions. Look for insights in the response body object, [`xcodeMetrics`](xcodemetrics.md).

A *diagnostic signature* is a recurring pattern of function calls your app makes that are associated with a metric. To get a diagnostic log for a signature, first call the [`List all diagnostic signatures for a build`](get-v1-builds-_id_-diagnosticsignatures.md) endpoint to get the resource IDs for signatures you’re interested in. Then call [`Download logs for a diagnostic signature`](get-v1-diagnosticsignatures-_id_-logs.md) using the signature resource IDs to download the logs.

To learn more about power and performance metrics, see [`About Metrics organizer`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devb642b28ac), and `Improving Your App's Performance`.

## Topics

### Getting Metrics and Diagnostic Logs
- [Retrieve Power and Performance Metrics and Log Insights](retrieve-power-and-performance-metrics-and-log-insights.md)
  Use the App Store Connect API to collect and parse diagnostic logs and metrics for your apps.
- [Get power and performance metrics for an app](get-v1-apps-_id_-perfpowermetrics.md)
  Get the performance and power metrics data for the most recent version of an app.
- [Get power and performance metrics for a build](get-v1-builds-_id_-perfpowermetrics.md)
  Get the performance and power metrics data for a specific build.
- [List all diagnostic signatures for a build](get-v1-builds-_id_-diagnosticsignatures.md)
  List the aggregate backtrace signatures captured for a specific build.
- [Download logs for a diagnostic signature](get-v1-diagnosticsignatures-_id_-logs.md)
  Get the anonymized backtrace logs associated with a specific diagnostic signature.
### Objects and types
- [object xcodeMetrics](xcodemetrics.md)
  A response that contains power and performance measurements for your app.
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

## See Also

- [Generating Tokens for API Requests](generating-tokens-for-api-requests.md)
  Create JSON Web Tokens (JWTs) signed with your private key to authorize API requests.
- [Sales and Finance](sales-and-finance.md)
  Download your sales and financial reports.
- [Analytics](analytics.md)
  Get data about your apps and usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/power-and-performance-metrics-and-logs)*