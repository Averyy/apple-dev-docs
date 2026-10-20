# List the Items in a Review Submission

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all the items in a specific review submission.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/reviewSubmissions/{id}/items`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the review submissions resource. Obtain the app resource ID from the [`List Review Submissions for an App`](./get-v1-reviewsubmissions.md) response.

### Query Parameters

- `fields[reviewSubmissionItems]` ([string]): **Allowed Values**: `state`, `appStoreVersion`, `appCustomProductPageVersion`, `appStoreVersionExperiment`, `appStoreVersionExperimentV2`, `appEvent`, `appAssetLibraryImage`, `appAssetLibraryVideo`, `backgroundAssetVersion`, `gameCenterAchievementVersion`, `gameCenterActivityVersion`, `gameCenterChallengeVersion`, `gameCenterLeaderboardSetVersion`, `gameCenterLeaderboardVersion`, `inAppPurchaseVersion`, `subscriptionVersion`, `subscriptionGroupVersion`
- `limit` (integer): **Maximum**: `200`
- `fields[appStoreVersionExperiments]` ([string]): **Allowed Values**: `name`, `trafficProportion`, `state`, `reviewRequired`, `startDate`, `endDate`, `appStoreVersion`, `appStoreVersionExperimentTreatments`, `platform`, `app`, `latestControlVersion`, `controlVersions`
- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[appCustomProductPageVersions]` ([string]): **Allowed Values**: `version`, `state`, `deepLink`, `appCustomProductPage`, `appCustomProductPageLocalizations`
- `fields[appEvents]` ([string]): **Allowed Values**: `referenceName`, `badge`, `eventState`, `deepLink`, `purchaseRequirement`, `primaryLocale`, `priority`, `purpose`, `territorySchedules`, `archivedTerritorySchedules`, `localizations`
- `include` ([string]): **Allowed Values**: `appStoreVersion`, `appCustomProductPageVersion`, `appStoreVersionExperiment`, `appStoreVersionExperimentV2`, `appEvent`, `appAssetLibraryImage`, `appAssetLibraryVideo`, `backgroundAssetVersion`, `gameCenterAchievementVersion`, `gameCenterActivityVersion`, `gameCenterChallengeVersion`, `gameCenterLeaderboardSetVersion`, `gameCenterLeaderboardVersion`, `inAppPurchaseVersion`, `subscriptionVersion`, `subscriptionGroupVersion`
- `fields[appAssetLibraryImages]` ([string]): **Allowed Values**: `category`, `createdDate`, `lastModifiedDate`, `fileName`, `fileSize`, `imageAsset`, `referenceName`, `specId`, `state`, `stateDetails`, `uploadOperations`, `placements`
- `fields[appAssetLibraryVideos]` ([string]): **Allowed Values**: `category`, `createdDate`, `lastModifiedDate`, `fileName`, `fileSize`, `previewFrameImage`, `previewFrameTimeCode`, `referenceName`, `specId`, `state`, `stateDetails`, `uploadOperations`, `videoAsset`, `placements`
- `fields[backgroundAssetVersions]` ([string]): **Allowed Values**: `createdDate`, `platforms`, `state`, `stateDetails`, `version`, `locale`, `backgroundAsset`, `internalBetaRelease`, `externalBetaRelease`, `appStoreRelease`, `assetFile`, `manifestFile`, `backgroundAssetUploadFiles`
- `fields[gameCenterAchievementVersions]` ([string]): **Allowed Values**: `version`, `state`, `achievement`, `localizations`
- `fields[gameCenterActivityVersions]` ([string]): **Allowed Values**: `version`, `state`, `fallbackUrl`, `activity`, `localizations`, `defaultImage`, `releases`
- `fields[gameCenterChallengeVersions]` ([string]): **Allowed Values**: `version`, `state`, `challenge`, `localizations`, `releases`, `defaultImage`
- `fields[gameCenterLeaderboardSetVersions]` ([string]): **Allowed Values**: `version`, `state`, `leaderboardSet`, `localizations`
- `fields[gameCenterLeaderboardVersions]` ([string]): **Allowed Values**: `version`, `state`, `leaderboard`, `localizations`
- `fields[inAppPurchaseVersions]` ([string]): **Allowed Values**: `version`, `state`, `inAppPurchase`, `image`, `images`, `localizations`
- `fields[subscriptionGroupVersions]` ([string]): **Allowed Values**: `version`, `state`, `subscriptionGroup`, `localizations`
- `fields[subscriptionVersions]` ([string]): **Allowed Values**: `version`, `state`, `subscription`, `image`, `images`, `localizations`

## Responses

- `200` OK (`ReviewSubmissionItemsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List Review Submissions for an App](./get-v1-reviewsubmissions.md)
  List recent and current review submissions for a specific app.
- [Read Review Submission Information](./get-v1-reviewsubmissions-_id_.md)
  Read information about a specific review submisison.
- [List item IDs](./get-v1-reviewsubmissions-_id_-relationships-items.md)
  Get the list of item IDs for a specific review submission.
- [List review submission IDs](./get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.
- [Modify a Review Submission](./patch-v1-reviewsubmissions-_id_.md)
  Edit the details or contents of a review submission.
- [Create a Review Submission](./post-v1-reviewsubmissions.md)
  Create a review submission for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-reviewsubmissions-_id_-items)*