# Create a Featuring Nomination

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Tell Apple about your upcoming app or feature.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/nominations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `NominationCreateRequest`

## Responses

- `201` Created (`NominationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing nominations
- [List Nominations](./get-v1-nominations.md)
  Get all featuring nominations.
- [Read Details for a Nomination](./get-v1-nominations-_id_.md)
  Get information for a specific featuring nomination.
- [Modify a Nomination](./patch-v1-nominations-_id_.md)
  Update a specific featuring nomination.
- [Delete a Featuring Nomination](./delete-v1-nominations-_id_.md)
  Remove a specific featuring nomination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-nominations)*