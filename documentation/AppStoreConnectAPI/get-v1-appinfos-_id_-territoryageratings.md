# List Territory Age Ratings for an App Info

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all territory age ratings for a specific app info.

**Availability**:
- App Store Connect API 4.1+

## Mentions

- [App Store Connect API 4.1 release notes](./app-store-connect-api-4-1-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/territoryAgeRatings`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `appInfo` resource ID from the [`List all app infos for an app`](./get-v1-apps-_id_-appinfos.md) response.

### Query Parameters

- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response.

  **Allowed Values**: `currency`
- `fields[territoryAgeRatings]` ([string]): Additional fields to include for each territory age rating resource returned by the response.

  **Allowed Values**: `appStoreAgeRating`, `territory`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `territory`
- `limit` (integer): The maximum number of territory age rating resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`TerritoryAgeRatingsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading territory age rating
- [List territory age rating IDs for an app info](./get-v1-appinfos-_id_-relationships-territoryageratings.md)
  List all territory age rating IDs for a specific app info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-territoryageratings)*