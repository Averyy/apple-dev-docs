# Read Beta Feedback Crash Submission Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific beta feedback crash submission.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaFeedbackCrashSubmissions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `betaFeedbackCrashSubmissions` resource ID from the [`List All Beta Feedback Crash Submissions for an App`](./get-v1-apps-_id_-betafeedbackcrashsubmissions.md) response.

### Query Parameters

- `fields[betaFeedbackCrashSubmissions]` ([string]): **Allowed Values**: `createdDate`, `comment`, `email`, `deviceModel`, `osVersion`, `locale`, `timeZone`, `architecture`, `connectionType`, `pairedAppleWatch`, `appUptimeInMilliseconds`, `diskBytesAvailable`, `diskBytesTotal`, `batteryPercentage`, `screenWidthInPoints`, `screenHeightInPoints`, `appPlatform`, `devicePlatform`, `deviceFamily`, `buildBundleId`, `crashLog`, `build`, `tester`
- `fields[betaTesters]` ([string]): **Allowed Values**: `firstName`, `lastName`, `email`, `inviteType`, `state`, `appDevices`, `apps`, `betaGroups`, `builds`
- `fields[builds]` ([string]): **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `include` ([string]): **Allowed Values**: `build`, `tester`

## Responses

- `200` OK (`BetaFeedbackCrashSubmissionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and deleting beta feedback crash submissions
- [List All Beta Feedback Crash Submissions for an App](./get-v1-apps-_id_-betafeedbackcrashsubmissions.md)
  Get the beta feedback crash submissions for a specific app.
- [List all beta feedback crash submission ids for an app](./get-v1-apps-_id_-relationships-betafeedbackcrashsubmissions.md)
  Get a list of beta feedback crash submissions for a specific app.
- [Read the Crash Log for a Beta Feedback Crash Submission](./get-v1-betafeedbackcrashsubmissions-_id_-crashlog.md)
  Get crash log information for a specific beta feedback crash submission.
- [Get the crash log ID for a beta feedback crash submission](./get-v1-betafeedbackcrashsubmissions-_id_-relationships-crashlog.md)
- [Delete a Beta Feedback Crash Submission](./delete-v1-betafeedbackcrashsubmissions-_id_.md)
  Delete a beta feedback crash submission from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betafeedbackcrashsubmissions-_id_)*