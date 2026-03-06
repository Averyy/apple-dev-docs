# Read report request information

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

- `fields[analyticsReportRequests]` ([string])
- `fields[analyticsReports]` ([string])
- `include` ([string])
- `limit[reports]` (integer)

## See Also

- [Request reports](post-v1-analyticsreportrequests.md)
  Request analytics reports for your apps.
- [Read report requests](get-v1-apps-_id_-analyticsreportrequests.md)
  Read analytics report requests for a specific app.
- [Read reports for a specific request](get-v1-analyticsreportrequests-_id_-reports.md)
  Get a list of reports generated from a specific analytics report request.
- [Read reports Ids for a specific request](get-v1-analyticsreportrequests-_id_-relationships-reports.md)
  Get a list of reports Ids from a specific analytics report request.
- [Delete a report request](delete-v1-analyticsreportrequests-_id_.md)
  Remove a specific analytics report request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreportrequests-_id_)*