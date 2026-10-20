# List Availability for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

The data structure that represents a get-v1-apps-{id}-app availability v2 resource.

**Availability**:
- App Store Connect API 3.6+

#### Overview

Get a list of availabilities for a specific app.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appAvailabilityV2`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[appAvailabilities]` ([string]): **Allowed Values**: `availableInNewTerritories`, `territoryAvailabilities`
- `include` ([string]): **Allowed Values**: `territoryAvailabilities`
- `fields[territoryAvailabilities]` ([string]): **Allowed Values**: `available`, `releaseDate`, `preOrderEnabled`, `preOrderPublishDate`, `contentStatuses`, `territory`
- `limit[territoryAvailabilities]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`AppAvailabilityV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting and managing an app’s availability
- [Get the app availability ID for an app](./get-v1-apps-_id_-relationships-appavailabilityv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appavailabilityv2)*