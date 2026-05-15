# List Item IDs

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the list of item IDs for a specific review submission.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/reviewSubmissions/{id}/relationships/items`

## Parameters

- `limit` (integer)

## See Also

- [List Review Submissions for an App](get-v1-reviewsubmissions.md)
  List recent and current review submissions for a specific app.
- [Read Review Submission Information](get-v1-reviewsubmissions-_id_.md)
  Read information about a specific review submisison.
- [List the Items in a Review Submission](get-v1-reviewsubmissions-_id_-items.md)
  List all the items in a specific review submission.
- [List Review Submission IDs](get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.
- [Modify a Review Submission](patch-v1-reviewsubmissions-_id_.md)
  Edit the details or contents of a review submission.
- [Create a Review Submission](post-v1-reviewsubmissions.md)
  Create a review submission for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-reviewsubmissions-_id_-relationships-items)*