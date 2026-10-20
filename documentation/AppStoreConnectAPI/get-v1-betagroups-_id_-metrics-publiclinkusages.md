# Read Public Link Usage Metrics for a Beta Group

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get public link usage metrics for a specific beta group.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaGroups/{id}/metrics/publicLinkUsages`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `betaGroups` resource ID from the [`List beta groups`](./get-v1-betagroups.md) response.

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`BetaPublicLinkUsagesV1MetricResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betagroups-_id_-metrics-publiclinkusages)*