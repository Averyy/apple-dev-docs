# Read advanced app clip experience information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperiences/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the advanced App Clip experience resource ID from the [`List all advanced app clip experiences for an app clip`](./get-v1-appclips-_id_-appclipadvancedexperiences.md) response.

### Query Parameters

- `fields[appClipAdvancedExperiences]` ([string]): Additional fields to include for each advanced App Clip experiences resource returned by the response.

  **Allowed Values**: `link`, `version`, `status`, `action`, `isPoweredBy`, `place`, `placeStatus`, `businessCategory`, `defaultLanguage`, `appClip`, `headerImage`, `localizations`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appClip`, `headerImage`, `localizations`
- `limit[localizations]` (integer): The maximum number of related localizations resources to return.

  **Maximum**: `50`
- `fields[appClipAdvancedExperienceImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `uploadOperations`, `assetDeliveryState`
- `fields[appClipAdvancedExperienceLocalizations]` ([string]): **Allowed Values**: `language`, `title`, `subtitle`
- `fields[appClips]` ([string]): **Allowed Values**: `bundleId`, `app`, `appClipDefaultExperiences`, `appClipAdvancedExperiences`

## Responses

- `200` OK (`AppClipAdvancedExperienceResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting and Managing Advanced App Clip Experiences
- [Create an advanced app clip experience](./post-v1-appclipadvancedexperiences.md)
  Configure a new advanced App Clip experience.
- [Modify and delete an advanced app clip experience](./patch-v1-appclipadvancedexperiences-_id_.md)
  Update and delete an existing advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipadvancedexperiences-_id_)*