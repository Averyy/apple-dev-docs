# Create a review submission

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a review submission for a specific app.

**Availability**:
- App Store Connect API 1.7+

## Mentions

- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)
- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)
- [Configuring Game center activities](configuring-game-center-activities.md)
- [Configuring Game Center challenges](configuring-game-center-challenges.md)

#### Overview

> **Note**: The attribute `platform` is no longer required when using [`Create a review submission`](post-v1-reviewsubmissions.md). You can optionally add the attribute platform when using [`Modify a review submission`](patch-v1-reviewsubmissions-_id_.md).

## See Also

- [List review submissions for an app](get-v1-reviewsubmissions.md)
  List recent and current review submissions for a specific app.
- [Read review submission information](get-v1-reviewsubmissions-_id_.md)
  Read information about a specific review submisison.
- [List the items in a review submission](get-v1-reviewsubmissions-_id_-items.md)
  List all the items in a specific review submission.
- [List item Ids](get-v1-reviewsubmissions-_id_-relationships-items.md)
  Get the list of item IDs for a specific review submission.
- [List review submission Ids](get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.
- [Modify a review submission](patch-v1-reviewsubmissions-_id_.md)
  Edit the details or contents of a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-reviewsubmissions)*