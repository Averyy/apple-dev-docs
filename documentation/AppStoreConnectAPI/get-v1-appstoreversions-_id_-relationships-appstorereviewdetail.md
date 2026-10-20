# Get the App Store review detail ID for an App Store version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/relationships/appStoreReviewDetail`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`AppStoreVersionAppStoreReviewDetailLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Release and Review Information
- [Read the app store version submission information of an app store version](./get-v1-appstoreversions-_id_-appstoreversionsubmission.md)
  Get the App Review submission for a specific App Store version.
- [Get the App Store version submission ID for an App Store version](./get-v1-appstoreversions-_id_-relationships-appstoreversionsubmission.md)
- [Read the app store review details resource information of an app store version](./get-v1-appstoreversions-_id_-appstorereviewdetail.md)
  Get the details you provide to App Review so they can test your app.
- [Read the app store version phased release information of an app store version](./get-v1-appstoreversions-_id_-appstoreversionphasedrelease.md)
  Read the phased release status and configuration for a version with phased release enabled.
- [Get the phased release ID for an App Store version](./get-v1-appstoreversions-_id_-relationships-appstoreversionphasedrelease.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-relationships-appstorereviewdetail)*