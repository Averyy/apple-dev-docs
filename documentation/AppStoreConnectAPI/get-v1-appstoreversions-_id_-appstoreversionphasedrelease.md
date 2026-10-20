# Read the app store version phased release information of an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read the phased release status and configuration for a version with phased release enabled.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/appStoreVersionPhasedRelease`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version resource ID from the [`List all app store versions for an app`](./get-v1-apps-_id_-appstoreversions.md) response.

### Query Parameters

- `fields[appStoreVersionPhasedReleases]` ([string]): Additional fields to include for each App Store version phased release resource returned by the response.

  **Allowed Values**: `phasedReleaseState`, `startDate`, `totalPauseDuration`, `currentDayNumber`

## Responses

- `200` OK (`AppStoreVersionPhasedReleaseWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Release and Review Information
- [Read the app store version submission information of an app store version](./get-v1-appstoreversions-_id_-appstoreversionsubmission.md)
  Get the App Review submission for a specific App Store version.
- [Get the App Store version submission ID for an App Store version](./get-v1-appstoreversions-_id_-relationships-appstoreversionsubmission.md)
- [Read the app store review details resource information of an app store version](./get-v1-appstoreversions-_id_-appstorereviewdetail.md)
  Get the details you provide to App Review so they can test your app.
- [Get the App Store review detail ID for an App Store version](./get-v1-appstoreversions-_id_-relationships-appstorereviewdetail.md)
- [Get the phased release ID for an App Store version](./get-v1-appstoreversions-_id_-relationships-appstoreversionphasedrelease.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-appstoreversionphasedrelease)*