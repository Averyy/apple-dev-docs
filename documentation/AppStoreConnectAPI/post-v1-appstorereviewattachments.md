# Create an app store review attachment

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Attach a document for App Review to an App Store version.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appStoreReviewAttachments`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppStoreReviewAttachmentCreateRequest`

## Responses

- `201` Created (`AppStoreReviewAttachmentResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Attachments
- [Commit an app store review attachment](./patch-v1-appstorereviewattachments-_id_.md)
  Commit an app screenshot after uploading it to the App Store.
- [Delete an app store review attachment](./delete-v1-appstorereviewattachments-_id_.md)
  Remove an attachment before you send your app to App Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appstorereviewattachments)*