# List all advanced app clip experiences for an app clip

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get all advanced App Clip experiences for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClips/{id}/appClipAdvancedExperiences`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app clip resource ID from the [`List all app clips for an app`](./get-v1-apps-_id_-appclips.md) response.

### Query Parameters

- `fields[appClipAdvancedExperienceLocalizations]` ([string]): Additional fields to include for each advanced App Clip experience localization resource returned by the response.

  **Allowed Values**: `language`, `title`, `subtitle`
- `fields[appClipAdvancedExperiences]` ([string]): Additional fields to include for each advanced App Clip experience resource returned by the response.

  **Allowed Values**: `link`, `version`, `status`, `action`, `isPoweredBy`, `place`, `placeStatus`, `businessCategory`, `defaultLanguage`, `appClip`, `headerImage`, `localizations`
- `filter[action]` ([string]): Filter the returned advanced App Clip experiences using the verb that appears on the App Clip card.

  **Allowed Values**: `OPEN`, `VIEW`, `PLAY`
- `filter[placeStatus]` ([string]): Filter the returned advanced App Clip experiences using the status of the associated place in Apple Maps.

  **Allowed Values**: `PENDING`, `MATCHED`, `NO_MATCH`
- `filter[status]` ([string]): Filter the returned advanced App Clip experiences using their status.

  **Allowed Values**: `RECEIVED`, `DEACTIVATED`, `APP_TRANSFER_IN_PROGRESS`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appClip`, `headerImage`, `localizations`
- `limit` (integer): The maximum number of advanced App Clip experience resources to return.

  **Maximum**: `200`
- `limit[localizations]` (integer): The maximum number of related localizations resources to return.

  **Maximum**: `50`
- `fields[appClips]` ([string]): Additional fields to include for each app clip resource returned by the response.

  **Allowed Values**: `bundleId`, `app`, `appClipDefaultExperiences`, `appClipAdvancedExperiences`
- `fields[appClipAdvancedExperienceImages]` ([string]): Additional fields to include for each advanced App Clip experience image resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `uploadOperations`, `assetDeliveryState`

## Responses

- `200` OK (`AppClipAdvancedExperiencesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting App Clip Experiences
- [List all default app clip experiences for an app clip](./get-v1-appclips-_id_-appclipdefaultexperiences.md)
  Get all default App Clip experiences for an App Clip.
- [List App Clip advanced experience IDs for an App Clip](./get-v1-appclips-_id_-relationships-appclipadvancedexperiences.md)
- [List default experience IDs for an App Clip](./get-v1-appclips-_id_-relationships-appclipdefaultexperiences.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclips-_id_-appclipadvancedexperiences)*