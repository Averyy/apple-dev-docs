# Commit an app store review attachment

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit an app screenshot after uploading it to the App Store.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appStoreReviewAttachments/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store review attachment resource ID from the [`List all review attachments for an app store review detail`](get-v1-appstorereviewdetails-_id_-appstorereviewattachments.md) response.

## See Also

- [Create an app store review attachment](post-v1-appstorereviewattachments.md)
  Attach a document for App Review to an App Store version.
- [Delete an app store review attachment](delete-v1-appstorereviewattachments-_id_.md)
  Remove an attachment before you send your app to App Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appstorereviewattachments-_id_)*