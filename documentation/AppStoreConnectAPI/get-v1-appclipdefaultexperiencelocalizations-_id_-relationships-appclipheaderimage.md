# Get the header image ID for an App Clip default experience localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperienceLocalizations/{id}/relationships/appClipHeaderImage`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`AppClipDefaultExperienceLocalizationAppClipHeaderImageLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Metadata for Your Default App Clip Experience
- [Read localization information of a default app clip experience](./get-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Get localized metadata that appears on the App Clip card of a specific default App Clip experience.
- [Read app clip card image information for a localized default app clip experience](./get-v1-appclipdefaultexperiencelocalizations-_id_-appclipheaderimage.md)
  Get the image that appears on the App Clip card, specific to a locale, for a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiencelocalizations-_id_-relationships-appclipheaderimage)*