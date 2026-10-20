# Create an app pre-order

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create an app pre-order and set the expected app release date.

**Availability**:
- App Store Connect API 3.0+

## Mentions

- [App Store Connect API 3.1 release notes](./app-store-connect-api-3-1-release-notes.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v2/appAvailabilities`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppAvailabilityV2CreateRequest`

## Responses

- `201` Created (`AppAvailabilityV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing app and territory availability
- [Read app availability](./get-v2-appavailabilities-_id_.md)
  Get information about your app’s availalbility.
- [Read app availablity territories](./get-v2-appavailabilities-_id_-territoryavailabilities.md)
  Read the territory availablity for a specific app.
- [List territory availability IDs for an app availability](./get-v2-appavailabilities-_id_-relationships-territoryavailabilities.md)
  Get a list of territory availability IDs for a specific app availability.
- [Modify the territory availability for an app pre-order](./patch-v1-territoryavailabilities-_id_.md)
  Update the release territories for your app pre-order.
- [End an app pre-order](./post-v1-endappavailabilitypreorders.md)
  End the pre-order for your app and release to store immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-appavailabilities)*