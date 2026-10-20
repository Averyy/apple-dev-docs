# Read app clip card image information for a localized default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the image that appears on the App Clip card, specific to a locale, for a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperienceLocalizations/{id}/appClipHeaderImage`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the default App Clip experience localization resource ID from the [`Read localization information for a default app clip experience`](./get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations.md) response.

### Query Parameters

- `fields[appClipHeaderImages]` ([string]): Additional fields to include for each app clip header image resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `uploadOperations`, `assetDeliveryState`, `appClipDefaultExperienceLocalization`
- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each default App Clip experience localization resource returned by the response.

  **Allowed Values**: `locale`, `subtitle`, `appClipDefaultExperience`, `appClipHeaderImage`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appClipDefaultExperienceLocalization`

## Responses

- `200` OK (`AppClipHeaderImageResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Metadata for Your Default App Clip Experience
- [Read localization information of a default app clip experience](./get-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Get localized metadata that appears on the App Clip card of a specific default App Clip experience.
- [Get the header image ID for an App Clip default experience localization](./get-v1-appclipdefaultexperiencelocalizations-_id_-relationships-appclipheaderimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiencelocalizations-_id_-appclipheaderimage)*