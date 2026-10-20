# List All Beta Feedback Crash Submissions for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the beta feedback crash submissions for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/betaFeedbackCrashSubmissions`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[betaFeedbackCrashSubmissions]` ([string]): Additional fields to include for each beta feedback crash submission resource returned by the response.

  **Allowed Values**: `createdDate`, `comment`, `email`, `deviceModel`, `osVersion`, `locale`, `timeZone`, `architecture`, `connectionType`, `pairedAppleWatch`, `appUptimeInMilliseconds`, `diskBytesAvailable`, `diskBytesTotal`, `batteryPercentage`, `screenWidthInPoints`, `screenHeightInPoints`, `appPlatform`, `devicePlatform`, `deviceFamily`, `buildBundleId`, `crashLog`, `build`, `tester`
- `fields[betaTesters]` ([string]): Additional fields to include for each beta tester resource returned by the response.

  **Allowed Values**: `firstName`, `lastName`, `email`, `inviteType`, `state`, `appDevices`, `apps`, `betaGroups`, `builds`
- `fields[builds]` ([string]): Additional fields to include for each build resource returned by the response.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `filter[appPlatform]` ([string]): Filter the returned beta feedback crash submissions by app platform.

  **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `filter[build.preReleaseVersion]` ([string]): Filter the returned beta feedback crash submissions by build pre-release version.
- `filter[build]` ([string]): Filter the returned beta feedback crash submissions by build.
- `filter[deviceModel]` ([string]): Filter the returned beta feedback crash submissions by device model.
- `filter[devicePlatform]` ([string]): Filter the returned beta feedback crash submissions by device platform.

  **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `filter[osVersion]` ([string]): Filter the returned beta feedback crash submissions by OS version.
- `filter[tester]` ([string]): Filter the returned beta feedback crash submissions by tester.
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `build`, `tester`
- `limit` (integer): The maximum number of beta feedback crash submission resources to return.

  **Maximum**: `200`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `createdDate`, `-createdDate`

## Responses

- `200` OK (`BetaFeedbackCrashSubmissionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting beta feedback
- [List All Beta Feedback Screenshot Submissions for an App](./get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md)
  Get beta feedback screenshot submissions for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betafeedbackcrashsubmissions)*