# List all icons for a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all the icons for various platforms delivered with a build.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/icons`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[buildIcons]` ([string]): **Allowed Values**: `iconAsset`, `iconType`, `masked`, `name`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`BuildIconsWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-icons)*