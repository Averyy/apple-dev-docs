# List the Items in a Review Submission

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all the items in a specific review submission.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/reviewSubmissions/{id}/items`

## Parameters

- `fields[reviewSubmissionItems]` ([string])
- `limit` (integer)
- `fields[appStoreVersionExperiments]` ([string])
- `fields[appStoreVersions]` ([string])
- `fields[appCustomProductPageVersions]` ([string])
- `fields[appEvents]` ([string])
- `include` ([string])
- `fields[backgroundAssetVersions]` ([string])
- `fields[gameCenterAchievementVersions]` ([string])
- `fields[gameCenterActivityVersions]` ([string])
- `fields[gameCenterChallengeVersions]` ([string])
- `fields[gameCenterLeaderboardSetVersions]` ([string])
- `fields[gameCenterLeaderboardVersions]` ([string])
- `fields[inAppPurchaseVersions]` ([string])
- `fields[subscriptionGroupVersions]` ([string])
- `fields[subscriptionVersions]` ([string])

## See Also

- [List Review Submissions for an App](get-v1-reviewsubmissions.md)
  List recent and current review submissions for a specific app.
- [Read Review Submission Information](get-v1-reviewsubmissions-_id_.md)
  Read information about a specific review submisison.
- [List item IDs](get-v1-reviewsubmissions-_id_-relationships-items.md)
  Get the list of item IDs for a specific review submission.
- [List review submission IDs](get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.
- [Modify a Review Submission](patch-v1-reviewsubmissions-_id_.md)
  Edit the details or contents of a review submission.
- [Create a Review Submission](post-v1-reviewsubmissions.md)
  Create a review submission for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-reviewsubmissions-_id_-items)*