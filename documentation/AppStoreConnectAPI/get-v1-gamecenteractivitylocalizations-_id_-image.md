# Read Image Information for an Activity Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about the image for a specific Game Center activity localization.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterActivityLocalizations/{id}/image`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterActivityImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `uploadOperations`, `assetDeliveryState`

## Responses

- `200` OK (`GameCenterActivityImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Game Center activities
- [Read Activity Localization Information](./get-v1-gamecenteractivitylocalizations-_id_.md)
  Get information for a specific Game Center activity localization.
- [Get the image ID for a Game Center activity localization](./get-v1-gamecenteractivitylocalizations-_id_-relationships-image.md)
- [Add an Activity Localization](./post-v1-gamecenteractivitylocalizations.md)
  Add a localization for a specific Game Center activity.
- [Modify an Activity Localization](./patch-v1-gamecenteractivitylocalizations-_id_.md)
  Update localization information for a specific Game Center activity.
- [Delete an Activity Localization](./delete-v1-gamecenteractivitylocalizations-_id_.md)
  Remove a specific localization from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenteractivitylocalizations-_id_-image)*