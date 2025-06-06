# Downloading Analytics Reports

**Framework**: App Store Connect API

Learn how to request and review data about your apps, their usage, engagement, and performance.

#### Overview

Use the Analytics Reports API to request and download reports for your apps. This API provides access to reports in these categories:

> **Note**:  To learn more about the contents of each report, see [`Analytics Reports`](https://developer.apple.com/documentation/analytics-reports).

 To learn more about the contents of each report, see [`Analytics Reports`](https://developer.apple.com/documentation/analytics-reports).

##### Understand Roles and Reports

To download analytics reports, be sure your API key has one of the following roles, because each role has access to specific endpoints:

| Role | Manage requests | List and download reports |
| --- | --- | --- |
| Admin | [`Request reports`](post-v1-analyticsreportrequests.md) and [`Delete a report request`](delete-v1-analyticsreportrequests-_id_.md) | [`Read reports for a specific request`](get-v1-analyticsreportrequests-_id_-reports.md) |
| Sales and Reports |  | [`Read reports for a specific request`](get-v1-analyticsreportrequests-_id_-reports.md) |
| Finance |  | [`Read reports for a specific request`](get-v1-analyticsreportrequests-_id_-reports.md) |

> **Note**:  If you share an API key for your developer account with a third party for analyzing or processing your reports, select the `Sales and Reports` role when generating a new key. This role can access to the [`Download Sales and Trends Reports`](get-v1-salesreports.md) but can’t access [`Download Finance Reports`](get-v1-financereports.md) endpoint.

 If you share an API key for your developer account with a third party for analyzing or processing your reports, select the `Sales and Reports` role when generating a new key. This role can access to the [`Download Sales and Trends Reports`](get-v1-salesreports.md) but can’t access [`Download Finance Reports`](get-v1-financereports.md) endpoint.

##### Request Analytics Reports

Start by using the [`Request reports`](post-v1-analyticsreportrequests.md) API to request generation of reports for one of your apps. There are two types of `accessTypes` for report requests:

Your first report request generates in 1–2 days. Subsequent `ONGOING` reports are available daily.

To see a list of your report requests, use [`Read report requests`](get-v1-apps-_id_-analyticsreportrequests.md).

To read more information about a specific request, use [`Read report request information`](get-v1-analyticsreportrequests-_id_.md) with the `ID` from [`Read report requests`](get-v1-apps-_id_-analyticsreportrequests.md) to see if the report is still active and generating new reports.

> **Note**:  If you don’t retrieve data for a long time, a report request changes to `stoppedDueToInactivity`. You need to make a new request to resume getting reports.

 If you don’t retrieve data for a long time, a report request changes to `stoppedDueToInactivity`. You need to make a new request to resume getting reports.

##### Read the Analytics Reports

Use [`Read reports for a specific request`](get-v1-analyticsreportrequests-_id_-reports.md) to check whether your reports are available. This endpoint lists all the reports that the API generated to fulfill your request. For more about the information in each report see [`Analytics Reports`](https://developer.apple.com/documentation/analytics-reports).

Each report has a name and category attributes, like this:

```other
      "attributes": {
        "name": "App Store Discovery and Engagement Detailed",
        "category": "APP_STORE_ENGAGEMENT"
      }
```

Some reports have two content levels, Standard or Detailed, which the report’s name reflects with a suffix. Standard reports include fields not easily related to uniquely identifiable user data. Detailed reports include all fields and also include additional privacy measures for the data, to help protect uniquely identifiable information for individuals.

To learn more about what data is in each report and report type, see [`Analytics Reports`](https://developer.apple.com/documentation/analytics-reports).

##### Download Specific Analytic Report Data

Select a report of interest and use [`Read a list of instances of a report`](get-v1-analyticsreports-_id_-instances.md) to see a list of report instances filtered by `granularity` and `processingDate`.  are discreet containers for a report data set. You can choose a `granularity` of daily, weekly, or monthly for the reports in an instance. The `processingDate` represents new data available that day. The data for a given report with a specific `processingDate` might contain data for that day, full data for past dates, or both.

Then, you use the [`Read the segments for a report`](get-v1-analyticsreportinstances-_id_-segments.md) endpoint to get a download URL for the report.  are the actual report files, and based on the amount of data for a specific instance, you might have multiple segments to download. You can also use `sizeInBytes` and `checksum` to verify a specific report segment downloaded successfully.

##### Analyze Your App Data

After you download some reports, you can start analyzing the data and learning more about how people use your apps. To learn more about the fields and descriptions in these reports see [`Analytics Reports`](https://developer.apple.com/documentation/analytics-reports).

For `ONGOING` report requests you need to regularly use these APIs to get updated data for these reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/downloading-analytics-reports)*