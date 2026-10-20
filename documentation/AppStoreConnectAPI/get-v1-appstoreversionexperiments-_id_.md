# Read app store experiment information v1

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific App Store version experiment.

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 2.4

> **Deprecated**: Use [`Read app store experiment information`](./get-v2-appstoreversionexperiments-_id_.md) instead.

## Mentions

- [App Store Connect API 2.4 release notes](./app-store-connect-api-2-4-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionExperiments/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version experiment resource ID from the [`List all experiments for an app store version v1`](./get-v1-appstoreversions-_id_-appstoreversionexperiments.md) response.

### Query Parameters

- `fields[appStoreVersionExperimentTreatments]` ([string]): Additional fields to include for each App Store version experiment treatment resource returned by the response.

  **Allowed Values**: `name`, `appIcon`, `appIconName`, `promotedDate`, `appStoreVersionExperiment`, `appStoreVersionExperimentV2`, `appStoreVersionExperimentTreatmentLocalizations`
- `fields[appStoreVersionExperiments]` ([string]): Additional fields to include for each App Store version experiment resource returned by the response.

  **Allowed Values**: `name`, `trafficProportion`, `state`, `reviewRequired`, `startDate`, `endDate`, `appStoreVersion`, `appStoreVersionExperimentTreatments`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appStoreVersion`, `appStoreVersionExperimentTreatments`
- `limit[appStoreVersionExperimentTreatments]` (integer): The maximum number of related App Store version experiment treatment resources to return.

  **Maximum**: `50`
- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`

## Responses

- `200` OK (`AppStoreVersionExperimentResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing App Store version experiments
- [List all experiments for an app store version v1](./get-v1-appstoreversions-_id_-appstoreversionexperiments.md)
  Get a list of all experiments for an App Store version of an app across all platforms.
- [List all experiments ids for an app store version v1](./get-v1-appstoreversions-_id_-relationships-appstoreversionexperiments.md)
  Get a list of all experiments IDs for an App Store version of an app across all platforms.
- [List all experiments for an app store version](./get-v1-appstoreversions-_id_-appstoreversionexperimentsv2.md)
  Get a list of all experiments for an App Store version of an app across all platforms.
- [List all experiment ids for an app store version](./get-v1-appstoreversions-_id_-relationships-appstoreversionexperimentsv2.md)
  Get a list of all experiments IDs for an App Store version across all platforms.
- [Read app store experiment information](./get-v2-appstoreversionexperiments-_id_.md)
  Get information for a specific App Store version experiment.
- [List all treatments for an app store experiment](./get-v2-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [List treatment IDs for an app store version experiment](./get-v2-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
  Get a list of experiment treatment IDs for a specific App Store version experiment.
- [Create an app store experiment](./post-v2-appstoreversionexperiments.md)
  Add a new experiment to an App Store version.
- [Modify an app store experiment](./patch-v2-appstoreversionexperiments-_id_.md)
  Update the name, the started state, and the proportion of traffic to send to an App Store experiment.
- [Delete an app store experiment](./delete-v2-appstoreversionexperiments-_id_.md)
  Delete a specific App Store version experiment before it starts.
- [List all treatments for an app store experiment v1](./get-v1-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [List treatment IDs for an App Store version experiment](./get-v1-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
- [Modify an app store experiment v1](./patch-v1-appstoreversionexperiments-_id_.md)
  Update the name, the started state, and the proportion of traffic to send to an App Store experiment.
- [Create an app store experiment v1](./post-v1-appstoreversionexperiments.md)
  Add a new experiment to an App Store version.
- [Delete an app store version experiment v1](./delete-v1-appstoreversionexperiments-_id_.md)
  Delete a specific App Store version experiment before it starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionexperiments-_id_)*