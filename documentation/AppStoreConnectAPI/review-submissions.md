# Review submissions

**Framework**: App Store Connect API

Create and manage your submissions for review, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.

#### Overview

The attribute `platform` is no longer required when using [`Create a Review Submission`](post-v1-reviewsubmissions.md). You can optionally add the attribute platform when using [`Modify a Review Submission`](patch-v1-reviewsubmissions-_id_.md).

## Topics

### Endpoints
- [List Review Submissions for an App](get-v1-reviewsubmissions.md)
  List recent and current review submissions for a specific app.
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
### Objects
- [object ReviewSubmission](reviewsubmission.md)
  A formal submission to App Store review grouping one or more items — app versions, in-app purchases, or events — for simultaneous review.
- [object ReviewSubmissionItem](reviewsubmissionitem.md)
  An individual reviewable item — such as an app version, in-app purchase, or App Clip — included in a review submission.
- [object ReviewSubmissionUpdateRequest](reviewsubmissionupdaterequest.md)
  The request body you use to update a review submission update request.
- [object ReviewSubmissionCreateRequest](reviewsubmissioncreaterequest.md)
  The request body for creating a review submission for an App Store version or associated items.
- [object ReviewSubmissionResponse](reviewsubmissionresponse.md)
  The response body for endpoints that create, read, or modify a single review submission.
- [object ReviewSubmissionsResponse](reviewsubmissionsresponse.md)
  The response body for endpoints that list review submissions for an app.
- [object AppReviewSubmissionsLinkagesResponse](appreviewsubmissionslinkagesresponse.md)
  A response containing the resource identifiers of review submissions associated with an app.
- [object ReviewSubmissionItemsLinkagesResponse](reviewsubmissionitemslinkagesresponse.md)
  A response containing the resource identifiers of items included in a review submission.

## See Also

- [Review submission items](review-submission-items.md)
  Manage the contents of your review submission, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.
- [App Store review details](app-store-review-details.md)
  Manage the required information you provide for App Review.
- [App Clip App Store review details](app-clip-app-store-review-details.md)
  Manage required App Clip information you provide for App Review.
- [App Store review attachments](app-store-review-attachments.md)
  Manage the attachments you upload to App Store Connect for App Review.
- [App Store version submissions](app-store-version-submissions.md)
  Submit versions of your app to App Review.
- [Actors](actors.md)
  Get information about who or which service made a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/review-submissions)*