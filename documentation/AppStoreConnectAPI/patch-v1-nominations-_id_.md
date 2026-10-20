# Modify a Nomination

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific featuring nomination.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/nominations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the nomination resource ID from the [`List Nominations`](./get-v1-nominations.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `NominationUpdateRequest`

## Responses

- `200` OK (`NominationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing nominations
- [Create a Featuring Nomination](./post-v1-nominations.md)
  Tell Apple about your upcoming app or feature.
- [List Nominations](./get-v1-nominations.md)
  Get all featuring nominations.
- [Read Details for a Nomination](./get-v1-nominations-_id_.md)
  Get information for a specific featuring nomination.
- [Delete a Featuring Nomination](./delete-v1-nominations-_id_.md)
  Remove a specific featuring nomination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-nominations-_id_)*