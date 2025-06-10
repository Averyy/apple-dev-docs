# Review submissions

**Framework**: App Store Connect API

Create and manage your submissions for review, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.

## Topics

### Endpoints
- [List review submissions for an app](get-v1-reviewsubmissions.md)
  List recent and current review submissions for a specific app.
- [Read review submission information](get-v1-reviewsubmissions-_id_.md)
  Read information about a specific review submisison.
- [List the items in a review submission](get-v1-reviewsubmissions-_id_-items.md)
  List all the items in a specific review submission.
- [GET /v1/reviewSubmissions/{id}/relationships/items](get-v1-reviewsubmissions-_id_-relationships-items.md)
- [GET /v1/apps/{id}/relationships/reviewSubmissions](get-v1-apps-_id_-relationships-reviewsubmissions.md)
- [Modify a review submission](patch-v1-reviewsubmissions-_id_.md)
  Edit the details or contents of a review submission.
- [Create a review submission](post-v1-reviewsubmissions.md)
  Create a review submission for a specific app.
### Objects
- [object ReviewSubmission](reviewsubmission.md)
- [object ReviewSubmissionItem](reviewsubmissionitem.md)
- [object ReviewSubmissionUpdateRequest](reviewsubmissionupdaterequest.md)
- [object ReviewSubmissionCreateRequest](reviewsubmissioncreaterequest.md)
- [object ReviewSubmissionResponse](reviewsubmissionresponse.md)
- [object ReviewSubmissionsResponse](reviewsubmissionsresponse.md)
- [object AppReviewSubmissionsLinkagesResponse](appreviewsubmissionslinkagesresponse.md)
- [object ReviewSubmissionItemsLinkagesResponse](reviewsubmissionitemslinkagesresponse.md)

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