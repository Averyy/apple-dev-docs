# List build IDs for a CI build run

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildRuns/{id}/relationships/builds`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`CiBuildRunBuildsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Build Information
- [Read xcode cloud build information](./get-v1-cibuildruns-_id_.md)
  Get information about a specific Xcode Cloud build.
- [List all actions for an xcode cloud build](./get-v1-cibuildruns-_id_-actions.md)
  List all actions Xcode Cloud performed during a specific build.
- [List all builds xcode cloud created in app store connect](./get-v1-cibuildruns-_id_-builds.md)
  List All App Store Connect and TestFlight Builds when it performed a build.
- [List action IDs for a CI build run](./get-v1-cibuildruns-_id_-relationships-actions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildruns-_id_-relationships-builds)*