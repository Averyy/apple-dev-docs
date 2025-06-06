# List All Diagnostic Signatures for a Build

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the aggregate backtrace signatures captured for a specific build.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 3.5 release notes](app-store-connect-api-3-5-release-notes.md)
- [App Store Connect API 2.0 release notes](app-store-connect-api-2-0-release-notes.md)

#### Discussion

The example below requests the top two weighted disk write diagnostic signatures. The example response returns two signatures that are responsible for 85% and 7% of disk writes.

##### Example Request and Response

## See Also

- [Retrieve Power and Performance Metrics and Log Insights](retrieve-power-and-performance-metrics-and-log-insights.md)
  Use the App Store Connect API to collect and parse diagnostic logs and metrics for your apps.
- [Get Power and Performance Metrics for an App](get-v1-apps-_id_-perfpowermetrics.md)
  Get the performance and power metrics data for the most recent version of an app.
- [Get Power and Performance Metrics for a Build](get-v1-builds-_id_-perfpowermetrics.md)
  Get the performance and power metrics data for a specific build.
- [Download Logs for a Diagnostic Signature](get-v1-diagnosticsignatures-_id_-logs.md)
  Get the anonymized backtrace logs associated with a specific diagnostic signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-diagnosticsignatures)*