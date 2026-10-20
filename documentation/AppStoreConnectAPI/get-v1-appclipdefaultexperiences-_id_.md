# Read default app clip experience information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a specific default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the default App Clip experience resource ID from the [`List all default app clip experiences for an app clip`](./get-v1-appclips-_id_-appclipdefaultexperiences.md) response.

### Query Parameters

- `fields[appClipAppStoreReviewDetails]` ([string]): Additional fields to include for each app clip App Store review detail resource returned by the response.

  **Allowed Values**: `invocationUrls`, `appClipDefaultExperience`
- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each default App Clip experience localization resource returned by the response.

  **Allowed Values**: `locale`, `subtitle`, `appClipDefaultExperience`, `appClipHeaderImage`
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each default App Clip experience resource returned by the response.

  **Allowed Values**: `action`, `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.

  **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`
- `limit[appClipDefaultExperienceLocalizations]` (integer): The maximum number of related default App Clip experience localizations resources to return.

  **Maximum**: `50`
- `fields[appClips]` ([string]): **Allowed Values**: `bundleId`, `app`, `appClipDefaultExperiences`, `appClipAdvancedExperiences`

## Responses

- `200` OK (`AppClipDefaultExperienceResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Default App Clip Experience Information
- [Read the app store review detail for a default app clip experience](./get-v1-appclipdefaultexperiences-_id_-appclipappstorereviewdetail.md)
  Get App Store Review details for a specific default App Clip experience.
- [Get the App Store review detail ID for an App Clip default experience](./get-v1-appclipdefaultexperiences-_id_-relationships-appclipappstorereviewdetail.md)
- [Read localization information for a default app clip experience](./get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations.md)
  Get localized metadata that appears on the App Clip card for a specific default App Clip experience.
- [List localization IDs for an App Clip default experience](./get-v1-appclipdefaultexperiences-_id_-relationships-appclipdefaultexperiencelocalizations.md)
- [Read app store version information for a default app clip experience](./get-v1-appclipdefaultexperiences-_id_-releasewithappstoreversion.md)
  Get App Store Version information for a default App Clip experience.
- [Get the app store versions resource id for a default app clip experience](./get-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion.md)
  Get IDs for App Store Versions related to a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiences-_id_)*