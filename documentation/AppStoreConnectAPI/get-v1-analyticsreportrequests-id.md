# Read Report Request Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details for and the state of a specific analytics report request.

**Availability**:
- App Store Connect API 3.4+

## Mentions

- [Downloading Analytics Reports](downloading-analytics-reports.md)

#### Discussion

> **Note**:  If you don’t retrieve data for a long time, a report request changes to `stoppedDueToInactivity`. You need to make a new request to resume getting reports.

##### Examples Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/d48c69c5-9bcb-4592-abbd-08a9411b0231
```

**Response**:

```json
{
  "data": {
    "type": "analyticsReportRequests",
    "id": "d48c69c5-9bcb-4592-abbd-08a9411b0231",
    "attributes": {
      "accessType": "ONGOING",
      "stoppedDueToInactivity": false
    },
    "relationships": {
      "reports": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/d48c69c5-9bcb-4592-abbd-08a9411b0231/relationships/reports",
          "related": "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/d48c69c5-9bcb-4592-abbd-08a9411b0231/reports"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/d48c69c5-9bcb-4592-abbd-08a9411b0231"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/d48c69c5-9bcb-4592-abbd-08a9411b0231"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/{id}`

## Parameters

- `fields[analyticsReportRequests]` ([string]): Additional fields to include for each analytics report requests resource returned by the response.
- `fields[analyticsReports]` ([string]): Additional fields to include for each analytics reports resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[reports]` (integer): The maximum number of related reports resources to return.

## See Also

- [Request Reports](post-v1-analyticsreportrequests.md)
  Request analytics reports for your apps.
- [Read Report Requests](get-v1-apps-_id_-analyticsreportrequests.md)
  Read analytics report requests for a specific app.
- [Read Reports for a Specific Request](get-v1-analyticsreportrequests-_id_-reports.md)
  Get a list of reports generated from a specific analytics report request.
- [Read reports ids for a specific request](get-v1-analyticsreportrequests-_id_-relationships-reports.md)
  Get a list of reports Ids from a specific analytics report request.
- [Delete a Report Request](delete-v1-analyticsreportrequests-_id_.md)
  Remove a specific analytics report request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreportrequests-_id_)*