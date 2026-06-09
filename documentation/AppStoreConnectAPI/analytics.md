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

The Sales and Reports role can also read [`Download sales and trends reports`](get-v1-salesreports.md) in addition to Analytics Reports.

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
- [Read reports ids for a specific request](get-v1-analyticsreportrequests-_id_-relationships-reports.md)
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
- [Read segment ids for a report](get-v1-analyticsreportinstances-_id_-relationships-segments.md)
  Get Ids for a specific analytics report segment.
- [Read the Details for a Report Segment](get-v1-analyticsreportsegments-_id_.md)
  Get details and download information for a specific analytics report segment.
- [Read a list of a report instance ids](get-v1-analyticsreports-_id_-relationships-instances.md)
  Read list of all the instance IDs for a specific type of analytics report.
### Objects
- [object AnalyticsReportRequest](analyticsreportrequest.md)
  A request to generate ongoing analytics reports for an app, specifying the report type and access frequency.
- [object AnalyticsReportRequestCreateRequest](analyticsreportrequestcreaterequest.md)
  The request body you use to create an analytics report request.
- [object AnalyticsReportRequestResponse](analyticsreportrequestresponse.md)
  The response body for endpoints that create or read an analytics report request.
- [object AnalyticsReportRequestsResponse](analyticsreportrequestsresponse.md)
  The response body for endpoints that list analytics report requests for an app.
- [object AnalyticsReport](analyticsreport.md)
  A generated analytics report containing App Store performance data produced from a report request.
- [object AnalyticsReportResponse](analyticsreportresponse.md)
  The response body for endpoints that read a single analytics report.
- [object AnalyticsReportsResponse](analyticsreportsresponse.md)
  The response body for endpoints that list analytics reports for a report request.
- [object AnalyticsReportInstance](analyticsreportinstance.md)
  A time-bounded instance of an analytics report, representing data for a specific reporting period.
- [object AnalyticsReportInstanceResponse](analyticsreportinstanceresponse.md)
  The response body for endpoints that read a single analytics report instance.
- [object AnalyticsReportInstancesResponse](analyticsreportinstancesresponse.md)
  The response body for endpoints that list instances of an analytics report.
- [object AnalyticsReportSegment](analyticsreportsegment.md)
  A downloadable segment within an analytics report instance, containing a portion of the report’s CSV data.
- [object AnalyticsReportSegmentResponse](analyticsreportsegmentresponse.md)
  The response body for endpoints that read a single downloadable segment of an analytics report.
- [object AnalyticsReportSegmentsResponse](analyticsreportsegmentsresponse.md)
  The response body for endpoints that list the downloadable segments of an analytics report instance.
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