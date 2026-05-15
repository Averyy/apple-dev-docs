# Read Report Requests

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read analytics report requests for a specific app.

**Availability**:
- App Store Connect API 3.4+

## Mentions

- [Downloading Analytics Reports](downloading-analytics-reports.md)

#### Discussion

##### Examples Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/apps/1476097583/analyticsReportRequests
```

**Response**:

```json
{
  "data": [
    {
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
    {
      "type": "analyticsReportRequests",
      "id": "A157dd7a-4fe2-479b-8d25-a8e4228c5b81",
      "attributes": {
        "accessType": "ONE_TIME_SNAPSHOT",
        "stoppedDueToInactivity": false
      },
      "relationships": {
        "reports": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/A157dd7a-4fe2-479b-8d25-a8e4228c5b81/relationships/reports",
            "related": "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/A157dd7a-4fe2-479b-8d25-a8e4228c5b81/reports"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/A157dd7a-4fe2-479b-8d25-a8e4228c5b81"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/389801252/analyticsReportRequests"
  },
  "meta": {
    "paging": {
      "total": 2,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/analyticsReportRequests`

## Parameters

- `fields[analyticsReportRequests]` ([string])
- `fields[analyticsReports]` ([string])
- `filter[accessType]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[reports]` (integer)

## See Also

- [Request Reports](post-v1-analyticsreportrequests.md)
  Request analytics reports for your apps.
- [Read Report Request Information](get-v1-analyticsreportrequests-_id_.md)
  Get details for and the state of a specific analytics report request.
- [Read Reports for a Specific Request](get-v1-analyticsreportrequests-_id_-reports.md)
  Get a list of reports generated from a specific analytics report request.
- [Read Reports IDs for a Specific Request](get-v1-analyticsreportrequests-_id_-relationships-reports.md)
  Get a list of reports Ids from a specific analytics report request.
- [Delete a Report Request](delete-v1-analyticsreportrequests-_id_.md)
  Remove a specific analytics report request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-analyticsreportrequests)*