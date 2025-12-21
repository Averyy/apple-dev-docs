# Review submissions

**Framework**: App Store Connect API

Create and manage your submissions for review, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.

#### Overview

The attribute `platform` is no longer required when using [`Create a review submission`](post-v1-reviewsubmissions.md). You can optionally add the attribute platform when using [`Modify a review submission`](patch-v1-reviewsubmissions-_id_.md).

## Topics

### Endpoints
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
- [Create a review submission](post-v1-reviewsubmissions.md)
  Create a review submission for a specific app.
### Objects
- [object ReviewSubmission](reviewsubmission.md)
  The data structure that represents a review submission resource.
- [object ReviewSubmissionItem](reviewsubmissionitem.md)
  The data structure that represents a review submission item resource.
- [object ReviewSubmissionUpdateRequest](reviewsubmissionupdaterequest.md)
  The request body you use to update a review submission update request.
- [object ReviewSubmissionCreateRequest](reviewsubmissioncreaterequest.md)
  The request body you use to create a review submission create request resource.
- [object ReviewSubmissionResponse](reviewsubmissionresponse.md)
  A response that contains a single review submission resource.
- [object ReviewSubmissionsResponse](reviewsubmissionsresponse.md)
  A response that contains a list of review submission resources.
- [object AppReviewSubmissionsLinkagesResponse](appreviewsubmissionslinkagesresponse.md)
  A response that contains a list of IDs of related resources.
- [object ReviewSubmissionItemsLinkagesResponse](reviewsubmissionitemslinkagesresponse.md)
  A response that contains a list of IDs of related resources.

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