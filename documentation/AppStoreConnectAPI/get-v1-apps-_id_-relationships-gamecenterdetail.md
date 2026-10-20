# Get the Game Center detail ID for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/gameCenterDetail`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`AppGameCenterDetailLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Game Center detail information
- [Read the state of game center for an app](./get-v1-apps-_id_-gamecenterdetail.md)
  Get Game Center detail information for an app.
- [List Game Center-enabled version IDs for an app](./get-v1-apps-_id_-relationships-gamecenterenabledversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-gamecenterdetail)*