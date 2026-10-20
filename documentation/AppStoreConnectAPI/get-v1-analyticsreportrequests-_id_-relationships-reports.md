# Read reports ids for a specific request

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of reports Ids from a specific analytics report request.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/analyticsReportRequests/{id}/relationships/reports`

## Parameters

- `limit` (integer)

## See Also

- [Request Reports](post-v1-analyticsreportrequests.md)
  Request analytics reports for your apps.
- [Read Report Requests](get-v1-apps-_id_-analyticsreportrequests.md)
  Read analytics report requests for a specific app.
- [Read Report Request Information](get-v1-analyticsreportrequests-_id_.md)
  Get details for and the state of a specific analytics report request.
- [Read Reports for a Specific Request](get-v1-analyticsreportrequests-_id_-reports.md)
  Get a list of reports generated from a specific analytics report request.
- [Delete a Report Request](delete-v1-analyticsreportrequests-_id_.md)
  Remove a specific analytics report request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreportrequests-_id_-relationships-reports)*