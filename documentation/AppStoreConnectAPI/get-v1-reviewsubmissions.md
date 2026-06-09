# List Review Submissions for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

List recent and current review submissions for a specific app.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/reviewSubmissions`

## Parameters

- `fields[actors]` ([string])
- `fields[appStoreVersions]` ([string])
- `fields[apps]` ([string])
- `fields[reviewSubmissionItems]` ([string])
- `fields[reviewSubmissions]` ([string])
- `filter[app]` ([string]) *(required)*
- `filter[platform]` ([string])
- `filter[state]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[items]` (integer)

## See Also

- [Read Review Submission Information](get-v1-reviewsubmissions-_id_.md)
  Read information about a specific review submisison.
- [List the Items in a Review Submission](get-v1-reviewsubmissions-_id_-items.md)
  List all the items in a specific review submission.
- [List item IDs](get-v1-reviewsubmissions-_id_-relationships-items.md)
  Get the list of item IDs for a specific review submission.
- [List review submission IDs](get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.
- [Modify a Review Submission](patch-v1-reviewsubmissions-_id_.md)
  Edit the details or contents of a review submission.
- [Create a Review Submission](post-v1-reviewsubmissions.md)
  Create a review submission for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-reviewsubmissions)*