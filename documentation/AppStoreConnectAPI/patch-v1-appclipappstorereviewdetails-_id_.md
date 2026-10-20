# Modify app store review details for an app clip

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update App Clip metadata you provide to App Store Review.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipAppStoreReviewDetails/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app clip App Store review detail resource ID from the [`Read the app store review detail for a default app clip experience`](./get-v1-appclipdefaultexperiences-_id_-appclipappstorereviewdetail.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppClipAppStoreReviewDetailUpdateRequest`

The request body you use to update the App Store review details of an App Clip.

## Responses

- `200` OK (`AppClipAppStoreReviewDetailResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing App Review Details for Your App Clip
- [Read the app store review details of an app clip](./get-v1-appclipappstorereviewdetails-_id_.md)
  Get App Store Review details for an App Clip.
- [Create app store review details for an app clip](./post-v1-appclipappstorereviewdetails.md)
  Provide App Clip metadata required by App Store Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipappstorereviewdetails-_id_)*