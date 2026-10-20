# Read the app store review details of an app clip

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get App Store Review details for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipAppStoreReviewDetails/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app clip App Store review detail resource ID from the [`Read the app store review detail for a default app clip experience`](./get-v1-appclipdefaultexperiences-_id_-appclipappstorereviewdetail.md) response.

### Query Parameters

- `fields[appClipAppStoreReviewDetails]` ([string]): Additional fields to include for each app clip App Store review detail resource returned by the response.

  **Allowed Values**: `invocationUrls`, `appClipDefaultExperience`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appClipDefaultExperience`
- `fields[appClipDefaultExperiences]` ([string]): **Allowed Values**: `action`, `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`

## Responses

- `200` OK (`AppClipAppStoreReviewDetailResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing App Review Details for Your App Clip
- [Create app store review details for an app clip](./post-v1-appclipappstorereviewdetails.md)
  Provide App Clip metadata required by App Store Review.
- [Modify app store review details for an app clip](./patch-v1-appclipappstorereviewdetails-_id_.md)
  Update App Clip metadata you provide to App Store Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipappstorereviewdetails-_id_)*