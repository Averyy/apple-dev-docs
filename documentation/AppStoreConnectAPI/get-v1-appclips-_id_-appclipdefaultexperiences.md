# List all default app clip experiences for an app clip

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get all default App Clip experiences for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClips/{id}/appClipDefaultExperiences`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app clip resource ID from the [`List all app clips for an app`](./get-v1-apps-_id_-appclips.md) response.

### Query Parameters

- `exists[releaseWithAppStoreVersion]` (boolean): Filter the returned default App Clip experiences to include only those that have (true) or don’t have (false) a related App Store version.
- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each default App Clip experience localization resource returned by the response.

  **Allowed Values**: `locale`, `subtitle`, `appClipDefaultExperience`, `appClipHeaderImage`
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each default App Clip experience resource returned by the response.

  **Allowed Values**: `action`, `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`
- `limit` (integer): The maximum number of default App Clip experience resources to return.

  **Maximum**: `200`
- `limit[appClipDefaultExperienceLocalizations]` (integer): The maximum number of related default App Clip experience localizations resources to return.

  **Maximum**: `50`
- `fields[appClips]` ([string]): Additional fields to include for each app clip resource returned by the response.

  **Allowed Values**: `bundleId`, `app`, `appClipDefaultExperiences`, `appClipAdvancedExperiences`
- `fields[appClipAppStoreReviewDetails]` ([string]): Additional fields to include for each app clip App Store review detail resource returned by the response.

  **Allowed Values**: `invocationUrls`, `appClipDefaultExperience`
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.

  **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`

## Responses

- `200` OK (`AppClipDefaultExperiencesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting App Clip Experiences
- [List all advanced app clip experiences for an app clip](./get-v1-appclips-_id_-appclipadvancedexperiences.md)
  Get all advanced App Clip experiences for an App Clip.
- [List App Clip advanced experience IDs for an App Clip](./get-v1-appclips-_id_-relationships-appclipadvancedexperiences.md)
- [List default experience IDs for an App Clip](./get-v1-appclips-_id_-relationships-appclipdefaultexperiences.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclips-_id_-appclipdefaultexperiences)*