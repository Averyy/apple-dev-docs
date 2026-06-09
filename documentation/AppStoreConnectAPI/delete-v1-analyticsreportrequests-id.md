# Delete a Report Request

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove a specific analytics report request.

**Availability**:
- App Store Connect API 3.4+

## Mentions

- [Downloading Analytics Reports](downloading-analytics-reports.md)

#### Discussion

##### Examples Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/d48c69c5-9bcb-4592-abbd-08a9411b0231

```

**Response**:

```json
204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the analytics report request resource ID from the [`Read Report Requests`](get-v1-apps-_id_-analyticsreportrequests.md) response.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-analyticsreportrequests-_id_)*