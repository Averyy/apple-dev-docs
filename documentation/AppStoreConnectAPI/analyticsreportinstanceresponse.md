# AnalyticsReportInstanceResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single analytics report instance.

**Availability**:
- App Store Connect API 3.4+

## Declaration

```swift
object AnalyticsReportInstanceResponse
```

#### Discussion

Use this object with [`Read Report Instance Information`](get-v1-analyticsreportinstances-_id_.md).

## Properties

- `data` (AnalyticsReportInstance) *(required)*
- `links` (DocumentLinks) *(required)*

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/analyticsreportinstanceresponse)*