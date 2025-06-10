# Manually Release an App Store Approved Version of Your App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Release an approved version of your app to the App Store.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

When you submit your app for review, if itʼs approved and the status changes to Pending Developer Release, then you can release a version. For more information about app review, see [`Submit for review`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-for-review). For more information about manually releasing versions, see [`Select a version release option`](https://developer.apple.comhttps://devcms.apple.com/help/app-store-connect/manage-your-apps-availability/select-a-version-release-option). For more information about app status, see [`App and submission statuses`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-and-submission-statuses).

> ❗ **Important**:  Send this request only when you’re ready to publish your version. You can’t cancel this request.

## Request Body

The request body you use to manually release an approved version of your app to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appstoreversionreleaserequests)*