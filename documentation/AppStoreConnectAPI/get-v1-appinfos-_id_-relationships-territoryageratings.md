# List territory age rating IDs for an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all territory age rating IDs for a specific app info.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/relationships/territoryAgeRatings`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `appInfo` resource ID from the [`List all app infos for an app`](./get-v1-apps-_id_-appinfos.md) response.

### Query Parameters

- `limit` (integer): The maximum number of territory age rating resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppInfoTerritoryAgeRatingsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading territory age rating
- [List Territory Age Ratings for an App Info](./get-v1-appinfos-_id_-territoryageratings.md)
  List all territory age ratings for a specific app info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-relationships-territoryageratings)*