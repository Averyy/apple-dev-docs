# App Store review attachments

**Framework**: App Store Connect API

Manage the attachments you upload to App Store Connect for App Review.

#### Overview

Use an `appReviewAttachments` resource to upload specific app documentation, demo videos, and other items to App Store Connect, to help prevent delays during the app review process.

For more information, see [`App Review information`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-review-information).

## Topics

### Reading Attachment Information
- [Read app store review attachment information](get-v1-appstorereviewattachments-_id_.md)
  Get information about an App Store review attachment and its upload and processing status.
- [List all review attachments for an app store review detail](get-v1-appstorereviewdetails-_id_-appstorereviewattachments.md)
  List all the App Store review attachments you include with a version when you submit it for App Review.
- [List App Store review attachment IDs for an App Store review detail](get-v1-appstorereviewdetails-_id_-relationships-appstorereviewattachments.md)
### Creating, Modifying, and Deleting Attachments
- [Create an app store review attachment](post-v1-appstorereviewattachments.md)
  Attach a document for App Review to an App Store version.
- [Commit an app store review attachment](patch-v1-appstorereviewattachments-_id_.md)
  Commit an app screenshot after uploading it to the App Store.
- [Delete an app store review attachment](delete-v1-appstorereviewattachments-_id_.md)
  Remove an attachment before you send your app to App Review.
### Objects
- [object AppStoreReviewAttachment](appstorereviewattachment.md)
  A file attached to an App Store review submission to provide reviewers with additional context, such as demo credentials or notes.
- [object AppStoreReviewAttachmentCreateRequest](appstorereviewattachmentcreaterequest.md)
  The request body you use to create an App Store Review Attachment.
- [object AppStoreReviewAttachmentResponse](appstorereviewattachmentresponse.md)
  The response body for endpoints that create, read, or modify a file attached to an App Store review submission.
- [object AppStoreReviewAttachmentUpdateRequest](appstorereviewattachmentupdaterequest.md)
  The request body you use to update an App Store Review Attachment.
- [object AppStoreReviewAttachmentsResponse](appstorereviewattachmentsresponse.md)
  The response body for endpoints that list files attached to an App Store review submission.

## See Also

- [Review submissions](review-submissions.md)
  Create and manage your submissions for review, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.
- [Review submission items](review-submission-items.md)
  Manage the contents of your review submission, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.
- [App Store review details](app-store-review-details.md)
  Manage the required information you provide for App Review.
- [App Clip App Store review details](app-clip-app-store-review-details.md)
  Manage required App Clip information you provide for App Review.
- [App Store version submissions](app-store-version-submissions.md)
  Submit versions of your app to App Review.
- [Actors](actors.md)
  Get information about who or which service made a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-review-attachments)*