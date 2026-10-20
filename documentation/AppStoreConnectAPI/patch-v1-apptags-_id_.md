# Modify App Tags

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Opt out of app tags for a specific app.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appTags/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app tag resource ID from the [`List App Tags`](./get-v1-apps-_id_-apptags.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppTagUpdateRequest`

## Responses

- `200` OK (`AppTagResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-apptags-_id_)*