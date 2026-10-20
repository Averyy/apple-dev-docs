# Delete an app store review attachment

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove an attachment before you send your app to App Review.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appStoreReviewAttachments/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store review attachment resource ID from the [`List all review attachments for an app store review detail`](./get-v1-appstorereviewdetails-_id_-appstorereviewattachments.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Attachments
- [Create an app store review attachment](./post-v1-appstorereviewattachments.md)
  Attach a document for App Review to an App Store version.
- [Commit an app store review attachment](./patch-v1-appstorereviewattachments-_id_.md)
  Commit an app screenshot after uploading it to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appstorereviewattachments-_id_)*