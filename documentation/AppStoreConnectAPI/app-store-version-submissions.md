# App Store version submissions

**Framework**: App Store Connect API

Submit versions of your app to App Review.

#### Overview

An `appStoreVersionSubmissions` resource enables you to submit a version of your app to App Review. This resource is the equivalent of clicking the Submit for Review button in the App Store Connect UI.

If your version submission is incomplete due to missing required information or other issues, you receive an error when you attempt to submit to App Review.

The `appStoreVersionSubmissions` resource is available while your submission request is live. For more information, see [`Submit for review`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-for-review).

## Topics

### Managing Review Submissions
- [Create an App Store version submission](post-v1-appstoreversionsubmissions.md)
  Submit an App Store version to App Review.
- [Delete an App Store Version Submission](delete-v1-appstoreversionsubmissions-_id_.md)
  Remove a version from App Store review.
### Objects
- [object AppStoreVersionSubmission](appstoreversionsubmission.md)
  The data structure that represents an App Store Version Submissions resource.
- [object AppStoreVersionSubmissionCreateRequest](appstoreversionsubmissioncreaterequest.md)
  The request body you use to create an App Store Version Submission.
- [object AppStoreVersionSubmissionResponse](appstoreversionsubmissionresponse.md)
  A response that contains a single App Store Version Submissions resource.

## See Also

- [Review submissions](review-submissions.md)
  Create and manage your submissions for review, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.
- [Review submission items](review-submission-items.md)
  Manage the contents of your review submission, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.
- [App Store review details](app-store-review-details.md)
  Manage the required information you provide for App Review.
- [App Clip App Store review details](app-clip-app-store-review-details.md)
  Manage required App Clip information you provide for App Review.
- [App Store review attachments](app-store-review-attachments.md)
  Manage the attachments you upload to App Store Connect for App Review.
- [Actors](actors.md)
  Get information about who or which service made a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-version-submissions)*