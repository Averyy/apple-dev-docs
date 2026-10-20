# Create app store review details for an app clip

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Provide App Clip metadata required by App Store Review.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appClipAppStoreReviewDetails`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppClipAppStoreReviewDetailCreateRequest`

The request body you use to create App Store detail information.

## Responses

- `201` Created (`AppClipAppStoreReviewDetailResponse`, `application/json`): The request completed successfully and a new App Clip App Store Review Details resource has been created.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing App Review Details for Your App Clip
- [Read the app store review details of an app clip](./get-v1-appclipappstorereviewdetails-_id_.md)
  Get App Store Review details for an App Clip.
- [Modify app store review details for an app clip](./patch-v1-appclipappstorereviewdetails-_id_.md)
  Update App Clip metadata you provide to App Store Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appclipappstorereviewdetails)*