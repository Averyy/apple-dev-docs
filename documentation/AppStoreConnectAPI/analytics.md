# Analytics

**Framework**: App Store Connect API

Get data about your apps and usage.

#### Overview

Use the Analytics Reports API to analyze your app’s performance on iOS and the App Store and find opportunities for improvement. To learn more about interpreting the data using the glossary of report fields and definitions, see [`Analytics Reports`](https://developer.apple.com/documentation/analytics-reports).

To help protect user privacy, where appropriate, Apple is applying measures to protect personally identifable infomation. For specific reports, Apple adds noise or applies crowd anonymity, and uses both approaches for other reports. Apple only reports totals when a specific number of data points are available. For more infomation about these measures, see [`Protecting user privacy in report data`](https://developer.apple.com/documentation/Analytics-Reports/privacy).

To download analytics reports, be sure you have one of the following user roles:

- ADMIN
- SALES AND REPORTS
- FINANCE

This table outlines which roles can use which resources:

| Role | Manage requests | List and download reports |
| --- | --- | --- |
| Admin | [`Request Reports`](post-v1-analyticsreportrequests.md) and [`Delete a Report Request`](delete-v1-analyticsreportrequests-_id_.md) | [`Read Reports for a Specific Request`](get-v1-analyticsreportrequests-_id_-reports.md) |
| Finance |  | [`Read Reports for a Specific Request`](get-v1-analyticsreportrequests-_id_-reports.md) |
| Sales and Reports |  | [`Read Reports for a Specific Request`](get-v1-analyticsreportrequests-_id_-reports.md) |

The Sales and Reports role can also read [`Download Sales and Trends Reports`](get-v1-salesreports.md) in addition to Analytics Reports.

To learn more about roles, see [`Program Roles`](https://developer.apple.comhttps://developer.apple.com/support/roles/).

> **Note**:  If you have any questions about the data made available in this API, including about how Apple applies privacy measures to protect user privacy and complies with legal obligations, contact Apple through Feedback Assistant by selecting the following option: Developer Tools & Resources > App Store Connect API > Data Request [`Learn more`](https://developer.apple.comhttps://support.apple.com/guide/feedback-assistant/welcome/mac) about how to use Feedback Assistant.

## Topics

### Essentials
- [Downloading Analytics Reports](downloading-analytics-reports.md)
  Learn how to request and review data about your apps, their usage, engagement, and performance.
### Making, Reading, and Deleting Requests
- [Request Reports](post-v1-analyticsreportrequests.md)
  Request analytics reports for your apps.
- [Read Report Requests](get-v1-apps-_id_-analyticsreportrequests.md)
  Read analytics report requests for a specific app.
- [Read Report Request Information](get-v1-analyticsreportrequests-_id_.md)
  Get details for and the state of a specific analytics report request.
- [Read Reports for a Specific Request](get-v1-analyticsreportrequests-_id_-reports.md)
  Get a list of reports generated from a specific analytics report request.
- [Read Reports IDs for a Specific Request](get-v1-analyticsreportrequests-_id_-relationships-reports.md)
  Get a list of reports Ids from a specific analytics report request.
- [Delete a Report Request](delete-v1-analyticsreportrequests-_id_.md)
  Remove a specific analytics report request.
### Reading Reports, Instances, and Segments
- [Read Report Information](get-v1-analyticsreports-_id_.md)
  Get details for a specific analytics report.
- [Read a List of Instances of a Report](get-v1-analyticsreports-_id_-instances.md)
  Read list of all the granularity options for a specific type of analytics report.
- [Read Report Instance Information](get-v1-analyticsreportinstances-_id_.md)
  Get details for a specific instance of an analytics report.
- [Read the Segments for a Report](get-v1-analyticsreportinstances-_id_-segments.md)
  Get details for a specific analytics report segment.
- [Read Segment IDs for a Report](get-v1-analyticsreportinstances-_id_-relationships-segments.md)
  Get Ids for a specific analytics report segment.
- [Read the Details for a Report Segment](get-v1-analyticsreportsegments-_id_.md)
  Get details and download information for a specific analytics report segment.
- [Read a List of a Report Instant IDs](get-v1-analyticsreports-_id_-relationships-instances.md)
  Read list of all the instance IDs for a specific type of analytics report.
### Objects
- [object AnalyticsReportRequest](analyticsreportrequest.md)
  The data structure that represents an analytics report request.
- [object AnalyticsReportRequestCreateRequest](analyticsreportrequestcreaterequest.md)
  The request body you use to create an analytics report request.
- [object AnalyticsReportRequestResponse](analyticsreportrequestresponse.md)
  A response that contains a single analytics report request resource.
- [object AnalyticsReportRequestsResponse](analyticsreportrequestsresponse.md)
  A response that contains a list of analytics report request resources.
- [object AnalyticsReport](analyticsreport.md)
  The data structure that represents an analytics report.
- [object AnalyticsReportResponse](analyticsreportresponse.md)
  A response that contains a single analytics report resource.
- [object AnalyticsReportsResponse](analyticsreportsresponse.md)
  A response that contains a list of analytics report resources.
- [object AnalyticsReportInstance](analyticsreportinstance.md)
  The data structure that represents an analytics report instance.
- [object AnalyticsReportInstanceResponse](analyticsreportinstanceresponse.md)
  A response that contains a single analytics report instance resource.
- [object AnalyticsReportInstancesResponse](analyticsreportinstancesresponse.md)
  A response that contains a list of analytics report instance resources.
- [object AnalyticsReportSegment](analyticsreportsegment.md)
  The data structure that represents an analytics report segment.
- [object AnalyticsReportSegmentResponse](analyticsreportsegmentresponse.md)
  A response that contains a single analytics report segment resource.
- [object AnalyticsReportSegmentsResponse](analyticsreportsegmentsresponse.md)
  A response that contains a list of analytics report segment resources.
- [object AnalyticsReportInstanceSegmentsLinkagesResponse](analyticsreportinstancesegmentslinkagesresponse.md)
- [object AnalyticsReportInstancesLinkagesResponse](analyticsreportinstanceslinkagesresponse.md)
- [object AnalyticsReportRequestReportsLinkagesResponse](analyticsreportrequestreportslinkagesresponse.md)
- [object AppAnalyticsReportRequestsLinkagesResponse](appanalyticsreportrequestslinkagesresponse.md)

## See Also

- [Sales and Finance](sales-and-finance.md)
  Download your sales and financial reports.
- [Power and Performance Metrics and Logs](power-and-performance-metrics-and-logs.md)
  Get power and performance metrics, logs, and signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/analytics)*