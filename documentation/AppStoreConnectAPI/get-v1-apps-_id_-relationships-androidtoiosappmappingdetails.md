# List the IDs of Android to iOS App Mapping Details for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the IDs of Android to iOS app mapping details for a specific app.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/androidToIosAppMappingDetails`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `limit` (integer): The maximum number of Android to iOS app mapping detail resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppAndroidToIosAppMappingDetailsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Android to iOS app mapping information
- [Read the Android to iOS App Mapping Details for an App](./get-v1-apps-_id_-androidtoiosappmappingdetails.md)
  Get details about the Android to iOS app mapping for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-androidtoiosappmappingdetails)*