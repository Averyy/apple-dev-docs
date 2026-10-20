# Read Android to iOS App Mapping Details

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific android to iOS app mapping detail.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/androidToIosAppMappingDetails/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the android to iOS app mapping detail resource ID from the [`Create an Android to iOS App Mapping Detail`](./post-v1-androidtoiosappmappingdetails.md) response.

### Query Parameters

- `fields[androidToIosAppMappingDetails]` ([string]): Additional fields to include for each android to iOS app mapping details resource returned by the response.

  **Allowed Values**: `packageName`, `appSigningKeyPublicCertificateSha256Fingerprints`

## Responses

- `200` OK (`AndroidToIosAppMappingDetailResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Mapping Details
- [Modify an Android to iOS App Mapping Detail](./patch-v1-androidtoiosappmappingdetails-_id_.md)
  Update an Android to iOS app mapping detail.
- [Create an Android to iOS App Mapping Detail](./post-v1-androidtoiosappmappingdetails.md)
  Create a detail that maps an Android app to an iOS app.
- [Delete an Android to iOS Mapping Detail](./delete-v1-androidtoiosappmappingdetails-_id_.md)
  Remove a specific Android to iOS mapping detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-androidtoiosappmappingdetails-_id_)*