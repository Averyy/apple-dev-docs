# App Store review details

**Framework**: App Store Connect API

Manage the required information you provide for App Review.

#### Overview

Use `appStoreReviewDetails` to provide information required for App Review. This information isn’t displayed on the App Store. Required attributes for App Review are:

- Contact first and last name
- Contact phone number
- Contact email address
- Whether testing your app requires a demo account
- Demo account name (if your app uses a single sign-on service)
- Demo account password (if your app uses a single sign-on service)

Optionally, provide notes for the review team using the notes attribute. If you need to attach a file for App Review, use the [`App Store review attachments`](app-store-review-attachments.md) resource.

For more information see [`App Review information`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-review-information).

## Topics

### Creating, Modifying, and Reading Review Details
- [Create an App Store Review Detail](post-v1-appstorereviewdetails.md)
  Add App Store review details to an App Store version, including contact and demo account information.
- [Read App Store Review Detail Information](get-v1-appstorereviewdetails-_id_.md)
  Get App Review details you provided, including contact information, demo account, and notes.
- [GET /v1/appStoreReviewDetails/{id}/relationships/appStoreReviewAttachments](get-v1-appstorereviewdetails-_id_-relationships-appstorereviewattachments.md)
- [Modify an App Store Review Detail](patch-v1-appstorereviewdetails-_id_.md)
  Update the app store review details, including the contact information, demo account, and notes.
### Objects
- [object AppStoreReviewDetail](appstorereviewdetail.md)
  The data structure that represent an App Store Review Details  resource.
- [object AppStoreReviewDetailCreateRequest](appstorereviewdetailcreaterequest.md)
  The request body you use to create an App Store Review Detail.
- [object AppStoreReviewDetailUpdateRequest](appstorereviewdetailupdaterequest.md)
  The request body you use to update an App Store Review Detail.
- [object AppStoreReviewDetailResponse](appstorereviewdetailresponse.md)
  A response that contains a single App Store Review Details resource.
- [object AppStoreReviewDetailAppStoreReviewAttachmentsLinkagesResponse](appstorereviewdetailappstorereviewattachmentslinkagesresponse.md)

## See Also

- [Review submissions](review-submissions.md)
  Create and manage your submissions for review, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.
- [Review submission items](review-submission-items.md)
  Manage the contents of your review submission, which can include your App Store version, App Store version experiments, custom product page versions, and in-app events.
- [App Clip App Store review details](app-clip-app-store-review-details.md)
  Manage required App Clip information you provide for App Review.
- [App Store review attachments](app-store-review-attachments.md)
  Manage the attachments you upload to App Store Connect for App Review.
- [App Store version submissions](app-store-version-submissions.md)
  Submit versions of your app to App Review.
- [Actors](actors.md)
  Get information about who or which service made a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-review-details)*