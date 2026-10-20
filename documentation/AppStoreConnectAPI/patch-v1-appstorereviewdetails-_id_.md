# Modify an app store review detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the App Store review details, including the contact information, demo account, and notes.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appStoreReviewDetails/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store review detail resource ID from the [`Read the app store review details resource information of an app store version`](./get-v1-appstoreversions-_id_-appstorereviewdetail.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppStoreReviewDetailUpdateRequest`

## Responses

- `200` OK (`AppStoreReviewDetailResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Reading Review Details
- [Create an app store review detail](./post-v1-appstorereviewdetails.md)
  Add App Store review details to an App Store version, including contact and demo account information.
- [Read app store review detail information](./get-v1-appstorereviewdetails-_id_.md)
  Get App Review details you provided, including contact information, demo account, and notes.
- [List App Store review attachment IDs for an App Store review detail](./get-v1-appstorereviewdetails-_id_-relationships-appstorereviewattachments.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appstorereviewdetails-_id_)*