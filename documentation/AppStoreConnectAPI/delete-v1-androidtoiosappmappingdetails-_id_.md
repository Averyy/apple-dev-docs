# Delete an Android to iOS Mapping Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a specific Android to iOS mapping detail.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/androidToIosAppMappingDetails/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the android to iOS app mapping detail resource ID from the [`Create an Android to iOS App Mapping Detail`](./post-v1-androidtoiosappmappingdetails.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Mapping Details
- [Read Android to iOS App Mapping Details](./get-v1-androidtoiosappmappingdetails-_id_.md)
  Get information about a specific android to iOS app mapping detail.
- [Modify an Android to iOS App Mapping Detail](./patch-v1-androidtoiosappmappingdetails-_id_.md)
  Update an Android to iOS app mapping detail.
- [Create an Android to iOS App Mapping Detail](./post-v1-androidtoiosappmappingdetails.md)
  Create a detail that maps an Android app to an iOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-androidtoiosappmappingdetails-_id_)*