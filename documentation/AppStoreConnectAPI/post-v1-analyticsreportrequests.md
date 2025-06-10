# Request reports

**Framework**: App Store Connect API  
**Kind**: httpRequest

Request analytics reports for your apps.

**Availability**:
- App Store Connect API 3.4+

## Mentions

- [Downloading Analytics Reports](downloading-analytics-reports.md)

#### Discussion

When making a request with this endpoint, the `accessType` `ONGOING` is most common and provides current data. This report request generates reports daily for each granularity: daily, weekly, and monthly. Use `ONE_TIME_SNAPSHOT` to get historical data.

##### Example Request and Response

## See Also

- [Read report requests](get-v1-apps-_id_-analyticsreportrequests.md)
  Read analytics report requests for a specific app.
- [Read report request information](get-v1-analyticsreportrequests-_id_.md)
  Get details for and the state of a specific analytics report request.
- [Read reports for a specific request](get-v1-analyticsreportrequests-_id_-reports.md)
  Get a list of reports generated from a specific analytics report request.
- [Read reports Ids for a specific request](get-v1-analyticsreportrequests-_id_-relationships-reports.md)
  Get a list of reports Ids from a specific analytics report request.
- [Delete a report request](delete-v1-analyticsreportrequests-_id_.md)
  Remove a specific analytics report request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-analyticsreportrequests)*