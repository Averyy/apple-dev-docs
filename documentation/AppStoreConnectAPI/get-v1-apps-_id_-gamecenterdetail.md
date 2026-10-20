# Read the state of game center for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get Game Center detail information for an app.

**Availability**:
- App Store Connect API 3.0+

## Mentions

- [Configuring Game center activities](./configuring-game-center-activities.md)
- [Configuring Game Center challenges](./configuring-game-center-challenges.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/gameCenterDetail`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[gameCenterAchievementReleases]` ([string]): Additional fields to include for each Game Center achievement release resource returned by the response.

  **Allowed Values**: `live`, `gameCenterDetail`, `gameCenterAchievement`
- `fields[gameCenterAchievements]` ([string]): Additional fields to include for each Game Center achievement resource returned by the response.

  **Allowed Values**: `referenceName`, `vendorIdentifier`, `points`, `showBeforeEarned`, `repeatable`, `archived`, `activityProperties`, `gameCenterDetail`, `gameCenterGroup`, `groupAchievement`, `localizations`, `releases`, `activity`, `versions`
- `fields[gameCenterAppVersions]` ([string]): Additional fields to include for each Game Center app version resource returned by the response.

  **Allowed Values**: `enabled`, `compatibilityVersions`, `appStoreVersion`
- `fields[gameCenterDetails]` ([string]): Additional fields to include for each Game Center detail resource returned by the response.

  **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[gameCenterGroups]` ([string]): Additional fields to include for each Game Center group resource returned by the response.

  **Allowed Values**: `referenceName`, `gameCenterDetails`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`
- `fields[gameCenterLeaderboardReleases]` ([string]): Additional fields to include for each Game Center leaderboard release resource returned by the response.

  **Allowed Values**: `live`, `gameCenterDetail`, `gameCenterLeaderboard`
- `fields[gameCenterLeaderboardSetReleases]` ([string]): Additional fields to include for each Game Center leaderboard set release resource returned by the response.

  **Allowed Values**: `live`, `gameCenterDetail`, `gameCenterLeaderboardSet`
- `fields[gameCenterLeaderboardSets]` ([string]): Additional fields to include for each Game Center leaderboard set resource returned by the response.

  **Allowed Values**: `referenceName`, `vendorIdentifier`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboardSet`, `localizations`, `gameCenterLeaderboards`, `releases`, `versions`
- `fields[gameCenterLeaderboards]` ([string]): Additional fields to include for each Game Center leaderboard resource returned by the response.

  **Allowed Values**: `defaultFormatter`, `referenceName`, `vendorIdentifier`, `submissionType`, `scoreSortType`, `scoreRangeStart`, `scoreRangeEnd`, `recurrenceStartDate`, `recurrenceDuration`, `recurrenceRule`, `archived`, `activityProperties`, `visibility`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboard`, `gameCenterLeaderboardSets`, `localizations`, `releases`, `activity`, `challenge`, `gameCenterScoreModerations`, `versions`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `challengesMinimumPlatformVersions`
- `limit[achievementReleases]` (integer) *(deprecated)*: The maximum number of related achievement releases resources to return.

  **Maximum**: `50`
- `limit[gameCenterAchievements]` (integer) *(deprecated)*: The maximum number of related Game Center achievements resources to return.

  **Maximum**: `50`
- `limit[gameCenterAppVersions]` (integer): The maximum number of related Game Center app versions resources to return.

  **Maximum**: `50`
- `limit[gameCenterLeaderboardSets]` (integer) *(deprecated)*: The maximum number of related Game Center leaderboard sets resources to return.

  **Maximum**: `50`
- `limit[gameCenterLeaderboards]` (integer) *(deprecated)*: The maximum number of related Game Center leaderboards resources to return.

  **Maximum**: `50`
- `limit[leaderboardReleases]` (integer) *(deprecated)*: The maximum number of related leaderboard releases resources to return.

  **Maximum**: `50`
- `limit[leaderboardSetReleases]` (integer) *(deprecated)*: The maximum number of related leaderboard set releases resources to return.

  **Maximum**: `50`
- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[gameCenterActivities]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `playStyle`, `minimumPlayersCount`, `maximumPlayersCount`, `supportsPartyCode`, `archived`, `properties`, `gameCenterDetail`, `gameCenterGroup`, `achievements`, `achievementsV2`, `leaderboards`, `leaderboardsV2`, `versions`
- `fields[gameCenterActivityVersionReleases]` ([string]): **Allowed Values**: `version`
- `fields[gameCenterChallengeVersionReleases]` ([string]): **Allowed Values**: `version`
- `fields[gameCenterChallenges]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `archived`, `challengeType`, `repeatable`, `gameCenterDetail`, `gameCenterGroup`, `versions`, `leaderboard`, `leaderboardV2`
- `limit[activityReleases]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[challengeReleases]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[challengesMinimumPlatformVersions]` (integer): **Maximum**: `50`
- `limit[gameCenterAchievementsV2]` (integer): **Maximum**: `50`
- `limit[gameCenterActivities]` (integer): **Maximum**: `50`
- `limit[gameCenterChallenges]` (integer): **Maximum**: `50`
- `limit[gameCenterLeaderboardSetsV2]` (integer): **Maximum**: `50`
- `limit[gameCenterLeaderboardsV2]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`GameCenterDetailResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Game Center detail information
- [Get the Game Center detail ID for an app](./get-v1-apps-_id_-relationships-gamecenterdetail.md)
- [List Game Center-enabled version IDs for an app](./get-v1-apps-_id_-relationships-gamecenterenabledversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-gamecenterdetail)*