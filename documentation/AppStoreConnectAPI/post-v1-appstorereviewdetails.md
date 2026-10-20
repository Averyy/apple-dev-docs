# Create an app store review detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add App Store review details to an App Store version, including contact and demo account information.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appStoreReviewDetails`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppStoreReviewDetailCreateRequest`

## Responses

- `201` Created (`AppStoreReviewDetailResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Reading Review Details
- [Read app store review detail information](./get-v1-appstorereviewdetails-_id_.md)
  Get App Review details you provided, including contact information, demo account, and notes.
- [List App Store review attachment IDs for an App Store review detail](./get-v1-appstorereviewdetails-_id_-relationships-appstorereviewattachments.md)
- [Modify an app store review detail](./patch-v1-appstorereviewdetails-_id_.md)
  Update the App Store review details, including the contact information, demo account, and notes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appstorereviewdetails)*