# Delete an app store review attachment

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove an attachment before you send your app to App Review.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appStoreReviewAttachments/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store review attachment resource ID from the [`List all review attachments for an app store review detail`](get-v1-appstorereviewdetails-_id_-appstorereviewattachments.md) response.

## See Also

- [Create an app store review attachment](post-v1-appstorereviewattachments.md)
  Attach a document for App Review to an App Store version.
- [Commit an app store review attachment](patch-v1-appstorereviewattachments-_id_.md)
  Commit an app screenshot after uploading it to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appstorereviewattachments-_id_)*